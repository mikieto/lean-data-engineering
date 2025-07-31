# Chapter 8 Hands-on: Building an Intellectual Immune System

## Your Mission in this Lab

In this chapter, you learned the core principles for building an **Intellectual Immune System** that learns from failures. Now, it's time to put that theory into practice.

Your mission in this hands-on lab is to experience the `fail -> guard -> prevent` learning loop firsthand. You will step into the role of a data engineer, using a `Makefile` to simulate a critical data drift scenario in a `retail_orders` pipeline. Then, with the help of your AI partner, you will implement and verify a "guard" that makes your system immune to that specific failure.

---
## The Scenario

You are a data engineer responsible for the `retail_orders` data pipeline. Recently, the pipeline has been failing due to unexpected upstream data quality issues, such as missing columns and incorrect data scales. Your goal is not just to fix the immediate problem but to build a resilient system that automatically learns from these failures to prevent them in the future.

This lab simulates that experience. You will intentionally trigger a failure, implement a "guard" to catch it, and verify that the system is now "immune" to that specific failure.

---
## Learning Objectives

By completing this hands-on lab, you will be able to:
-   **Trigger and observe** a data quality failure in a controlled environment.
-   **Implement a data quality "guard"** using Policy-as-Code (OPA/Rego).
-   **Verify** that the new guard successfully prevents the same failure from recurring.
-   **Understand** the practical application of the "Fail -> Guard -> Prevent" loop, the core of the Intellectual Immune System.

---
## The Workflow

This lab follows the ADR-centric workflow. Your role is to act as the **Human** who verifies the results of each step using the provided `validation_checklist.md`.

You will use the following `make` commands to step through the `fail -> guard -> prevent` cycle:
1.  `make baseline`: Confirm the pipeline works with good data.
2.  `make drift`: Simulate a failure by running the pipeline with bad data. **Note: This command is expected to fail!** This "successful failure" confirms that our initial validation is correctly detecting the data drift. This is the "illness" that our immune system will learn to fight.
3.  `make fix`: Apply a pre-built "guard" to the system.
4.  `make run`: Re-run the pipeline with the bad data to verify the guard works.

---
## The Artifact

You will interact with the following key files:
-   `Makefile`: The main interface for running the lab's steps.
-   `data/`: Contains the valid (`orders_good.csv`) and invalid (`orders_bad.csv`) datasets.
-   `scripts/validate.py`: The Python script that validates the data.
-   `guards/policies.rego`: The OPA policy file where your data quality "guard" is defined.

---
## The Prompt

According to our pedagogical principles, we provide the solution code for `guards/policies.rego` in this lab. However, if you wanted to generate this "guard" using AI, here is the prompt you would use. This is your opportunity to practice the **AI Collaboration Cycle**.

**Prompt to Generate the Data Quality Guard:**
```

As a data governance specialist, your task is to write an OPA (Rego) policy to validate incoming CSV data for a retail orders pipeline.

The validation rules are defined in our ADR. The key requirements are:

1.  The following columns must always be present: `order_id`, `customer_id`, `order_ts`, `net_amount`.
2.  The `net_amount` values must not have a Population Stability Index (PSI) greater than 0.2 when compared to a baseline, to detect sudden changes in the data's distribution (like a shift from dollars to cents).

Please generate a Rego policy that implements these two rules. The policy should deny any data that violates these conditions.

```

---
## Setup & Notes

-   **ADR & Checklist**: Before you begin, please review the "specification" for this lab in the [ADR](./adr/0001-implement-fail-guard-prevent-loop.md) and the "test cases" in the [Validation Checklist](./adr/validation_checklist.md).
-   **Environment**: This lab is designed to be run in a GitHub Codespaces environment.
-   **AI Output May Vary**: If you use the prompt above with your own LLM, the generated Rego code may differ slightly from the solution provided in this lab. This is expected. The goal is to learn the **process** of prompting, reviewing, and refining AI-generated code.
```