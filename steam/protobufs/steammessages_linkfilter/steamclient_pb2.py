# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_linkfilter.steamclient.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
from steam.protobufs.steammessages_unified_base import steamclient_pb2 as steammessages__unified__base_dot_steamclient__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*steammessages_linkfilter.steamclient.proto\x1a\x18steammessages_base.proto\x1a,steammessages_unified_base.steamclient.proto\"^\n,CCommunity_GetLinkFilterHashPrefixes_Request\x12\x10\n\x08hit_type\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12\r\n\x05start\x18\x03 \x01(\x04\"F\n-CCommunity_GetLinkFilterHashPrefixes_Response\x12\x15\n\rhash_prefixes\x18\x01 \x03(\r\"X\n&CCommunity_GetLinkFilterHashes_Request\x12\x10\n\x08hit_type\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12\r\n\x05start\x18\x03 \x01(\x04\"9\n\'CCommunity_GetLinkFilterHashes_Response\x12\x0e\n\x06hashes\x18\x01 \x03(\x0c\"?\n+CCommunity_GetLinkFilterListVersion_Request\x12\x10\n\x08hit_type\x18\x01 \x01(\r\"N\n,CCommunity_GetLinkFilterListVersion_Response\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\x32\xf4\x02\n\x13\x43ommunityLinkFilter\x12z\n\x19GetLinkFilterHashPrefixes\x12-.CCommunity_GetLinkFilterHashPrefixes_Request\x1a..CCommunity_GetLinkFilterHashPrefixes_Response\x12h\n\x13GetLinkFilterHashes\x12\'.CCommunity_GetLinkFilterHashes_Request\x1a(.CCommunity_GetLinkFilterHashes_Response\x12w\n\x18GetLinkFilterListVersion\x12,.CCommunity_GetLinkFilterListVersion_Request\x1a-.CCommunity_GetLinkFilterListVersion_ResponseB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_linkfilter.steamclient_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST']._serialized_start=118
  _globals['_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST']._serialized_end=212
  _globals['_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_RESPONSE']._serialized_start=214
  _globals['_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_RESPONSE']._serialized_end=284
  _globals['_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST']._serialized_start=286
  _globals['_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST']._serialized_end=374
  _globals['_CCOMMUNITY_GETLINKFILTERHASHES_RESPONSE']._serialized_start=376
  _globals['_CCOMMUNITY_GETLINKFILTERHASHES_RESPONSE']._serialized_end=433
  _globals['_CCOMMUNITY_GETLINKFILTERLISTVERSION_REQUEST']._serialized_start=435
  _globals['_CCOMMUNITY_GETLINKFILTERLISTVERSION_REQUEST']._serialized_end=498
  _globals['_CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE']._serialized_start=500
  _globals['_CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE']._serialized_end=578
  _globals['_COMMUNITYLINKFILTER']._serialized_start=581
  _globals['_COMMUNITYLINKFILTER']._serialized_end=953
# @@protoc_insertion_point(module_scope)
