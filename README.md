# Keystone

Welcome to the Indigo data pipeline. This repository extracts all EVM blocks, logs, and transaction traces and serializes them into parquet files. This is the base for the Indigo data warehouse (implemented with snowflake and dbt).

Two primary components are:

1) Implementation of Firehose by [Streaming Fast](https://www.streamingfast.io/) streaming EVM data to flat files S3.
2) Parquet Factory which creates parquet files for data warehouse use.



![Screen Shot 2022-04-20 at 4 55 50 PM](https://user-images.githubusercontent.com/10226899/164321288-00b352ed-a3fa-4d81-9983-6872705fec7d.png)
