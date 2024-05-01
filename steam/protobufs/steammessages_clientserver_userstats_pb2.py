# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_clientserver_userstats.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*steammessages_clientserver_userstats.proto\x1a\x18steammessages_base.proto\"u\n\x16\x43MsgClientGetUserStats\x12\x0f\n\x07game_id\x18\x01 \x01(\x06\x12\x11\n\tcrc_stats\x18\x02 \x01(\r\x12\x1c\n\x14schema_local_version\x18\x03 \x01(\x05\x12\x19\n\x11steam_id_for_user\x18\x04 \x01(\x06\"\xdf\x02\n\x1e\x43MsgClientGetUserStatsResponse\x12\x0f\n\x07game_id\x18\x01 \x01(\x06\x12\x12\n\x07\x65result\x18\x02 \x01(\x05:\x01\x32\x12\x11\n\tcrc_stats\x18\x03 \x01(\r\x12\x0e\n\x06schema\x18\x04 \x01(\x0c\x12\x34\n\x05stats\x18\x05 \x03(\x0b\x32%.CMsgClientGetUserStatsResponse.Stats\x12N\n\x12\x61\x63hievement_blocks\x18\x06 \x03(\x0b\x32\x32.CMsgClientGetUserStatsResponse.Achievement_Blocks\x1a,\n\x05Stats\x12\x0f\n\x07stat_id\x18\x01 \x01(\r\x12\x12\n\nstat_value\x18\x02 \x01(\r\x1a\x41\n\x12\x41\x63hievement_Blocks\x12\x16\n\x0e\x61\x63hievement_id\x18\x01 \x01(\r\x12\x13\n\x0bunlock_time\x18\x02 \x03(\x07\"\x9a\x02\n CMsgClientStoreUserStatsResponse\x12\x0f\n\x07game_id\x18\x01 \x01(\x06\x12\x12\n\x07\x65result\x18\x02 \x01(\x05:\x01\x32\x12\x11\n\tcrc_stats\x18\x03 \x01(\r\x12Z\n\x17stats_failed_validation\x18\x04 \x03(\x0b\x32\x39.CMsgClientStoreUserStatsResponse.Stats_Failed_Validation\x12\x19\n\x11stats_out_of_date\x18\x05 \x01(\x08\x1aG\n\x17Stats_Failed_Validation\x12\x0f\n\x07stat_id\x18\x01 \x01(\r\x12\x1b\n\x13reverted_stat_value\x18\x02 \x01(\r\"\xe8\x01\n\x19\x43MsgClientStoreUserStats2\x12\x0f\n\x07game_id\x18\x01 \x01(\x06\x12\x17\n\x0fsettor_steam_id\x18\x02 \x01(\x06\x12\x17\n\x0fsettee_steam_id\x18\x03 \x01(\x06\x12\x11\n\tcrc_stats\x18\x04 \x01(\r\x12\x16\n\x0e\x65xplicit_reset\x18\x05 \x01(\x08\x12/\n\x05stats\x18\x06 \x03(\x0b\x32 .CMsgClientStoreUserStats2.Stats\x1a,\n\x05Stats\x12\x0f\n\x07stat_id\x18\x01 \x01(\r\x12\x12\n\nstat_value\x18\x02 \x01(\r\"\xc2\x01\n\x16\x43MsgClientStatsUpdated\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x0f\n\x07game_id\x18\x02 \x01(\x06\x12\x11\n\tcrc_stats\x18\x03 \x01(\r\x12<\n\rupdated_stats\x18\x04 \x03(\x0b\x32%.CMsgClientStatsUpdated.Updated_Stats\x1a\x34\n\rUpdated_Stats\x12\x0f\n\x07stat_id\x18\x01 \x01(\r\x12\x12\n\nstat_value\x18\x02 \x01(\r\"\xbc\x01\n\x18\x43MsgClientStoreUserStats\x12\x0f\n\x07game_id\x18\x01 \x01(\x06\x12\x16\n\x0e\x65xplicit_reset\x18\x02 \x01(\x08\x12@\n\x0estats_to_store\x18\x03 \x03(\x0b\x32(.CMsgClientStoreUserStats.Stats_To_Store\x1a\x35\n\x0eStats_To_Store\x12\x0f\n\x07stat_id\x18\x01 \x01(\r\x12\x12\n\nstat_value\x18\x02 \x01(\rB\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientserver_userstats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGCLIENTGETUSERSTATS']._serialized_start=72
  _globals['_CMSGCLIENTGETUSERSTATS']._serialized_end=189
  _globals['_CMSGCLIENTGETUSERSTATSRESPONSE']._serialized_start=192
  _globals['_CMSGCLIENTGETUSERSTATSRESPONSE']._serialized_end=543
  _globals['_CMSGCLIENTGETUSERSTATSRESPONSE_STATS']._serialized_start=432
  _globals['_CMSGCLIENTGETUSERSTATSRESPONSE_STATS']._serialized_end=476
  _globals['_CMSGCLIENTGETUSERSTATSRESPONSE_ACHIEVEMENT_BLOCKS']._serialized_start=478
  _globals['_CMSGCLIENTGETUSERSTATSRESPONSE_ACHIEVEMENT_BLOCKS']._serialized_end=543
  _globals['_CMSGCLIENTSTOREUSERSTATSRESPONSE']._serialized_start=546
  _globals['_CMSGCLIENTSTOREUSERSTATSRESPONSE']._serialized_end=828
  _globals['_CMSGCLIENTSTOREUSERSTATSRESPONSE_STATS_FAILED_VALIDATION']._serialized_start=757
  _globals['_CMSGCLIENTSTOREUSERSTATSRESPONSE_STATS_FAILED_VALIDATION']._serialized_end=828
  _globals['_CMSGCLIENTSTOREUSERSTATS2']._serialized_start=831
  _globals['_CMSGCLIENTSTOREUSERSTATS2']._serialized_end=1063
  _globals['_CMSGCLIENTSTOREUSERSTATS2_STATS']._serialized_start=432
  _globals['_CMSGCLIENTSTOREUSERSTATS2_STATS']._serialized_end=476
  _globals['_CMSGCLIENTSTATSUPDATED']._serialized_start=1066
  _globals['_CMSGCLIENTSTATSUPDATED']._serialized_end=1260
  _globals['_CMSGCLIENTSTATSUPDATED_UPDATED_STATS']._serialized_start=1208
  _globals['_CMSGCLIENTSTATSUPDATED_UPDATED_STATS']._serialized_end=1260
  _globals['_CMSGCLIENTSTOREUSERSTATS']._serialized_start=1263
  _globals['_CMSGCLIENTSTOREUSERSTATS']._serialized_end=1451
  _globals['_CMSGCLIENTSTOREUSERSTATS_STATS_TO_STORE']._serialized_start=1398
  _globals['_CMSGCLIENTSTOREUSERSTATS_STATS_TO_STORE']._serialized_end=1451
# @@protoc_insertion_point(module_scope)
