# Chapter 2 Hands-on Lab: AI-Powered Data Architecture Design

Welcome to the Chapter 2 Hands-on Lab\! This lab guides you through the practical steps of using the **ADR-centric AI Collaboration Workflow** to design and implement a modern data architecture. For the concepts and philosophy behind this workflow, please refer to the "Putting Theory into Practice" section in Chapter 2 of the book.

## Get Started Instantly with GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/mikieto/lean-data-engineering)

**Click the badge above to launch a pre-configured development environment.** This will set up all necessary tools automatically.

### **Required Setup: AWS Credentials**

To allow Terraform to create resources, you must configure your AWS credentials as Codespaces secrets.

1.  **Get Credentials**: Create a dedicated IAM user in your AWS account with minimal necessary permissions. Generate an Access Key ID and a Secret Access Key. **Do not use root credentials.**
2.  **Add Secrets**: In your forked repository, go to `Settings` \> `Codespaces secrets` and add the following three secrets:
      * `AWS_ACCESS_KEY_ID`
      * `AWS_SECRET_ACCESS_KEY`
      * `AWS_DEFAULT_REGION` (e.g., `us-east-1`)
3.  **Rebuild Codespace**: If your Codespace is running, rebuild it (`Ctrl+Shift+P` \> `Dev Containers: Rebuild Container`) to apply the secrets.

-----

## Lab Scenario

You are the CTO of a mid-sized e-commerce company. Your central Data Lakehouse is successful but has become a bottleneck. You need to scale your data platform to **accelerate domain-driven innovation**.

## Lab Steps: Your AI Collaboration Workflow

### **Step 1: Formalize Your Intent in an ADR**

Your first step is to use AI to help formalize your strategic decision in an Architecture Decision Record (ADR).

1.  **Instruct AI to generate an ADR template**:

      * **You (to AI)**: "Based on the goal to 'accelerate domain-driven innovation' for a data platform, provide a template for an Architecture Decision Record (ADR) that includes sections for context, decision, alternatives, and rationale."

2.  **Collaborate with AI to populate the ADR**:

      * Use the provided example `adr/0001-data-platform-scaling-strategy.md` as a reference.
      * Work with your AI to fill out each section, defining the context, your chosen decision (e.g., "Phased Data Mesh"), and why you rejected the alternatives.

### **Step 2: Generate Code from the ADR**

With the ADR finalized, use it as a precise specification for code generation.

1.  **Copy the content of your final ADR**.
2.  **Provide it to the AI with a clear instruction**:
      * **You (to AI)**: "Based on the following Architecture Decision Record, generate a high-level Infrastructure as Code (IaC) for a pilot Data Mesh implementation using AWS and Terraform, focusing on initial domain data product buckets and a simplified data contract policy."
      * **(Paste your ADR content here)**

### **Step 3: Review and Validate the Output**

Review the AI-generated code against your ADR.

1.  **Strategic Review**: Does the generated code (`main.tf`, `data_definitions.yaml`) accurately reflect the decision and rationale in your ADR?
2.  **Technical Validation**: Use the provided `Makefile` to run basic checks in your Codespaces terminal.
      * `cd chapter02`
      * `make validate` (Validates Terraform syntax)
      * `make security-check` (Runs basic security scan with `tfsec`)

### **Step 4 (Optional): Iterate and Refine**

If you find discrepancies, provide specific, corrective feedback to the AI, referencing your ADR.

  * **You (to AI)**: "The ADR requires a tagging policy for 'cost-center'. Please add this to the S3 bucket resources in the Terraform code."

-----

## Hands-on Files

  * `adr/0001-data-platform-scaling-strategy.md`: The example ADR to guide your work.
  * `main.tf`, `data_definitions.yaml`: Example solution files. Your AI's output may differ. Focus on the process.
  * `Makefile`: Contains shortcuts for validation and Terraform commands (`init`, `plan`, `apply`, `destroy`).
  * `prompts/`: Contains more advanced, structured YAML prompts you can experiment with.