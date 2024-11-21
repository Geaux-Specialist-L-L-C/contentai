# Copilot Context for K-12 Educational Content Generator

This file provides GitHub Copilot with context about the repository's purpose, structure, and guidelines. It helps Copilot generate more accurate and relevant code suggestions.

## Repository Purpose

The goal of this project is to generate curriculum-aligned educational content for K-12 students using AI models. It includes:

- Text-based lessons and assessments using language models.
- Visual content (e.g., diagrams) using diffusion-based models.
- Audio content (e.g., narrated lessons) using speech synthesis.

## Key Features

- Fine-tuning pre-trained models (e.g., GPT, Stable Diffusion, Tacotron).
- Scalable deployment via Docker, Porter, AWS, and Azure.
- Cloud-based data storage and processing using Snowflake.

## Repository Structure

```plaintext
/src
  /models         # Custom models and fine-tuning scripts
  /data           # Data ingestion and preprocessing
  /services       # API endpoints for content generation
  /notebooks      # Interactive development and exploration
  /config         # Cloud configuration and credentials
```

## Development Environment

- GitHub Codespaces is the primary IDE for this project.
- Dependencies are managed via `requirements.txt`.
- Code is deployed using Docker and Porter.

## Sample Tasks for Copilot

Here are examples of tasks Copilot might assist with:

1. Generate Python scripts for fine-tuning GPT-based models.
2. Create FastAPI endpoints for content generation.
3. Write Dockerfiles for containerized deployments.
4. Generate test cases for model outputs and APIs.
5. Write scripts for uploading datasets to AWS S3 or Azure Blob Storage.

## Best Practices

- Use clear and concise comments to explain the purpose of your code.
- Always validate Copilot's suggestions for accuracy and efficiency.
- Follow the coding standards outlined in `CONTRIBUTING.md`.

## Related Files

- `README.md`: Overview and quick start guide.
- `CONTRIBUTING.md`: Contribution guidelines.
- `Dockerfile`: Containerization instructions.
- `.env.example`: Template for environment variables.
