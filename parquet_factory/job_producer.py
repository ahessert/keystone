import boto3
import json
from msilib.schema import Error

from environment import PARQUET_FACTORY_ARN, AWS_REGION


BATCH_SIZE = 10000 # Number of blocks should be defined by the table depending on processing demands and must keep the job under 15 minutes (10 to be safe)

LambdaClient = boto3.client('lambda', region_name=AWS_REGION)

def run(event, context):
    """ This is a scheduler of the Parquet Factory Jobs.
        It's purpose is to scale large processing joba
        accross many lambda tasks. 
        
        event payload:
            {
                tablename: the parquet schema we are building
                job_type: process 'historical' OR 'update' recent data
                block_start: only included in historical jobs
            }
    """
    job_type = event.get('job_type')
    tablename = event.get('tablename')
    current_block = 111111111 #function get_current_block()

    if job_type == 'update':
        block_start = get_last_block_proccessed()
        invoke_parquet_job(tablename, block_start)
    elif job_type == 'historical':
        block_start = event.get('block_start')
        for idx in range(block_start, current_block, BATCH_SIZE):
            invoke_parquet_job(tablename, idx, BATCH_SIZE)
    else:
        raise Error("Must include job_type 'update' OR 'historical': received '%s'" % 'job_type')

def invoke_parquet_job(tablename, block_start, block_count=None):
    payload = {
        'tablename': tablename,
        'block_start': block_start,
        'block_count': block_count,
    }

    params = {
            'FunctionName': PARQUET_FACTORY_ARN,
            'InvocationType': 'Event',
            'Payload': bytes(json.dumps(payload), 'utf-8')
    }

    LambdaClient.invoke(**params)

def get_last_block_proccessed():
    NotImplemented