# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_clientserver_lbs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$steammessages_clientserver_lbs.proto\x1a\x18steammessages_base.proto\"|\n\x15\x43MsgClientLBSSetScore\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x16\n\x0eleaderboard_id\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x05\x12\x0f\n\x07\x64\x65tails\x18\x04 \x01(\x0c\x12\x1b\n\x13upload_score_method\x18\x05 \x01(\x05\"\xa2\x01\n\x1d\x43MsgClientLBSSetScoreResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x1f\n\x17leaderboard_entry_count\x18\x02 \x01(\x05\x12\x15\n\rscore_changed\x18\x03 \x01(\x08\x12\x1c\n\x14global_rank_previous\x18\x04 \x01(\x05\x12\x17\n\x0fglobal_rank_new\x18\x05 \x01(\x05\"M\n\x13\x43MsgClientLBSSetUGC\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x16\n\x0eleaderboard_id\x18\x02 \x01(\x05\x12\x0e\n\x06ugc_id\x18\x03 \x01(\x06\"1\n\x1b\x43MsgClientLBSSetUGCResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"\xa7\x01\n\x1b\x43MsgClientLBSFindOrCreateLB\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x1f\n\x17leaderboard_sort_method\x18\x02 \x01(\x05\x12 \n\x18leaderboard_display_type\x18\x03 \x01(\x05\x12\x1b\n\x13\x63reate_if_not_found\x18\x04 \x01(\x08\x12\x18\n\x10leaderboard_name\x18\x05 \x01(\t\"\xd5\x01\n#CMsgClientLBSFindOrCreateLBResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x16\n\x0eleaderboard_id\x18\x02 \x01(\x05\x12\x1f\n\x17leaderboard_entry_count\x18\x03 \x01(\x05\x12\"\n\x17leaderboard_sort_method\x18\x04 \x01(\x05:\x01\x30\x12#\n\x18leaderboard_display_type\x18\x05 \x01(\x05:\x01\x30\x12\x18\n\x10leaderboard_name\x18\x06 \x01(\t\"\x9f\x01\n\x19\x43MsgClientLBSGetLBEntries\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x05\x12\x16\n\x0eleaderboard_id\x18\x02 \x01(\x05\x12\x13\n\x0brange_start\x18\x03 \x01(\x05\x12\x11\n\trange_end\x18\x04 \x01(\x05\x12 \n\x18leaderboard_data_request\x18\x05 \x01(\x05\x12\x10\n\x08steamids\x18\x06 \x03(\x06\"\xf8\x01\n!CMsgClientLBSGetLBEntriesResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x1f\n\x17leaderboard_entry_count\x18\x02 \x01(\x05\x12\x39\n\x07\x65ntries\x18\x03 \x03(\x0b\x32(.CMsgClientLBSGetLBEntriesResponse.Entry\x1a\x63\n\x05\x45ntry\x12\x15\n\rsteam_id_user\x18\x01 \x01(\x06\x12\x13\n\x0bglobal_rank\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x05\x12\x0f\n\x07\x64\x65tails\x18\x04 \x01(\x0c\x12\x0e\n\x06ugc_id\x18\x05 \x01(\x06\x42\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientserver_lbs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGCLIENTLBSSETSCORE']._serialized_start=66
  _globals['_CMSGCLIENTLBSSETSCORE']._serialized_end=190
  _globals['_CMSGCLIENTLBSSETSCORERESPONSE']._serialized_start=193
  _globals['_CMSGCLIENTLBSSETSCORERESPONSE']._serialized_end=355
  _globals['_CMSGCLIENTLBSSETUGC']._serialized_start=357
  _globals['_CMSGCLIENTLBSSETUGC']._serialized_end=434
  _globals['_CMSGCLIENTLBSSETUGCRESPONSE']._serialized_start=436
  _globals['_CMSGCLIENTLBSSETUGCRESPONSE']._serialized_end=485
  _globals['_CMSGCLIENTLBSFINDORCREATELB']._serialized_start=488
  _globals['_CMSGCLIENTLBSFINDORCREATELB']._serialized_end=655
  _globals['_CMSGCLIENTLBSFINDORCREATELBRESPONSE']._serialized_start=658
  _globals['_CMSGCLIENTLBSFINDORCREATELBRESPONSE']._serialized_end=871
  _globals['_CMSGCLIENTLBSGETLBENTRIES']._serialized_start=874
  _globals['_CMSGCLIENTLBSGETLBENTRIES']._serialized_end=1033
  _globals['_CMSGCLIENTLBSGETLBENTRIESRESPONSE']._serialized_start=1036
  _globals['_CMSGCLIENTLBSGETLBENTRIESRESPONSE']._serialized_end=1284
  _globals['_CMSGCLIENTLBSGETLBENTRIESRESPONSE_ENTRY']._serialized_start=1185
  _globals['_CMSGCLIENTLBSGETLBENTRIESRESPONSE_ENTRY']._serialized_end=1284
# @@protoc_insertion_point(module_scope)
