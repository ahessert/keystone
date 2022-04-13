# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging
import asyncio

import grpc
from sf.firehose.v1.firehose_pb2 import Request, Response
from sf.firehose.v1.firehose_pb2_grpc import StreamStub


async def run() -> None:
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    async with grpc.aio.insecure_channel('localhost:13042') as channel:
        stub = StreamStub(channel)

        # Read from an async generator
        async for response in stub.Blocks(
            Request()):
            print("Greeter client received from async generator: " +
                  response)


        # Direct read from the stub
        stream = stub.Blocks(Request())
        while True:
            response = await stream.read()
            if response == grpc.aio.EOF:
                break
            print("Greeter client received from direct read: " +
                    response)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
