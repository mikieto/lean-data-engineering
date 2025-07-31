import pandas as pd
import numpy as np
import argparse
import subprocess
import json
import sys
import os

# --- Helper Functions ---
def calculate_psi(baseline, current, bins=10):
    """Calculate the Population Stability Index."""
    baseline_counts = np.histogram(baseline, bins)[0]
    current_counts = np.histogram(current, bins)[0]

    # Avoid division by zero
    baseline_dist = (baseline_counts + 0.5) / baseline_counts.sum()
    current_dist = (current_counts + 0.5) / current_counts.sum()

    psi = np.sum((current_dist - baseline_dist) * np.log(current_dist / baseline_dist))
    return psi

def check_required_columns(df, required_cols):
    """Check if all required columns are present in the DataFrame."""
    missing_cols = set(required_cols) - set(df.columns)
    if missing_cols:
        print(f"❌ Validation Failed: Missing required columns: {', '.join(missing_cols)}")
        return False
    return True

def run_opa_policy(data_dict, policy_file):
    """Run OPA policy against the data."""
    try:
        opa_input = json.dumps({"input": data_dict})
        result = subprocess.run(
            ["opa", "eval", "-d", policy_file, "-I", f"data.policy.deny"],
            input=opa_input, text=True, capture_output=True, check=True
        )
        violations = json.loads(result.stdout).get("result", [{}])[0].get("expressions", [])
        if violations:
            for v in violations:
                print(f"🛡️ Policy Violation (Guard): {v['value']}")
            return False
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError) as e:
        print(f"OPA execution error: {e}")
        return False

# --- Main Logic ---
def main():
    parser = argparse.ArgumentParser(description="Data Quality Validation Script")
    parser.add_argument("--datafile", required=True, help="Path to the data CSV file")
    parser.add_argument("--policy", help="Path to the OPA policy file")
    parser.add_argument("--baseline", action="store_true", help="Generate baseline metrics")
    args = parser.parse_args()

    # --- Configuration ---
    REQUIRED_COLUMNS = ['order_id', 'customer_id', 'order_ts', 'net_amount']
    METRICS_FILE = "metrics/baseline_metrics.json"

    # --- Load Data ---
    try:
        df = pd.read_csv(args.datafile)
    except FileNotFoundError:
        print(f"Error: Data file not found at {args.datafile}")
        sys.exit(1)

    # --- Baseline Mode ---
    if args.baseline:
        if not check_required_columns(df, REQUIRED_COLUMNS):
            sys.exit(1)

        # Ensure the metrics directory exists
        metrics_dir = os.path.dirname(METRICS_FILE)
        os.makedirs(metrics_dir, exist_ok=True)
        
        # Save baseline metrics
        baseline_metrics = {"net_amount_mean": df["net_amount"].mean()}
        with open(METRICS_FILE, "w") as f:
            json.dump(baseline_metrics, f)
        print(f"✅ Baseline metrics saved to {METRICS_FILE}")
        sys.exit(0)

    # --- Validation Mode ---
    # 1. Manual Column Check (Initial Drift Detection)
    if not check_required_columns(df, REQUIRED_COLUMNS):
        sys.exit(1)

    # 2. OPA Policy Check (Guard)
    if args.policy:
        data_for_opa = {
            "columns": list(df.columns),
            "psi": {"net_amount": 0.0} # Placeholder for PSI check
        }
        # Load baseline for PSI calculation
        try:
            with open(METRICS_FILE, "r") as f:
                baseline_metrics = json.load(f)
            # Create a dummy baseline series for PSI calc
            baseline_series = np.random.normal(baseline_metrics['net_amount_mean'], 20, len(df))
            psi_value = calculate_psi(baseline_series, df['net_amount'])
            data_for_opa["psi"]["net_amount"] = psi_value
        except FileNotFoundError:
            print("Warning: Baseline metrics not found. Skipping PSI check.")
        
        if not run_opa_policy(data_for_opa, args.policy):
            sys.exit(1)
    
    print("✅ All data validation checks passed.")

if __name__ == "__main__":
    main()