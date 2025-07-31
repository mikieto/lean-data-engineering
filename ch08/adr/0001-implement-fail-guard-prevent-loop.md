# ADR-CH08-001: Implement a "Fail-Guard-Prevent" Loop for Data Quality

## Context

**The Problem:** Our `retail_orders` data pipeline is vulnerable to upstream data quality issues. Two recent incidents have caused data corruption downstream: 1) a required `customer_id` column was suddenly dropped, and 2) the `net_amount` column was unexpectedly scaled (e.g., from dollars to cents), breaking financial reports. These failures are detected late, requiring manual intervention and eroding trust in the data.

**The Goal:** We need an automated, resilient way to handle such data drifts. Instead of just fixing the immediate issue, we want to build a system that learns from these failures and automatically prevents them from recurring. This hands-on lab will implement a minimal, tangible version of the **Intellectual Immune System**.

## Decision

We will implement a data pipeline validation system that demonstrates a complete "Fail -> Guard -> Prevent" loop using a `Makefile` interface.

The workflow will be as follows:
1.  **Baseline:** First, run the pipeline against a valid dataset to confirm it passes (`make baseline`).
2.  **Fail (Drift):** Intentionally introduce a dataset with known quality issues (the "drift") and run the pipeline to demonstrate its failure (`make drift`). The system must detect the anomaly and deny the process.
3.  **Guard (Fix):** Implement a "guard" – a declarative data quality rule (using OPA/Rego) that specifically targets the drift pattern.
4.  **Prevent (Run):** Re-run the pipeline against the faulty dataset. The newly implemented guard should catch the error, and the process should fail gracefully with a clear explanation, thus preventing the bad data from propagating.

## Rationale

This approach was chosen because it provides the most direct and tangible way for a user to experience the core concept of the **Intellectual Immune System**.

-   **Experiential Learning:** By manually running `make drift` and `make fix`, the user actively participates in the learning loop, which is more effective than passively reading about it.
-   **Simplicity and Focus:** It uses a minimal set of tools (Make, Python, Rego) to focus purely on the "fail-guard-prevent" mechanism without the complexity of a full-scale distributed system.
-   **Reproducibility:** This workflow is fully self-contained and can be run locally or in a Codespaces environment, guaranteeing a consistent learning experience for all readers.

## Acceptance Criteria

-   `make baseline` must complete successfully (exit code 0).
-   `make drift` must fail (non-zero exit code) and the log must clearly state the reason for failure (e.g., "Required column 'customer_id' is missing").
-   After running `make fix`, a `guards/policies.rego` file must be created or updated with a new policy.
-   Running `make run` after the fix must also fail, but this time, the log must indicate that the `policy` explicitly denied the invalid data.
