.PHONY: init plan apply destroy validate validate-yaml security-check cost-estimate validate-data clean

# --- Configuration Variables ---
AWS_REGION ?= us-east-1 # Default AWS region. Override with: make apply AWS_REGION=ap-northeast-1
TERRAFORM_DIR := .

# --- Terraform Commands ---

# Initialize Terraform (e.g., download providers)
init:
	@echo "Initializing Terraform..."
	terraform -chdir=$(TERRAFORM_DIR) init

# Generate an execution plan
plan: init
	@echo "Generating Terraform plan..."
	terraform -chdir=$(TERRAFORM_DIR) plan

# Apply the Terraform configuration (creates/updates resources)
apply: plan
	@echo "Applying Terraform configuration..."
	# WARNING: -auto-approve is used for lab convenience. Do not use this in production environments without careful review.
	terraform -chdir=$(TERRAFORM_DIR) apply -auto-approve

# Destroy the created Terraform resources
destroy:
	@echo "Destroying Terraform resources..."
	# WARNING: This will permanently delete all resources created by this Terraform configuration.
	terraform -chdir=$(TERRAFORM_DIR) destroy -auto-approve

# Validate the Terraform configuration syntax
validate: init
	@echo "Validating Terraform configuration..."
	terraform -chdir=$(TERRAFORM_DIR) validate

# --- Security & Compliance Checks ---
# Requires tfsec and checkov to be installed in the environment (e.g., via .devcontainer)
security-check:
	@echo "Running security checks with tfsec..."
	tfsec $(TERRAFORM_DIR) || true # '|| true' to not fail the make target if issues are found, just report
	@echo "Running compliance checks with checkov..."
	checkov -d $(TERRAFORM_DIR) --framework terraform --quiet || true

# --- Cost Estimation ---
# Requires infracost CLI to be installed and configured
cost-estimate: init
	@echo "Estimating infrastructure costs..."
	infracost breakdown --path=$(TERRAFORM_DIR) --format=json > infracost_report.json
	@echo "Cost estimate saved to infracost_report.json. Review before 'make apply'."

# --- Data Definition & Quality Validation ---

# Validate the data_definitions.yaml (requires 'yamllint' to be installed)
validate-yaml:
	@echo "Validating data_definitions.yaml..."
	@if [ -f data_definitions.yaml ]; then \
		python3 -m yamllint data_definitions.yaml; \
	else \
		echo "data_definitions.yaml not found."; \
	fi

# Placeholder for more comprehensive data quality tests (e.g., Great Expectations, dbt tests)
validate-data:
	@echo "Running data quality validation checks..."
	# This is a placeholder. Implement actual data quality tests here.
	# Example: great_expectations checkpoint run my_checkpoint
	# Example: dbt test --select +my_model
	echo "Consider using Great Expectations or dbt tests here for comprehensive data validation."

# --- Cleanup ---

# Remove Terraform state files, cache, and infracost report
clean:
	@echo "Cleaning up local development files..."
	rm -rf $(TERRAFORM_DIR)/.terraform
	rm -f $(TERRAFORM_DIR)/.terraform.lock.hcl
	rm -f $(TERRAFORM_DIR)/terraform.tfstate*
	rm -f infracost_report.json
	@echo "Cleanup complete."
