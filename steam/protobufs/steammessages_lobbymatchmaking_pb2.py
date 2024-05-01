# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_lobbymatchmaking.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$steammessages_lobbymatchmaking.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\x9e\x01\n-LobbyMatchmakingLegacy_GetLobbyStatus_Request\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x15\n\rsteamid_lobby\x18\x02 \x01(\x06\x12\x17\n\x0f\x63laim_ownership\x18\x03 \x01(\x08\x12\x18\n\x10\x63laim_membership\x18\x04 \x01(\x08\x12\x13\n\x0bversion_num\x18\x05 \x01(\r\"\x93\x01\n.LobbyMatchmakingLegacy_GetLobbyStatus_Response\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x15\n\rsteamid_lobby\x18\x02 \x01(\x06\x12:\n\x0clobby_status\x18\x03 \x01(\x0e\x32\r.ELobbyStatus:\x15k_ELobbyStatusInvalid*\x81\x01\n\x0c\x45LobbyStatus\x12\x19\n\x15k_ELobbyStatusInvalid\x10\x00\x12\x18\n\x14k_ELobbyStatusExists\x10\x01\x12\x1e\n\x1ak_ELobbyStatusDoesNotExist\x10\x02\x12\x1c\n\x18k_ELobbyStatusNotAMember\x10\x03\x32\xc6\x01\n\x16LobbyMatchmakingLegacy\x12\x85\x01\n\x0eGetLobbyStatus\x12..LobbyMatchmakingLegacy_GetLobbyStatus_Request\x1a/.LobbyMatchmakingLegacy_GetLobbyStatus_Response\"\x12\x82\xb5\x18\x0eGetLobbyStatus\x1a$\x82\xb5\x18 Lobby matchmaking legacy serviceB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_lobbymatchmaking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_LOBBYMATCHMAKINGLEGACY']._loaded_options = None
  _globals['_LOBBYMATCHMAKINGLEGACY']._serialized_options = b'\202\265\030 Lobby matchmaking legacy service'
  _globals['_LOBBYMATCHMAKINGLEGACY'].methods_by_name['GetLobbyStatus']._loaded_options = None
  _globals['_LOBBYMATCHMAKINGLEGACY'].methods_by_name['GetLobbyStatus']._serialized_options = b'\202\265\030\016GetLobbyStatus'
  _globals['_ELOBBYSTATUS']._serialized_start=412
  _globals['_ELOBBYSTATUS']._serialized_end=541
  _globals['_LOBBYMATCHMAKINGLEGACY_GETLOBBYSTATUS_REQUEST']._serialized_start=101
  _globals['_LOBBYMATCHMAKINGLEGACY_GETLOBBYSTATUS_REQUEST']._serialized_end=259
  _globals['_LOBBYMATCHMAKINGLEGACY_GETLOBBYSTATUS_RESPONSE']._serialized_start=262
  _globals['_LOBBYMATCHMAKINGLEGACY_GETLOBBYSTATUS_RESPONSE']._serialized_end=409
  _globals['_LOBBYMATCHMAKINGLEGACY']._serialized_start=544
  _globals['_LOBBYMATCHMAKINGLEGACY']._serialized_end=742
_builder.BuildServices(DESCRIPTOR, 'steammessages_lobbymatchmaking_pb2', _globals)
# @@protoc_insertion_point(module_scope)
