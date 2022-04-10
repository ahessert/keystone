# syntax=docker/dockerfile:1
FROM golang:1.18.0 as build

# Install grpcurl
RUN go install github.com/fullstorydev/grpcurl/cmd/grpcurl@v1.8.6

# Install proto dependencies
WORKDIR /src
RUN git clone https://github.com/streamingfast/proto.git
RUN git clone https://github.com/streamingfast/proto-ethereum.git

ENTRYPOINT grpcurl -plaintext -import-path ./proto -import-path ./proto-ethereum -proto sf/ethereum/codec/v1/codec.proto -proto sf/firehose/v1/firehose.proto -d '' sfeth:13042 sf.firehose.v1.Stream.Blocks

