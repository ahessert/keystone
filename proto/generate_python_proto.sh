# run this file from keystone home directory
# for protoc run `brew install protobuf`
python3 -m grpc_tools.protoc -I=./proto --python_out=./parquet_factory/protoc_outfiles --grpc_python_out=./parquet_factory/protoc_outfiles ./proto/sfeth-codec-v1.proto
python3 -m grpc_tools.protoc -I=./proto --python_out=./parquet_factory/protoc_outfiles ./proto/firehose-v1.proto
