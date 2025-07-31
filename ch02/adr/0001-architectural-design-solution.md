# ADR-CH02-001: Architectural Design for the Retail Orders Data Pipeline (Solution)

## Context

**The Problem:** The "Retail-X" company needs to build a new data pipeline to process `retail_orders` data. However, there are multiple competing architectural patterns (e.g., Lakehouse, Data Mesh), and the team lacks a clear, rational basis for choosing the best approach for their specific needs. Simply picking a popular technology without clear justification leads to technical debt and stakeholder misalignment.

**The Goal:** To use a structured, governable process to design a data pipeline architecture. The design must be explicitly linked to business requirements and technical constraints, ensuring the decision is defensible, auditable, and serves as a clear blueprint for implementation. This lab simulates the role of an AI Collaboration Architect (ACA) in leading this design process.

## Decision

We will adopt a modern **Lakehouse architecture** for the `retail_orders` data pipeline. This architecture will utilize cloud storage (like S3) for the raw `Records` layer and a structured query engine (like Snowflake or Databricks) for the `Knowledge` and `Principles` layers.

## Rationale

The Lakehouse architecture was chosen over a decentralized Data Mesh for this specific scenario due to the following reasons:
-   **Simplicity & Speed:** For a single, well-defined data source like `retail_orders`, a centralized Lakehouse provides the fastest path to value with less operational overhead.
-   **Maturity of Tooling:** The tooling around Lakehouse patterns is mature and widely adopted, reducing implementation risk for the team.
-   **Alignment with Goals:** It directly supports the goal of creating a governable, auditable data blueprint, which is the core of our 3-Tier model. A Data Mesh would introduce unnecessary complexity at this stage.

---
## Logical Schema Definition

- **Table Name**: `retail_orders`
- **Description**: Contains raw order data ingested from the e-commerce platform. This schema serves as the data contract for the Records layer.
- **Columns**:
    - `order_id`: STRING, NOT NULL, PRIMARY KEY
    - `customer_id`: STRING, NOT NULL
    - `order_ts`: TIMESTAMP, NOT NULL
    - `net_amount`: DECIMAL(10, 2), NOT NULL
- **Data Quality Constraints**:
    - `net_amount` must be a positive value.
    - `order_ts` must be a valid ISO 8601 timestamp format.

## Acceptance Criteria

-   The final ADR must clearly state the chosen architectural pattern in the **Decision** section.
-   The **Rationale** section must explain *why* the chosen pattern is superior to the alternatives for this specific scenario.
-   The ADR must contain a complete **Logical Schema Definition** for the `retail_orders` table, including data types and quality constraints for each column, which will serve as the input for the Chapter 4 hands-on.