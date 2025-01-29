from logging.config import fileConfig
from os import environ
from dotenv import load_dotenv
from alembic import context
from sqlalchemy import create_engine

load_dotenv()

config = context.config
fileConfig(config.config_file_name)

target_metadata = None

def get_url():
    return f"postgresql+psycopg2://{environ['POSTGRES_USER']}:{environ['POSTGRES_PASSWORD']}@{environ['POSTGRES_HOST']}:{environ['POSTGRES_PORT']}/{environ['POSTGRES_DB']}"

def run_migrations_offline():
    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = create_engine(get_url())

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
