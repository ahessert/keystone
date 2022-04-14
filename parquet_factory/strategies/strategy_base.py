
class Strategy():

    @staticmethod
    def grpc_filters():
        raise NotImplementedError

    @staticmethod
    def build_table():
        raise NotImplementedError

    @staticmethod
    def parquet_partition():
        raise NotImplementedError
