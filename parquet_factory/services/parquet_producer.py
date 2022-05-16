from datetime import datetime
import pyarrow as pa
import pyarrow.parquet as pq

from environment import PARQUET_OUTDIR

def write_parquet(rows, schema):
    table = pa.Table.from_pylist(rows, schema=schema)
    pq.write_table(
        table=table,
        where=str(datetime.utcnow()) + '.parquet',
        compression='snappy',
        filesystem=PARQUET_OUTDIR
    )
