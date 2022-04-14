import grpc
import protoc_outfiles.firehose_v1_pb2 as firehose_proto
import protoc_outfiles.firehose_v1_pb2_grpc as firehose_grpc

FIREHOSE_ENDPOINT = 'localhost:13042'

class FirehoseGRPC():

    def __init__(self):
        self.channel = grpc.insecure_channel(FIREHOSE_ENDPOINT)
        self.stub = firehose_grpc.StreamStub(self.channel)
    
    @staticmethod
    def request_args(start_block, block_count, filters):
        request_args = {}
        if start_block: request_args['start_block_num'] = start_block
        if block_count: request_args['stop_block_num'] = start_block + block_count
        if filters: request_args['transforms'] = filters
        return request_args

    def stream_blocks(self, start_block=None, block_count=None, filters=None):
        request_args = self.request_args(start_block, block_count, filters)
        RequestObject = firehose_proto.Request(**request_args)
        return self.stub.Blocks(RequestObject)
