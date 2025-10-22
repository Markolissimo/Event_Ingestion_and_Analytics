# Event Ingestion and Analytics Service

A service for ingesting and analyzing event data with idempotent operations and real-time analytics.

## Features

- **Event Ingestion**: High-throughput API for receiving events
- **Idempotent Operations**: Duplicate events are handled gracefully
- **Analytics**: Real-time analytics endpoints for event data
- **Data Import**: CLI tool for bulk importing historical data

## Tech Stack

- **API Framework**: FastAPI
- **Database**: PostgreSQL (Hot Storage), DuckDB (Cold Storage) - the item which will be explored
- **Message Queue**: NATS with JetStream - the item which will be explored
- **Testing**: pytest with async support
- **Code Quality**: black, isort, mypy, flake8

## Getting Started

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- PostgreSQL

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd event-ingestion-analytics
   ```

2. Create and activate a virtual environment:
   On Linux/MacOS
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   On Windows
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

### Running the Service

```bash
uvicorn src.event_ingestion.main:app --reload
```

## Project Structure

```
src/
  event_ingestion/
    api/           # API endpoints and routes
    core/          # Core application logic
    db/            # Database models and migrations
    models/        # Pydantic models
    services/      # Business logic services
    __init__.py
    main.py        # Application entry point

docs/             # Documentation
  TECH_TASK_DESCRIPTION.md
  ADR.md          # Architecture Decision Records
  LEARNED.md      # Lessons learned during development
```

## API Documentation

Once the service is running, you can access:
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

## License
[MIT](LICENSE)
