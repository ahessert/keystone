# syntax=docker/dockerfile:1
FROM golang:1.18.0 as build

# Install Streaming Fast's deep-mind geth EVM node
WORKDIR /src
RUN git clone https://github.com/streamingfast/go-ethereum
WORKDIR /src/go-ethereum
RUN git checkout release/geth-1.10.x-dm
RUN go install ./cmd/geth
RUN go install ./cmd/bootnode

# Install sfeth for streaming EVM data
WORKDIR /src
RUN git clone https://github.com/streamingfast/sf-ethereum
WORKDIR /src/sf-ethereum
RUN go install ./cmd/sfeth

# Firehose is sfeths gRPC endpoint
WORKDIR /src/firehose
WORKDIR /src/firehose/mindreader
RUN geth --mainnet dumpgenesis > ./genesis.json
WORKDIR /src/firehose
