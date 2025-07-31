.PHONY: baseline drift fix run demo clean

# Define the python script path
VALIDATE_SCRIPT = scripts/validate.py

# Default target
all: demo

# Run validation against good data
baseline:
	@echo "🧪 Running baseline validation with good data..."
	@python3 $(VALIDATE_SCRIPT) --datafile data/orders_good.csv --baseline
	@echo "✅ Baseline validation successful."

# Run validation against bad data (drift) to show initial failure
drift:
	@echo "💥 Simulating data drift with bad data..."
	@! python3 $(VALIDATE_SCRIPT) --datafile data/orders_bad.csv
	@echo "✅ Drift detected as expected."

# Apply the fix (the guard policy)
fix:
	@echo "🛡️ Applying the guard (Policy-as-Code)..."
	@cp guards/policies.rego.solution guards/policies.rego
	@echo "✅ Guard is now in place."

# Re-run validation against bad data to show the guard works
run:
	@echo "🔬 Re-running validation with the guard in place..."
	@! python3 $(VALIDATE_SCRIPT) --datafile data/orders_bad.csv --policy guards/policies.rego
	@echo "✅ Guard successfully prevented the drift."

# A full demonstration sequence
demo: clean baseline drift fix run
	@echo "🎉 Demo complete!"

# Clean up generated files
clean:
	@echo "🧹 Cleaning up generated files..."
	@rm -f guards/policies.rego
	@rm -f metrics/baseline_metrics.json