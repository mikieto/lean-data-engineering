# Chapter 2 Hands-on Lab: AI-Powered Data Architecture Design

Welcome to the Chapter 2 Hands-on Lab! This lab is your practical guide to becoming an **AI Collaboration Architect (ACA)**, using a powerful, repeatable methodology to design modern data architectures.

## Why This Lab Matters: Bridging Intent and Implementation

As a data leader, you define the strategic "Why"—the purpose and value—of your data initiatives. But how do you translate that "Why" into concrete architectural "Hows" and "Whats" that AI can understand and build? And how do you ensure AI-generated solutions truly align with your intent and governance standards?

This lab introduces you to an **ADR-centric AI Collaboration Workflow**. Here, an Architecture Decision Record (ADR) becomes your definitive design specification, ensuring:

1.  **Clear Intent (Why/What)**: Your strategic decisions are meticulously captured, serving as the ultimate "North Star" for AI.
2.  **AI-Driven Implementation (How)**: AI generates infrastructure as code (IaC) and data definitions based directly on your ADR.
3.  **Verifiable Outcomes**: You review AI-generated code against the precise requirements defined in your ADR, ensuring alignment with your governance model.

By mastering this workflow, you will not only accelerate your data projects but also build a transparent, auditable, and continuously improving data architecture.

### AI Collaboration Workflow Flow

```{mermaid}
%%| label: fig-adr-workflow
%%| fig-cap: "AI Collaboration Workflow: ADR as the central artifact."
graph TD
    subgraph Human Role
        H_DefineWhy[Define Strategic Why]
        H_ReviewADR[Review/Refine ADR]
        H_ReviewCode[Review AI-Generated Code against ADR]
        H_Iterate[Iterate/Provide Feedback]
        H_End[End: Implemented Architecture]
    end

    subgraph AI Role
        AI_GenADRTemp[Generate ADR Template]
        AI_GenCode[Generate Code from ADR]
        AI_Refine[Refine Code]
    end

    H_DefineWhy --> AI_GenADRTemp
    AI_GenADRTemp --> H_ReviewADR
    H_ReviewADR -- Approved ADR --> AI_GenCode
    AI_GenCode --> H_ReviewCode
    H_ReviewCode -- Discrepancies/Refinement --> H_Iterate
    H_Iterate --> AI_Refine
    AI_Refine --> H_ReviewCode
    H_ReviewCode -- Approved Code --> H_End

    style H_DefineWhy fill:#FFFDE7,stroke:#F57F17
    style H_ReviewADR fill:#FFFDE7,stroke:#F57F17
    style H_ReviewCode fill:#FFFDE7,stroke:#F57F17
    style H_Iterate fill:#FFFDE7,stroke:#F57F17
    style AI_GenADRTemp fill:#E3F2FD,stroke:#1E88E5
    style AI_GenCode fill:#E3F2FD,stroke:#1E88E5
    style AI_Refine fill:#E3F2FD,stroke:#1E88E5
    style H_End fill:#E8F5E9,stroke:#388E3C
````

## Get Started Instantly with GitHub Codespaces

[](https://www.google.com/search?q=https://codespaces.new/mikieto/lean-data-engineering)

**Click the badge above to launch a pre-configured development environment in GitHub Codespaces.** This will set up all necessary tools and dependencies automatically, so you can jump straight into the lab exercises without any local setup.

### Codespaces AWS Credentials Setup

To allow Terraform to create AWS resources within your Codespaces environment, you need to provide your AWS credentials as GitHub Codespaces secrets.

1.  **Prepare AWS Credentials**:

      * Log in to your AWS Management Console.
      * **Highly Recommended**: Create a dedicated IAM user for this lab with **minimal necessary permissions** (e.g., S3 bucket creation/deletion, Glue database/table creation/deletion, S3 bucket policy management).
      * Generate an Access Key ID and a Secret Access Key for this IAM user. **DO NOT use your root account credentials or credentials with excessive permissions.**

2.  **Add Secrets to Your GitHub Repository**:

      * Navigate to your forked GitHub repository in your web browser.
      * Go to **`Settings`** > **`Codespaces`** > **`Repository secrets`** (or `Codespaces secrets`).
      * Add the following three secrets:
          * `AWS_ACCESS_KEY_ID`: Your IAM user's Access Key ID.
          * `AWS_SECRET_ACCESS_KEY`: Your IAM user's Secret Access Key.
          * `AWS_DEFAULT_REGION`: The AWS region you wish to use (e.g., `us-east-1` or `ap-northeast-1`). This will override the default in the Makefile.
      * **Security Note**: These secrets are securely passed as environment variables to your Codespaces container. Never commit your credentials directly into your repository.

3.  **Rebuild Codespace**: If your Codespace is already running, you will need to rebuild it to pick up the new secrets. In VS Code, open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select `Dev Containers: Rebuild Container`.

-----

## Lab Scenario

You are the CTO of a mid-sized e-commerce company. You have successfully built a central Data Lakehouse for your marketing team. Now, your Product and Logistics teams are eager to build their own data products, but your central team is overwhelmed. You need a strategy to scale your data platform.

-----

## Your AI Collaboration Workflow: ADR as the Core

This workflow guides you through the process of defining your architectural decisions in an ADR, leveraging AI for code generation, and verifying the output.

### 1. Repository File Structure for this Lab

This `chapter02/` directory contains the following key files:

  * `README.md` (this file): Guides you through the lab steps.
  * `main.tf`: The Terraform Infrastructure as Code (IaC) example.
  * `data_definitions.yaml`: Defines the schema and quality rules for a **Silver layer data product** in a Medallion architecture. It specifies the layout of clean, conformed data ready for business use, not the raw source data (Bronze layer).
  * `Makefile`: Simplifies running Terraform and validation commands.
  * `adr/`: Subdirectory containing Architecture Decision Records (ADRs).
      * `adr/0001-data-platform-scaling-strategy.md`: An example ADR that captures the decision for this lab's scenario.

### Step 1: Pin the 'Why' (Intent Conveyance & ADR Initiation)

In this step, you will clearly communicate your overarching "Why" to the AI and begin to formalize it within an ADR template. This sets the strategic direction.

1.  **Initiate the dialogue with AI**: Start by stating your core challenge and the "Why" for scaling your platform.

      * **You (to AI)**: "We need to scale our data platform. Our central Lakehouse is successful, but it's becoming a bottleneck."
      * **AI (expected response)**: "Understood. To recommend the best path, it is crucial to clarify the primary business driver. Is the priority (A) Speed and Autonomy for the new teams, or (B) maintaining Centralized Control and Consistency?"
      * **You (to AI)**: "The priority is (A) Speed and Autonomy. Our 'Why' is to **accelerate domain-driven innovation**."

2.  **Generate an ADR Template with AI**: Now, instruct AI to provide a template for formalizing this decision.

      * **You (to AI)**: "Based on this 'Why', provide a template for an Architecture Decision Record (ADR) to capture this scaling strategy, including sections for context, decision, alternatives, and rationale."
      * **AI (expected response - *template example, actual AI output may vary*)**:
        ```markdown
        # Architecture Decision Record: [Decision Title]

        ## 1. Context
        [Describe the problem that is driving this decision. What is the current state? What challenges are we facing?]

        ## 2. Decision
        [State the chosen architectural decision clearly and concisely.]

        ## 3. Alternatives Considered
        [List the alternative solutions that were evaluated. Why were they not chosen? Refer back to your 'Why'.]

        ## 4. Rationale
        [Explain in detail why the chosen decision is the best fit for the context, referencing the 'Why' and the Four-Tier Governance Model principles.]

        ## 5. Consequences
        [Describe the positive and negative impacts of this decision. What are the known trade-offs?]

        ## 6. Status
        [Proposed / Approved / Implemented / Deprecated]

        ## 7. Date
        [YYYY-MM-DD]
        ```

3.  **Populate the ADR (Collaborate with AI)**: Fill in the ADR template using the dialogue from Step 1 and your strategic choice. You can ask AI to draft sections based on your inputs.

      * **You (to AI)**: "Draft the 'Context' section of the ADR for our scaling problem."
      * **You (to AI)**: "Now, based on 'accelerate domain-driven innovation', suggest three architectural alternatives for the 'Alternatives Considered' section." (Referencing the book's examples: Phased Data Mesh, Independent Lakehouses, Hub-and-Spoke Model)

### Step 2: Unleash the 'How' (ADR-Driven Code Generation)

With your ADR defining the "What" (the specific architectural decision and its requirements), instruct AI to generate the corresponding "How" (the concrete implementation code).

1.  **Access and Provide the ADR to AI for code generation**:
      * **Open the example ADR**: In your Codespaces environment, navigate to the `adr/` directory within `chapter02/` and open `0001-data-platform-scaling-strategy.md`.
      * **Copy the content**: Copy the entire content of this ADR file.
      * **Provide to AI**: Paste the copied ADR content to your LLM and instruct it to generate code.
          * **You (to AI)**: "Based on the following Architecture Decision Record, generate a high-level Infrastructure as Code (IaC) for a pilot Data Mesh implementation using AWS, focusing on setting up initial domain data product buckets and a simplified data contract policy. Assume a Lakehouse foundation."
          * **(Paste ADR content here)**:
            ```markdown
            # Architecture Decision Record: Data Platform Scaling Strategy

            ## 1. Context
            Our central Data Lakehouse for the marketing team is successful but has become a bottleneck for new product and logistics data initiatives. We need to scale our data platform to support these new teams efficiently.

            ## 2. Decision
            Implement a **Phased Data Mesh** approach, starting with pilot domains for Product and Logistics. This will involve decentralizing data ownership to business domains, treating data as a product, and federating governance.

            ## 3. Alternatives Considered
            - **The Independent Lakehouses**: Rejected due to potential for data silos and inconsistent governance across domains.
            - **The Hub-and-Spoke Model**: Rejected as it maintains a central bottleneck, which contradicts our "Speed and Autonomy" priority.

            ## 4. Rationale
            The Phased Data Mesh aligns with our primary goal to "accelerate domain-driven innovation." It empowers domain teams with autonomy while establishing federated governance (L3: Legislation) to maintain overall consistency, leveraging our existing Lakehouse foundation (L1/L2). This balances agility with control.

            ## 5. Consequences
            - **Positive**: Increased innovation speed, improved data ownership, reduced central team bottleneck.
            - **Negative**: Requires significant cultural shift, initial investment in platform tooling, potential for new silos if governance is not properly implemented.

            ## 6. Status: Approved
            ## 7. Date: 2025-07-22
            ```
      * **AI (expected response)**: AI will generate IaC code (similar to `main.tf` and `data_definitions.yaml` in this folder).

### Step 3: Iterate to 'Wow' (ADR-Driven Review & Refinement)

Now, your role as an ACA is critical. Review the AI-generated code against your ADR, ensuring it precisely meets your defined requirements and strategic intent.

1.  **Review AI-generated code against ADR**:

      * Open `main.tf` and `data_definitions.yaml` in this `chapter02/` folder.
      * Compare the generated code with your ADR's "Decision," "Rationale," and "Consequences" sections.
      * **Check for alignment**: Does the code reflect the chosen Data Mesh strategy? Are the resources logically separated by domain? Are the initial data product definitions reasonable?
      * **Check for governance adherence**: Does the code reflect any L3 (Legislation) requirements from your ADR (e.g., tagging for governance, placeholders for access policies)?

2.  **Validate Code Syntax and Style**: Use the provided `Makefile` to perform basic validation.

      * Open the terminal in Codespaces (`Terminal > New Terminal`).
      * Navigate to the `chapter02/` directory: `cd chapter02/`
      * **Validate Terraform syntax**:
        ```bash
        make validate
        ```
      * **Validate YAML syntax (if `yamllint` is installed in Codespaces)**:
        ```bash
        make validate-yaml
        ```
      * **Reflect**: These checks ensure basic technical correctness, but human review against the ADR ensures strategic alignment.

3.  **Iterate and Refine (Optional)**: If you find discrepancies or areas for improvement, provide specific feedback to the AI, referencing the ADR.

      * **You (to AI)**: "The generated `main.tf` looks good, but the data product's S3 bucket policy doesn't explicitly include encryption at rest as per our L3 legislation 'PII_Encryption_Policy' in my ADR. Please update the policy to enforce server-side encryption for the Marketing Data Product bucket."
      * **AI**: The AI will then generate a refined version.

-----

## Sample Prompt for AI Interaction (Customer 360-degree View)

Below is a sample YAML prompt template you can use to communicate complex architectural intent to your LLM. This structured format helps the AI generate more precise and aligned outputs.

<details>
<summary>Click to Copy Sample YAML Prompt for AI</summary>

```yaml
# customer-360-view-prompt.yaml (Example from Chapter 2)
initiative_id: "customer-360-view"
date: "2025-07-18"
project_purpose: # Overarching goal and values for this initiative (L4: Constitution)
  mission_statement: |
    To dramatically enhance customer experience and provide personalized services,
    aiming to increase customer loyalty by 25% and revenue by 15%.
  core_principles:
    - "Transparency in data usage and customer privacy are top priorities."
    - "All customer-facing decisions must be explainable."

governance_layers: # Explicitly define each layer of the Four-Tier Governance Model
  - layer_id: "L4"
    name: "Constitution"
    description: "Guiding Principles & Values for the 'Customer 360-Degree View' initiative."
    elements:
      - type: "principle"
        id: "customer_loyalty_goal"
        value: "Increase customer loyalty by 25% and revenue by 15% through personalized services."
      - type: "value"
        id: "privacy_transparency"
        value: "Transparency in data usage and customer privacy are top priorities."

  - layer_id: "L3"
    name: "Legislation"
    description: "Machine-readable Rules and Policies for this Initiative."
    elements:
      - type: "policy"
        id: "PII_Encryption_Policy"
        description: "All Personally Identifiable Information (PII) must be encrypted when transitioning from L1 to L2."
        impact_layer: "L3 (Legislation)"
      - type: "policy"
        id: "Data_Quality_SLA_Customer_Master"
        description: "Customer master data must maintain 99.9% accuracy with monthly quality checks."
        impact_layer: "L3 (Legislation)"
      - type: "policy"
        id: "Access_Control_Marketing_Team"
        description: "Marketing team is allowed access only to aggregated and anonymized customer behavior data."
        impact_layer: "L3 (Legislation)"

  - layer_id: "L2"
    name: "Knowledge"
    description: "Expected Knowledge Structure for the Customer 360-Degree View."
    elements:
      - type: "knowledge_asset"
        id: "Customer_Master_Knowledge_Graph"
        description: |
          Build an integrated customer master data knowledge graph (L2).
          Includes customer ID, attributes, historical interaction logs, and aggregated behavior patterns.
        source_from_layer: "L1 (Logs) & External"
        expected_consumers: ["AI Personalization Engine", "Marketing Analytics"]
        impact_layer: "L2 (Knowledge)"

  - layer_id: "L1"
    name: "Logs"
    description: "Source Data Definition (Immutable Records)."
    elements:
      - type: "data_source"
        id: "Website_Clickstream_Logs"
        description: |
          Raw clickstream data from the website (L1).
          Includes timestamp, user_id, event_type, page_id, session_id.
        location: "s3://raw-logs/website/"
        immutability_requirement: "Must maintain full change history and be tamper-proof."
        impact_layer: "L1 (Logs)"

ai_task_instruction: |
  Based on the requirements for each governance layer defined above (from L1 data to L4 objectives),
  propose optimal data architecture designs for building a "Customer 360-degree View",
  including combinations of specific physical implementations for each layer (e.g., Lakehouse, Data Vault, Vector DB).
  Emphasize the data linkage path to the AI personalization engine.
```

</details>

-----

## Example Solution Code & Definitions

The `main.tf` and `data_definitions.yaml` files in this `chapter02/` directory are examples of the kind of IaC and data definition files that an AI might generate in response to the ADR-driven prompts. These files are not merely a raw output from an AI; they represent the **refined outcome of AI collaboration**. They were generated based on an AI's proposal, followed by human review, strategic refinement, and final approval—the exact workflow you are learning in this lab.

**Note on AI-Generated Code:**

  * Your actual LLM's output may vary significantly.
  * Focus on understanding the *structure* and *logic* of the generated code, and how it addresses the requirements defined in your ADR. Your role as an ACA is to evaluate, refine, and iterate on these AI-generated solutions.

You can explore `main.tf` and `data_definitions.yaml` now to see an example of what your AI partner can help you create!

-----

## Running the Example Code with Makefile

The `Makefile` simplifies interaction with the Terraform configuration.

1.  **Initialize the Terraform project**:
    ```bash
    make init
    ```
2.  **Review the planned changes**:
    ```bash
    make plan
    ```
3.  **Apply the configuration (creates AWS resources)**:
    ```bash
    make apply
    ```
    *Note: This command will attempt to create actual AWS resources. Ensure you have AWS credentials configured in your Codespaces environment (if applicable) and understand potential costs. For learning purposes, you might just run `make plan`.*
4.  **Validate data definitions (requires `yamllint` installed)**:
    ```bash
    make validate-yaml
    ```
5.  **Destroy resources after completion**:
    ```bash
    make destroy
    ```
    *Always remember to destroy resources to avoid unexpected charges.*
6.  **Clean up local Terraform files**:
    ```bash
    make clean
    ```

-----

## Verifying and Refining AI-Generated Code (Advanced Tips)

Beyond basic syntax checks, ensuring your AI-generated code meets production standards requires a multi-faceted approach. These tips enhance the "Iterate to 'Wow'" step, helping you become a more effective ACA.

### 1. Security and Compliance Checks (Shift Left)

Automating security and compliance scans early in the development lifecycle is crucial for cloud-native deployments.

  * **Implement Static Analysis**: Integrate tools like `tfsec` or `checkov` into your workflow. These scan your IaC for potential security misconfigurations.
      * **Add to Makefile**:
        ```makefile
        # Add to chapter02/Makefile
        .PHONY: security-check
        security-check:
        	@echo "Running security checks with tfsec..."
        	tfsec . || true # '|| true' to not fail the make target if issues are found, just report
        	@echo "Running compliance checks with checkov..."
        	checkov -d . --framework terraform --quiet || true
        ```
      * **Run the check**: `make security-check` (You may need to add `tfsec` and `checkov` installation to your `.devcontainer/devcontainer.json`'s `postCreateCommand` or `features`).

### 2. Infrastructure and Data Quality Testing

IaC needs testing just like application code. This ensures your infrastructure behaves as expected and your data meets quality standards.

  * **Infrastructure Testing (Integration/E2E)**: For more robust testing, consider frameworks like `Terratest` (Go-based). While beyond this lab's scope, it validates deployed infrastructure.
  * **Data Quality Validation**: Ensure the data processed by your architecture is reliable.
      * **Integrate a Data Quality Framework**: Tools like `Great Expectations` or `dbt tests` (if using dbt) can validate data definitions against actual data.
      * **Add to Makefile (example for `Great Expectations` skeleton)**:
        ```makefile
        # Add to chapter02/Makefile
        .PHONY: validate-data
        validate-data:
        	@echo "Running data quality validation checks..."
        	# Assuming 'great_expectations init' and 'great_expectations checkpoint run'
        	# is configured. This is a placeholder for actual data quality test execution.
        	echo "Placeholder for data quality tests against data_definitions.yaml."
        	echo "Consider using Great Expectations or dbt tests here."
        ```
      * **Run the check**: `make validate-data`

### 3. Cost Guardrails and Rollback Procedures

Managing cloud costs and having clear rollback plans are essential for production readiness.

  * **Estimate Costs with `infracost`**: Before applying IaC, get a cost estimate.
      * **Integrate `infracost`**: (Requires `infracost` CLI setup in Codespaces).
        ```makefile
        # Add to chapter02/Makefile
        .PHONY: cost-estimate
        cost-estimate: init
        	@echo "Estimating infrastructure costs..."
        	infracost breakdown --path=$(TERRAFORM_DIR) --format=json > infracost_report.json
        	@echo "Cost estimate saved to infracost_report.json. Review before 'make apply'."
        ```
      * **Run the estimate**: `make cost-estimate`
  * **Plan Rollbacks**: Always have a strategy for reverting to a known good state. Terraform's state management helps, but manual steps or custom scripts may be needed for complex changes. Define this in your ADR's "Consequences" section.
  * **Cloud Account Management**: Ensure you are using a dedicated development/sandbox AWS account for these labs to prevent unexpected charges or impact on production. Confirm your AWS region (`AWS_REGION` variable in Makefile) aligns with free tier availability if applicable.

### 4. Exploring Advanced Concepts (Optional)

Dive deeper into specific architectural patterns and their application.

  * **Vector Database and RAG Integration**: Chapter 2 highlights Vector DBs as a key extension to the Knowledge layer.
      * **Explore `chapter02/examples/rag_demo/`**: This subdirectory contains a minimal example demonstrating how to integrate a Vector Database (e.g., using `langchain` with a local vector store or a service like Pinecone) for Retrieval Augmented Generation (RAG).
      * **Navigate**: `cd chapter02/examples/rag_demo/` to explore the Python script and `README.md` within that folder.

-----

## Practical Tips for Your Workflow

These tips enhance your collaboration with AI and improve your overall development efficiency as an ACA.

  * **Review AI Output Locally First**: Before adding AI-generated code to Git (e.g., `git add .`), always review it thoroughly in your local editor. Ensure it meets your standards, is strategically aligned, and has no unexpected elements.
  * **Document Iterations with Difference Logs**: For complex iterations, consider creating short "AI_DIFF.md" files or adding concise notes to your `task_log` or `decision_log` summarizing "AI proposal ⇄ Human review and refinement" cycles. This helps trace decision evolution.
  * **Define Tagging Conventions in ADR**: Explicitly define resource tagging rules (e.g., `project=chapter02`, `domain=logistics`, `env=dev`) in your ADR (or L3: Legislation section of a YAML prompt). Then, instruct AI to apply these tags to generated resources. This directly supports your governance strategy.
  * **Sign Your Commits**: Use signed commits (`git commit -S -m "..."`) to cryptographically verify who approved the change. This enhances auditability and trust in a collaborative, AI-assisted workflow.
