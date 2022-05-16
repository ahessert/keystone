
class Strategy():
    grpc_filters = NotImplementedError
    parquet_schema = NotImplementedError

    @staticmethod
    def process_message():
        raise NotImplementedError
