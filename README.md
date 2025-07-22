# Lean Data Engineering

Welcome to the `lean-data-engineering` GitHub repository, a practical companion to the book **"Lean Data Engineering: [Your Book Title Here, e.g., A Guide to AI-Powered Architecture]"**.

This repository serves as a **live manual** for the hands-on labs and executable code examples presented in the book. It embodies the core philosophy of **Jibun OS** and **AI Collaboration**, providing you with a dynamic, up-to-date environment to practice and apply the concepts learned.

## Why This Repository?

The book focuses on the "Why" and "What"—the core principles, strategies, and architectural blueprints for modern data management in the AI era. This repository complements the book by providing the "How"—the concrete, executable examples and hands-on labs that might evolve faster than a printed book.

By separating the executable content from the static book, we ensure:
* **Up-to-Date Code**: Code examples are continuously updated to reflect the latest tools and best practices.
* **Practical Application**: You can immediately apply theoretical knowledge in a real coding environment.
* **AI-Powered Learning**: Experience the AI Collaboration Cycle firsthand, from defining strategic intent in an Architecture Decision Record (ARD) to generating and reviewing Infrastructure as Code (IaC) with AI.

## Get Started Instantly with GitHub Codespaces

The fastest way to get started with any lab in this repository is by using GitHub Codespaces. It provides a pre-configured, cloud-based development environment that requires no local setup.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/mikieto/lean-data-engineering)

**Click the badge above to launch a dedicated Codespaces environment for this repository.** This will automatically set up all necessary tools (Terraform, Python, AWS CLI, dbt, linters, etc.) and dependencies, allowing you to jump straight into any lab exercise.

## Repository Structure

This repository is organized by chapters, with each chapter containing its relevant hands-on labs and code examples.

* `**/.devcontainer/`**: Contains the Visual Studio Code Dev Container configuration (Dockerfile, devcontainer.json) that defines the consistent development environment for all labs in this repository. This lives at the repository root.
* `**chapterXX/`**: Each folder (`chapter01/`, `chapter02/`, etc.) corresponds to a chapter in the book.
    * `**chapterXX/README.md`**: Provides the specific instructions, lab scenarios, AI interaction examples (including sample prompts), and guidance for the hands-on exercises of that chapter.
    * `**chapterXX/main.tf`, `chapterXX/data_definitions.yaml` (or similar files)**: Contains the executable sample code and configuration files for the chapter's lab. These are the results of AI collaboration, not purely AI-generated.
    * `**chapterXX/adr/`**: (Optional) Directory for Architecture Decision Records (ADRs) specific to the chapter's architectural decisions, if applicable.
    * `**chapterXX/Makefile`**: Contains simplified `make` commands to run, validate, and manage resources for the chapter's lab.

## How to Navigate the Labs

1.  **Launch Codespaces**: Click the "Open in GitHub Codespaces" badge above.
2.  **Navigate to a Chapter**: Once your Codespaces environment is ready, open the `README.md` file within the desired `chapterXX/` folder (e.g., `chapter02/README.md`).
3.  **Follow the Instructions**: Each `chapterXX/README.md` will guide you through the specific lab scenario, AI interaction steps, and how to run the provided code using `make` commands.

We encourage you to explore the repository, experiment with the code, and embark on your journey to becoming an **AI Collaboration Architect (ACA)**!

---