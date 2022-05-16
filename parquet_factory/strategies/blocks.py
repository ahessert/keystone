import protoc_outfiles.sfeth_codec_v1_pb2 as sfeth_proto
import pyarrow as pa

from strategies.strategy_base import Strategy 

class Blocks(Strategy):
    grpc_filters = []
    parquet_schema = pa.schema({
        "number": pa.int64(), 
        "nonce": pa.string(), 
        "timestamp": pa.string()
    })

    @staticmethod
    def process_message(proto_object):
        proto = sfeth_proto.Block()
        proto.ParseFromString(proto_object.block.value)
        return {
            "number": proto.number,
            "nonce": str(proto.header.nonce),
            "timestamp": str(proto.header.timestamp)
        }
