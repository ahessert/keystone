FROM python:3.9.1-slim

WORKDIR /app

# Copy in reqired files
COPY parquet_factory/requirements.txt ./

# Install Python Requirements
RUN pip install -U pip
RUN pip install -r requirements.txt