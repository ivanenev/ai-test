from setuptools import setup, find_packages

setup(
    name="pkb",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "psycopg2-binary",
        "minio",
        "python-dotenv",
        "alembic"
    ],
)
