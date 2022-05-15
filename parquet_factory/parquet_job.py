from services.gprc_service import FirehoseGRPC
from strategies import strategy_map
from services.parquet_producer import make_table, write_parquet


def run(event, context):
    tablename = event.get("tablename")
    start_block = event.get("start_block")
    block_count = event.get("block_count")

    TableStrategy = strategy_map[tablename]
    Firehose = FirehoseGRPC()

    block_stream = Firehose.stream_blocks(
        start_block,
        block_count,
        TableStrategy.grpc_filters(),
    )

    # for message in block_stream:
    #     TableStrategy.build_table(message)

    table = make_table(block_stream)
    write_parquet(table)

    # grpc_stream > TableStrategy.build_table() > make_parquet

    
if __name__ == "__main__":
    test_event = {"tablename": "blocks", "start_block": 33, "block_count": 10}
    run(test_event, None)
