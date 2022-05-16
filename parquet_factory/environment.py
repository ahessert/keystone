import os
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"), # load variables from .env file
    **os.environ,  # override loaded values with environment variables
}

FIREHOSE_ENDPOINT = config.get('GRPC_ENDPOINT', 'localhost:13042')

AWS_REGION = config.get('AWS_REGION', "us-east-2")
PARQUET_FACTORY_ARN = config.get('PARQUET_FACTORY_ARN')
PARQUET_OUTDIR = config.get('PARQUET_OUTDIR', 's3://indigo-data-lake')
