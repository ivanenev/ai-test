# Personal Knowledge Base (PKB)

## Architecture

- **Metadata Storage**: PostgreSQL
- **File Storage**: MinIO
- **Version Control**: Built-in document versioning
- **Relationships**: Temporal relationship tracking

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables in `.env`

3. Run database migrations:
   ```bash
   alembic upgrade head
   ```

4. Start the MinIO server

## Development

- `src/`: Main application code
- `tests/`: Unit and integration tests
- `migrations/`: Database migrations
- `storage/`: Local storage for development
