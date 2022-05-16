from services.gprc_service import FirehoseGRPC
from strategies import strategy_map
from services.parquet_producer import write_parquet


def run(event, context):
    tablename = event.get("tablename")
    start_block = event.get("start_block")
    block_count = event.get("block_count")

    TableStrategy = strategy_map[tablename]
    grpc_filters = TableStrategy.grpc_filters
    parquet_schema = TableStrategy.parquet_schema

    Firehose = FirehoseGRPC()

    block_stream = Firehose.stream_blocks(
        start_block,
        block_count,
        grpc_filters,
    )

    table_rows = [
        TableStrategy.process_message(block) 
        for block in block_stream
    ]
 
    write_parquet(table_rows, parquet_schema)

    
if __name__ == "__main__":
    test_event = {"tablename": "blocks", "start_block": 33, "block_count": 10}
    run(test_event, None)
