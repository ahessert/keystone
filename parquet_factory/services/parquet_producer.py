from datetime import datetime
import pyarrow as pa
import pyarrow.parquet as pq
from google.protobuf.json_format import MessageToDict

def make_table(block_stream):
    schema = pa.schema(
        {"number": pa.int64(), "nonce": pa.string(), "timestamp": pa.string()}
    )

    numbers = []
    nonces = []
    timestamps = []
    for block in block_stream:
        des_block = MessageToDict(block)["block"]
        numbers.append(int(des_block["number"]))
        nonces.append(des_block['header']["nonce"])
        # TODO: Convert this from string to timestamp type
        timestamps.append(des_block["header"]["timestamp"])

    table = pa.Table.from_pydict(
        dict(zip(schema.names, (numbers, nonces, timestamps))), schema=schema
    )
    return table 

def write_parquet(table):
    str(datetime.utcnow())

    pq.write_table(
        table=table,
        where=str(datetime.utcnow()) + '.parquet',
        compression='snappy',
        filesystem='s3://indigo-data-lake'
    )