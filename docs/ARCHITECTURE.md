# Architecture

~~~mermaid
flowchart LR
    Analyst[Analyst] --> Dashboard[Flask Dashboard]
    Analyst --> API[REST API]
    API --> Engine[Analysis Engine]
    Engine --> Store[(SQLite Findings)]
    Dashboard --> Store
    Store --> Reports[JSON Results]
~~~

## Components

- Flask dashboard for analyst-facing review.
- REST API for automation and integrations.
- Domain-specific service module for scoring and analysis.
- SQLite persistence for local evidence history.
- Docker and GitHub Actions for portable delivery.
