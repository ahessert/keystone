# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sfeth-codec-v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14sfeth-codec-v1.proto\x12\x14sf.ethereum.codec.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc9\x03\n\x05\x42lock\x12\x0b\n\x03ver\x18\x01 \x01(\x05\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x0e\n\x06number\x18\x03 \x01(\x04\x12\x0c\n\x04size\x18\x04 \x01(\x04\x12\x31\n\x06header\x18\x05 \x01(\x0b\x32!.sf.ethereum.codec.v1.BlockHeader\x12\x31\n\x06uncles\x18\x06 \x03(\x0b\x32!.sf.ethereum.codec.v1.BlockHeader\x12\x42\n\x12transaction_traces\x18\n \x03(\x0b\x32&.sf.ethereum.codec.v1.TransactionTrace\x12<\n\x0f\x62\x61lance_changes\x18\x0b \x03(\x0b\x32#.sf.ethereum.codec.v1.BalanceChange\x12\x36\n\x0c\x63ode_changes\x18\x14 \x03(\x0b\x32 .sf.ethereum.codec.v1.CodeChange\x12\x19\n\x11\x66iltering_applied\x18( \x01(\x08\x12%\n\x1d\x66iltering_include_filter_expr\x18) \x01(\t\x12%\n\x1d\x66iltering_exclude_filter_expr\x18* \x01(\t\"D\n\x0fHeaderOnlyBlock\x12\x31\n\x06header\x18\x05 \x01(\x0b\x32!.sf.ethereum.codec.v1.BlockHeader\"\xa4\x01\n\rBlockWithRefs\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x1b.sf.ethereum.codec.v1.Block\x12\x45\n\x16transaction_trace_refs\x18\x03 \x01(\x0b\x32%.sf.ethereum.codec.v1.TransactionRefs\x12\x14\n\x0cirreversible\x18\x04 \x01(\x08\"!\n\x0fTransactionRefs\x12\x0e\n\x06hashes\x18\x01 \x03(\x0c\"B\n\rUnclesHeaders\x12\x31\n\x06uncles\x18\x01 \x03(\x0b\x32!.sf.ethereum.codec.v1.BlockHeader\"(\n\x08\x42lockRef\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x0e\n\x06number\x18\x02 \x01(\x04\"\xfa\x02\n\x0b\x42lockHeader\x12\x13\n\x0bparent_hash\x18\x01 \x01(\x0c\x12\x12\n\nuncle_hash\x18\x02 \x01(\x0c\x12\x10\n\x08\x63oinbase\x18\x03 \x01(\x0c\x12\x12\n\nstate_root\x18\x04 \x01(\x0c\x12\x19\n\x11transactions_root\x18\x05 \x01(\x0c\x12\x14\n\x0creceipt_root\x18\x06 \x01(\x0c\x12\x12\n\nlogs_bloom\x18\x07 \x01(\x0c\x12\x30\n\ndifficulty\x18\x08 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12\x0e\n\x06number\x18\t \x01(\x04\x12\x11\n\tgas_limit\x18\n \x01(\x04\x12\x10\n\x08gas_used\x18\x0b \x01(\x04\x12-\n\ttimestamp\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nextra_data\x18\r \x01(\x0c\x12\x10\n\x08mix_hash\x18\x0e \x01(\x0c\x12\r\n\x05nonce\x18\x0f \x01(\x04\x12\x0c\n\x04hash\x18\x10 \x01(\x0c\"\x17\n\x06\x42igInt\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\"\xf2\x06\n\x10TransactionState\x12\x44\n\x0eprevious_state\x18\x01 \x01(\x0e\x32,.sf.ethereum.codec.v1.TransactionState.State\x12\x43\n\rcurrent_state\x18\x02 \x01(\x0e\x32,.sf.ethereum.codec.v1.TransactionState.State\x12\x45\n\ntransition\x18\n \x01(\x0e\x32\x31.sf.ethereum.codec.v1.TransactionState.Transition\x12\x0c\n\x04hash\x18\x0b \x01(\x0c\x12.\n\x03trx\x18\x03 \x01(\x0b\x32!.sf.ethereum.codec.v1.Transaction\x12\x37\n\x0c\x62lock_header\x18\x04 \x01(\x0b\x32!.sf.ethereum.codec.v1.BlockHeader\x12\x42\n\x12transaction_traces\x18\x05 \x01(\x0b\x32&.sf.ethereum.codec.v1.TransactionTrace\x12\x14\n\x0c\x63onfirmation\x18\x06 \x01(\x04\x12<\n\x11head_block_header\x18\x07 \x01(\x0b\x32!.sf.ethereum.codec.v1.BlockHeader\x12\x18\n\x10replaced_by_hash\x18\x08 \x01(\x0c\x12\x36\n\x12pending_first_seen\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11pending_last_seen\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9c\x01\n\nTransition\x12\x0e\n\nTRANS_INIT\x10\x00\x12\x10\n\x0cTRANS_POOLED\x10\x01\x12\x0f\n\x0bTRANS_MINED\x10\x02\x12\x10\n\x0cTRANS_FORKED\x10\x03\x12\x13\n\x0fTRANS_CONFIRMED\x10\x04\x12\x12\n\x0eTRANS_REPLACED\x10\x05\x12 \n\x1cTRANS_SPECULATIVELY_EXECUTED\x10\x06\"U\n\x05State\x12\x11\n\rSTATE_UNKNOWN\x10\x00\x12\x11\n\rSTATE_PENDING\x10\x01\x12\x12\n\x0eSTATE_IN_BLOCK\x10\x02\x12\x12\n\x0eSTATE_REPLACED\x10\x03\"\xe5\x01\n\x0bTransaction\x12\n\n\x02to\x18\x01 \x01(\x0c\x12\r\n\x05nonce\x18\x02 \x01(\x04\x12/\n\tgas_price\x18\x03 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12\x11\n\tgas_limit\x18\x04 \x01(\x04\x12+\n\x05value\x18\x05 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12\r\n\x05input\x18\x06 \x01(\x0c\x12\t\n\x01v\x18\x07 \x01(\x0c\x12\t\n\x01r\x18\x08 \x01(\x0c\x12\t\n\x01s\x18\t \x01(\x0c\x12\x0c\n\x04hash\x18\x15 \x01(\x0c\x12\x0c\n\x04\x66rom\x18\x16 \x01(\x0c\"\xd8\x03\n\x10TransactionTrace\x12\n\n\x02to\x18\x01 \x01(\x0c\x12\r\n\x05nonce\x18\x02 \x01(\x04\x12/\n\tgas_price\x18\x03 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12\x11\n\tgas_limit\x18\x04 \x01(\x04\x12+\n\x05value\x18\x05 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12\r\n\x05input\x18\x06 \x01(\x0c\x12\t\n\x01v\x18\x07 \x01(\x0c\x12\t\n\x01r\x18\x08 \x01(\x0c\x12\t\n\x01s\x18\t \x01(\x0c\x12\x10\n\x08gas_used\x18\n \x01(\x04\x12\r\n\x05index\x18\x14 \x01(\r\x12\x0c\n\x04hash\x18\x15 \x01(\x0c\x12\x0c\n\x04\x66rom\x18\x16 \x01(\x0c\x12\x13\n\x0breturn_data\x18\x17 \x01(\x0c\x12\x12\n\npublic_key\x18\x18 \x01(\x0c\x12<\n\x06status\x18\x1e \x01(\x0e\x32,.sf.ethereum.codec.v1.TransactionTraceStatus\x12\x39\n\x07receipt\x18\x1f \x01(\x0b\x32(.sf.ethereum.codec.v1.TransactionReceipt\x12)\n\x05\x63\x61lls\x18  \x03(\x0b\x32\x1a.sf.ethereum.codec.v1.Call\"\x88\x01\n\x1cTransactionTraceWithBlockRef\x12\x35\n\x05trace\x18\x01 \x01(\x0b\x32&.sf.ethereum.codec.v1.TransactionTrace\x12\x31\n\tblock_ref\x18\x02 \x01(\x0b\x32\x1e.sf.ethereum.codec.v1.BlockRef\"\x82\x01\n\x12TransactionReceipt\x12\x12\n\nstate_root\x18\x01 \x01(\x0c\x12\x1b\n\x13\x63umulative_gas_used\x18\x02 \x01(\x04\x12\x12\n\nlogs_bloom\x18\x03 \x01(\x0c\x12\'\n\x04logs\x18\x04 \x03(\x0b\x32\x19.sf.ethereum.codec.v1.Log\"W\n\x03Log\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06topics\x18\x02 \x03(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\r\n\x05index\x18\x04 \x01(\r\x12\x12\n\nblockIndex\x18\x06 \x01(\r\"\xdb\x08\n\x04\x43\x61ll\x12\r\n\x05index\x18\x01 \x01(\r\x12\x14\n\x0cparent_index\x18\x02 \x01(\r\x12\r\n\x05\x64\x65pth\x18\x03 \x01(\r\x12\x31\n\tcall_type\x18\x04 \x01(\x0e\x32\x1e.sf.ethereum.codec.v1.CallType\x12\x0e\n\x06\x63\x61ller\x18\x05 \x01(\x0c\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\x0c\x12+\n\x05value\x18\x07 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12\x11\n\tgas_limit\x18\x08 \x01(\x04\x12\x14\n\x0cgas_consumed\x18\t \x01(\x04\x12\x13\n\x0breturn_data\x18\r \x01(\x0c\x12\r\n\x05input\x18\x0e \x01(\x0c\x12\x15\n\rexecuted_code\x18\x0f \x01(\x08\x12\x0f\n\x07suicide\x18\x10 \x01(\x08\x12I\n\x10keccak_preimages\x18\x14 \x03(\x0b\x32/.sf.ethereum.codec.v1.Call.KeccakPreimagesEntry\x12<\n\x0fstorage_changes\x18\x15 \x03(\x0b\x32#.sf.ethereum.codec.v1.StorageChange\x12<\n\x0f\x62\x61lance_changes\x18\x16 \x03(\x0b\x32#.sf.ethereum.codec.v1.BalanceChange\x12\x38\n\rnonce_changes\x18\x18 \x03(\x0b\x32!.sf.ethereum.codec.v1.NonceChange\x12\'\n\x04logs\x18\x19 \x03(\x0b\x32\x19.sf.ethereum.codec.v1.Log\x12\x36\n\x0c\x63ode_changes\x18\x1a \x03(\x0b\x32 .sf.ethereum.codec.v1.CodeChange\x12\x18\n\x10\x63reated_accounts\x18\x1b \x03(\x0c\x12\x34\n\x0bgas_changes\x18\x1c \x03(\x0b\x32\x1f.sf.ethereum.codec.v1.GasChange\x12\x32\n\ngas_events\x18\x1d \x03(\x0b\x32\x1e.sf.ethereum.codec.v1.GasEvent\x12\x15\n\rstatus_failed\x18\n \x01(\x08\x12\x17\n\x0fstatus_reverted\x18\x0c \x01(\x08\x12\x16\n\x0e\x66\x61ilure_reason\x18\x0b \x01(\t\x12\x16\n\x0estate_reverted\x18\x1e \x01(\x08\x12G\n\x15\x65rc20_balance_changes\x18\x32 \x03(\x0b\x32(.sf.ethereum.codec.v1.ERC20BalanceChange\x12G\n\x15\x65rc20_transfer_events\x18\x33 \x03(\x0b\x32(.sf.ethereum.codec.v1.ERC20TransferEvent\x12\x19\n\x11\x66iltering_matched\x18< \x01(\x08\x1a\x36\n\x14KeccakPreimagesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x92\x01\n\x12\x45RC20BalanceChange\x12\x16\n\x0eholder_address\x18\x01 \x01(\x0c\x12\x31\n\x0bold_balance\x18\x02 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12\x31\n\x0bnew_balance\x18\x03 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\"\\\n\x12\x45RC20TransferEvent\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x0c\x12\n\n\x02to\x18\x02 \x01(\x0c\x12,\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\"S\n\rStorageChange\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x11\n\told_value\x18\x03 \x01(\x0c\x12\x11\n\tnew_value\x18\x04 \x01(\x0c\"\xf9\x04\n\rBalanceChange\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12/\n\told_value\x18\x02 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12/\n\tnew_value\x18\x03 \x01(\x0b\x32\x1c.sf.ethereum.codec.v1.BigInt\x12:\n\x06reason\x18\x04 \x01(\x0e\x32*.sf.ethereum.codec.v1.BalanceChange.Reason\"\xb8\x03\n\x06Reason\x12\x12\n\x0eREASON_UNKNOWN\x10\x00\x12\x1c\n\x18REASON_REWARD_MINE_UNCLE\x10\x01\x12\x1c\n\x18REASON_REWARD_MINE_BLOCK\x10\x02\x12\x1e\n\x1aREASON_DAO_REFUND_CONTRACT\x10\x03\x12\x1d\n\x19REASON_DAO_ADJUST_BALANCE\x10\x04\x12\x13\n\x0fREASON_TRANSFER\x10\x05\x12\x1a\n\x16REASON_GENESIS_BALANCE\x10\x06\x12\x12\n\x0eREASON_GAS_BUY\x10\x07\x12!\n\x1dREASON_REWARD_TRANSACTION_FEE\x10\x08\x12\x1b\n\x17REASON_REWARD_FEE_RESET\x10\x0e\x12\x15\n\x11REASON_GAS_REFUND\x10\t\x12\x18\n\x14REASON_TOUCH_ACCOUNT\x10\n\x12\x19\n\x15REASON_SUICIDE_REFUND\x10\x0b\x12\x1b\n\x17REASON_SUICIDE_WITHDRAW\x10\r\x12 \n\x1cREASON_CALL_BALANCE_OVERRIDE\x10\x0c\x12\x0f\n\x0bREASON_BURN\x10\x0f\"D\n\x0bNonceChange\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x11\n\told_value\x18\x02 \x01(\x04\x12\x11\n\tnew_value\x18\x03 \x01(\x04\"e\n\nCodeChange\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x10\n\x08old_hash\x18\x02 \x01(\x0c\x12\x10\n\x08old_code\x18\x03 \x01(\x0c\x12\x10\n\x08new_hash\x18\x04 \x01(\x0c\x12\x10\n\x08new_code\x18\x05 \x01(\x0c\"\x8e\x05\n\tGasChange\x12\x11\n\told_value\x18\x01 \x01(\x04\x12\x11\n\tnew_value\x18\x02 \x01(\x04\x12\x36\n\x06reason\x18\x03 \x01(\x0e\x32&.sf.ethereum.codec.v1.GasChange.Reason\"\xa2\x04\n\x06Reason\x12\x12\n\x0eREASON_UNKNOWN\x10\x00\x12\x0f\n\x0bREASON_CALL\x10\x01\x12\x14\n\x10REASON_CALL_CODE\x10\x02\x12\x19\n\x15REASON_CALL_DATA_COPY\x10\x03\x12\x14\n\x10REASON_CODE_COPY\x10\x04\x12\x17\n\x13REASON_CODE_STORAGE\x10\x05\x12\x1c\n\x18REASON_CONTRACT_CREATION\x10\x06\x12\x1d\n\x19REASON_CONTRACT_CREATION2\x10\x07\x12\x18\n\x14REASON_DELEGATE_CALL\x10\x08\x12\x14\n\x10REASON_EVENT_LOG\x10\t\x12\x18\n\x14REASON_EXT_CODE_COPY\x10\n\x12\x1b\n\x17REASON_FAILED_EXECUTION\x10\x0b\x12\x18\n\x14REASON_INTRINSIC_GAS\x10\x0c\x12\x1f\n\x1bREASON_PRECOMPILED_CONTRACT\x10\r\x12!\n\x1dREASON_REFUND_AFTER_EXECUTION\x10\x0e\x12\x11\n\rREASON_RETURN\x10\x0f\x12\x1b\n\x17REASON_RETURN_DATA_COPY\x10\x10\x12\x11\n\rREASON_REVERT\x10\x11\x12\x18\n\x14REASON_SELF_DESTRUCT\x10\x12\x12\x16\n\x12REASON_STATIC_CALL\x10\x13\x12\x1c\n\x18REASON_STATE_COLD_ACCESS\x10\x14\"\x9e\x01\n\x08GasEvent\x12-\n\x02id\x18\x01 \x01(\x0e\x32!.sf.ethereum.codec.v1.GasEvent.Id\x12\x0b\n\x03gas\x18\x02 \x01(\x04\x12\x19\n\x11linked_call_index\x18\x03 \x01(\x04\";\n\x02Id\x12\x0e\n\nID_UNKNOWN\x10\x00\x12\x11\n\rID_AFTER_CALL\x10\x01\x12\x12\n\x0eID_BEFORE_CALL\x10\x02*N\n\x16TransactionTraceStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\x0c\n\x08REVERTED\x10\x03*Y\n\x08\x43\x61llType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04\x43\x41LL\x10\x01\x12\x0c\n\x08\x43\x41LLCODE\x10\x02\x12\x0c\n\x08\x44\x45LEGATE\x10\x03\x12\n\n\x06STATIC\x10\x04\x12\n\n\x06\x43REATE\x10\x05\x42\x46ZDgithub.com/streamingfast/sf-ethereum/pb/sf/ethereum/codec/v1;pbcodecb\x06proto3')

_TRANSACTIONTRACESTATUS = DESCRIPTOR.enum_types_by_name['TransactionTraceStatus']
TransactionTraceStatus = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONTRACESTATUS)
_CALLTYPE = DESCRIPTOR.enum_types_by_name['CallType']
CallType = enum_type_wrapper.EnumTypeWrapper(_CALLTYPE)
UNKNOWN = 0
SUCCEEDED = 1
FAILED = 2
REVERTED = 3
UNSPECIFIED = 0
CALL = 1
CALLCODE = 2
DELEGATE = 3
STATIC = 4
CREATE = 5


_BLOCK = DESCRIPTOR.message_types_by_name['Block']
_HEADERONLYBLOCK = DESCRIPTOR.message_types_by_name['HeaderOnlyBlock']
_BLOCKWITHREFS = DESCRIPTOR.message_types_by_name['BlockWithRefs']
_TRANSACTIONREFS = DESCRIPTOR.message_types_by_name['TransactionRefs']
_UNCLESHEADERS = DESCRIPTOR.message_types_by_name['UnclesHeaders']
_BLOCKREF = DESCRIPTOR.message_types_by_name['BlockRef']
_BLOCKHEADER = DESCRIPTOR.message_types_by_name['BlockHeader']
_BIGINT = DESCRIPTOR.message_types_by_name['BigInt']
_TRANSACTIONSTATE = DESCRIPTOR.message_types_by_name['TransactionState']
_TRANSACTION = DESCRIPTOR.message_types_by_name['Transaction']
_TRANSACTIONTRACE = DESCRIPTOR.message_types_by_name['TransactionTrace']
_TRANSACTIONTRACEWITHBLOCKREF = DESCRIPTOR.message_types_by_name['TransactionTraceWithBlockRef']
_TRANSACTIONRECEIPT = DESCRIPTOR.message_types_by_name['TransactionReceipt']
_LOG = DESCRIPTOR.message_types_by_name['Log']
_CALL = DESCRIPTOR.message_types_by_name['Call']
_CALL_KECCAKPREIMAGESENTRY = _CALL.nested_types_by_name['KeccakPreimagesEntry']
_ERC20BALANCECHANGE = DESCRIPTOR.message_types_by_name['ERC20BalanceChange']
_ERC20TRANSFEREVENT = DESCRIPTOR.message_types_by_name['ERC20TransferEvent']
_STORAGECHANGE = DESCRIPTOR.message_types_by_name['StorageChange']
_BALANCECHANGE = DESCRIPTOR.message_types_by_name['BalanceChange']
_NONCECHANGE = DESCRIPTOR.message_types_by_name['NonceChange']
_CODECHANGE = DESCRIPTOR.message_types_by_name['CodeChange']
_GASCHANGE = DESCRIPTOR.message_types_by_name['GasChange']
_GASEVENT = DESCRIPTOR.message_types_by_name['GasEvent']
_TRANSACTIONSTATE_TRANSITION = _TRANSACTIONSTATE.enum_types_by_name['Transition']
_TRANSACTIONSTATE_STATE = _TRANSACTIONSTATE.enum_types_by_name['State']
_BALANCECHANGE_REASON = _BALANCECHANGE.enum_types_by_name['Reason']
_GASCHANGE_REASON = _GASCHANGE.enum_types_by_name['Reason']
_GASEVENT_ID = _GASEVENT.enum_types_by_name['Id']
Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.Block)
  })
_sym_db.RegisterMessage(Block)

HeaderOnlyBlock = _reflection.GeneratedProtocolMessageType('HeaderOnlyBlock', (_message.Message,), {
  'DESCRIPTOR' : _HEADERONLYBLOCK,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.HeaderOnlyBlock)
  })
_sym_db.RegisterMessage(HeaderOnlyBlock)

BlockWithRefs = _reflection.GeneratedProtocolMessageType('BlockWithRefs', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKWITHREFS,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.BlockWithRefs)
  })
_sym_db.RegisterMessage(BlockWithRefs)

TransactionRefs = _reflection.GeneratedProtocolMessageType('TransactionRefs', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONREFS,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.TransactionRefs)
  })
_sym_db.RegisterMessage(TransactionRefs)

UnclesHeaders = _reflection.GeneratedProtocolMessageType('UnclesHeaders', (_message.Message,), {
  'DESCRIPTOR' : _UNCLESHEADERS,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.UnclesHeaders)
  })
_sym_db.RegisterMessage(UnclesHeaders)

BlockRef = _reflection.GeneratedProtocolMessageType('BlockRef', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKREF,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.BlockRef)
  })
_sym_db.RegisterMessage(BlockRef)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEADER,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.BlockHeader)
  })
_sym_db.RegisterMessage(BlockHeader)

BigInt = _reflection.GeneratedProtocolMessageType('BigInt', (_message.Message,), {
  'DESCRIPTOR' : _BIGINT,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.BigInt)
  })
_sym_db.RegisterMessage(BigInt)

TransactionState = _reflection.GeneratedProtocolMessageType('TransactionState', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONSTATE,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.TransactionState)
  })
_sym_db.RegisterMessage(TransactionState)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

TransactionTrace = _reflection.GeneratedProtocolMessageType('TransactionTrace', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONTRACE,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.TransactionTrace)
  })
_sym_db.RegisterMessage(TransactionTrace)

TransactionTraceWithBlockRef = _reflection.GeneratedProtocolMessageType('TransactionTraceWithBlockRef', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONTRACEWITHBLOCKREF,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.TransactionTraceWithBlockRef)
  })
_sym_db.RegisterMessage(TransactionTraceWithBlockRef)

TransactionReceipt = _reflection.GeneratedProtocolMessageType('TransactionReceipt', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONRECEIPT,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.TransactionReceipt)
  })
_sym_db.RegisterMessage(TransactionReceipt)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), {
  'DESCRIPTOR' : _LOG,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.Log)
  })
_sym_db.RegisterMessage(Log)

Call = _reflection.GeneratedProtocolMessageType('Call', (_message.Message,), {

  'KeccakPreimagesEntry' : _reflection.GeneratedProtocolMessageType('KeccakPreimagesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CALL_KECCAKPREIMAGESENTRY,
    '__module__' : 'sfeth_codec_v1_pb2'
    # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.Call.KeccakPreimagesEntry)
    })
  ,
  'DESCRIPTOR' : _CALL,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.Call)
  })
_sym_db.RegisterMessage(Call)
_sym_db.RegisterMessage(Call.KeccakPreimagesEntry)

ERC20BalanceChange = _reflection.GeneratedProtocolMessageType('ERC20BalanceChange', (_message.Message,), {
  'DESCRIPTOR' : _ERC20BALANCECHANGE,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.ERC20BalanceChange)
  })
_sym_db.RegisterMessage(ERC20BalanceChange)

ERC20TransferEvent = _reflection.GeneratedProtocolMessageType('ERC20TransferEvent', (_message.Message,), {
  'DESCRIPTOR' : _ERC20TRANSFEREVENT,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.ERC20TransferEvent)
  })
_sym_db.RegisterMessage(ERC20TransferEvent)

StorageChange = _reflection.GeneratedProtocolMessageType('StorageChange', (_message.Message,), {
  'DESCRIPTOR' : _STORAGECHANGE,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.StorageChange)
  })
_sym_db.RegisterMessage(StorageChange)

BalanceChange = _reflection.GeneratedProtocolMessageType('BalanceChange', (_message.Message,), {
  'DESCRIPTOR' : _BALANCECHANGE,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.BalanceChange)
  })
_sym_db.RegisterMessage(BalanceChange)

NonceChange = _reflection.GeneratedProtocolMessageType('NonceChange', (_message.Message,), {
  'DESCRIPTOR' : _NONCECHANGE,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.NonceChange)
  })
_sym_db.RegisterMessage(NonceChange)

CodeChange = _reflection.GeneratedProtocolMessageType('CodeChange', (_message.Message,), {
  'DESCRIPTOR' : _CODECHANGE,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.CodeChange)
  })
_sym_db.RegisterMessage(CodeChange)

GasChange = _reflection.GeneratedProtocolMessageType('GasChange', (_message.Message,), {
  'DESCRIPTOR' : _GASCHANGE,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.GasChange)
  })
_sym_db.RegisterMessage(GasChange)

GasEvent = _reflection.GeneratedProtocolMessageType('GasEvent', (_message.Message,), {
  'DESCRIPTOR' : _GASEVENT,
  '__module__' : 'sfeth_codec_v1_pb2'
  # @@protoc_insertion_point(class_scope:sf.ethereum.codec.v1.GasEvent)
  })
_sym_db.RegisterMessage(GasEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/streamingfast/sf-ethereum/pb/sf/ethereum/codec/v1;pbcodec'
  _CALL_KECCAKPREIMAGESENTRY._options = None
  _CALL_KECCAKPREIMAGESENTRY._serialized_options = b'8\001'
  _TRANSACTIONTRACESTATUS._serialized_start=6353
  _TRANSACTIONTRACESTATUS._serialized_end=6431
  _CALLTYPE._serialized_start=6433
  _CALLTYPE._serialized_end=6522
  _BLOCK._serialized_start=80
  _BLOCK._serialized_end=537
  _HEADERONLYBLOCK._serialized_start=539
  _HEADERONLYBLOCK._serialized_end=607
  _BLOCKWITHREFS._serialized_start=610
  _BLOCKWITHREFS._serialized_end=774
  _TRANSACTIONREFS._serialized_start=776
  _TRANSACTIONREFS._serialized_end=809
  _UNCLESHEADERS._serialized_start=811
  _UNCLESHEADERS._serialized_end=877
  _BLOCKREF._serialized_start=879
  _BLOCKREF._serialized_end=919
  _BLOCKHEADER._serialized_start=922
  _BLOCKHEADER._serialized_end=1300
  _BIGINT._serialized_start=1302
  _BIGINT._serialized_end=1325
  _TRANSACTIONSTATE._serialized_start=1328
  _TRANSACTIONSTATE._serialized_end=2210
  _TRANSACTIONSTATE_TRANSITION._serialized_start=1967
  _TRANSACTIONSTATE_TRANSITION._serialized_end=2123
  _TRANSACTIONSTATE_STATE._serialized_start=2125
  _TRANSACTIONSTATE_STATE._serialized_end=2210
  _TRANSACTION._serialized_start=2213
  _TRANSACTION._serialized_end=2442
  _TRANSACTIONTRACE._serialized_start=2445
  _TRANSACTIONTRACE._serialized_end=2917
  _TRANSACTIONTRACEWITHBLOCKREF._serialized_start=2920
  _TRANSACTIONTRACEWITHBLOCKREF._serialized_end=3056
  _TRANSACTIONRECEIPT._serialized_start=3059
  _TRANSACTIONRECEIPT._serialized_end=3189
  _LOG._serialized_start=3191
  _LOG._serialized_end=3278
  _CALL._serialized_start=3281
  _CALL._serialized_end=4396
  _CALL_KECCAKPREIMAGESENTRY._serialized_start=4342
  _CALL_KECCAKPREIMAGESENTRY._serialized_end=4396
  _ERC20BALANCECHANGE._serialized_start=4399
  _ERC20BALANCECHANGE._serialized_end=4545
  _ERC20TRANSFEREVENT._serialized_start=4547
  _ERC20TRANSFEREVENT._serialized_end=4639
  _STORAGECHANGE._serialized_start=4641
  _STORAGECHANGE._serialized_end=4724
  _BALANCECHANGE._serialized_start=4727
  _BALANCECHANGE._serialized_end=5360
  _BALANCECHANGE_REASON._serialized_start=4920
  _BALANCECHANGE_REASON._serialized_end=5360
  _NONCECHANGE._serialized_start=5362
  _NONCECHANGE._serialized_end=5430
  _CODECHANGE._serialized_start=5432
  _CODECHANGE._serialized_end=5533
  _GASCHANGE._serialized_start=5536
  _GASCHANGE._serialized_end=6190
  _GASCHANGE_REASON._serialized_start=5644
  _GASCHANGE_REASON._serialized_end=6190
  _GASEVENT._serialized_start=6193
  _GASEVENT._serialized_end=6351
  _GASEVENT_ID._serialized_start=6292
  _GASEVENT_ID._serialized_end=6351
# @@protoc_insertion_point(module_scope)
