# keystone

## Generate grpc protos
```
python3 -m grpc.tools.protoc -I../proto  -I../proto-ethereum --python_out=. --grpc_python_out=. ../proto/sf/firehose/v1/firehose.proto ../proto-ethereum/sf/ethereum/codec/v1/codec.proto
```