import protoc_outfiles.sfeth_codec_v1_pb2 as sfeth_proto

from strategies.strategy_base import Strategy 

class Blocks(Strategy):
    @staticmethod
    def grpc_filters():
        return []

    @staticmethod
    def build_table(proto_object):
        table_row = sfeth_proto.Block
        return table_row
        
    @staticmethod
    def parquet_partition():
        return 'block_hash'
