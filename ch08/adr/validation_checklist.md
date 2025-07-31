# Validation Checklist for Chapter 8 Hands-on

This checklist is used to manually verify that the hands-on lab for Chapter 8 has been implemented correctly according to the ADR.

## Instructions
Run the `make` commands in the specified order and check if the result matches the "Expected Outcome".

---

### Baseline Run Verification

-   [ ] **Command**: `make baseline`
-   [ ] **Expected Outcome**: The command completes successfully with an exit code of 0. No errors are reported in the log.

### Drift Detection Verification

-   [ ] **Command**: `make drift`
-   [ ] **Expected Outcome**: The command **fails** with a non-zero exit code. The log output must contain a clear error message indicating the reason for the failure (e.g., "Required column 'customer_id' is missing" or a data validation error).

### Guard Implementation Verification

-   [ ] **Action**: Run `make fix`.
-   [ ] **Expected Outcome**: The command completes successfully. A file named `guards/policies.rego` should now exist and contain a new policy rule designed to catch the drift.

### Prevention Verification

-   [ ] **Action**: Run `make run` (executed *after* `make fix`).
-   [ ] **Expected Outcome**: The command **fails** again with a non-zero exit code. Crucially, the log output must now indicate that the failure was caused by the **OPA policy** explicitly denying the data. This confirms the "guard" is working as intended.
