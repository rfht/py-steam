# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_vac.steamclient.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#steammessages_vac.steamclient.proto\x1a\x18steammessages_base.proto\x1a,steammessages_unified_base.steamclient.proto\"\xec\x01\n(CFileVerification_SignatureCheck_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x11\n\tfile_size\x18\x03 \x01(\x04\x12\x16\n\x0e\x66ile_timestamp\x18\x04 \x01(\r\x12\x17\n\x0f\x66ile_timestamp2\x18\x05 \x01(\r\x12\x18\n\x10signature_result\x18\x06 \x01(\r\x12\x10\n\x08\x66ilename\x18\x07 \x01(\t\x12\x1e\n\x16\x63lient_package_version\x18\x08 \x01(\r\x12\x10\n\x08sha1hash\x18\t \x01(\x0c\"C\n)CFileVerification_SignatureCheck_Response\x12\x16\n\x0e\x64\x65ny_operation\x18\x01 \x01(\x08\"\xa5\x01\n+CFileVerification_SteamServiceCheck_Request\x12\x16\n\x0eservice_status\x18\x02 \x01(\r\x12\x1e\n\x16\x63lient_package_version\x18\x03 \x01(\r\x12\x15\n\rlauncher_type\x18\x04 \x01(\r\x12\x0f\n\x07os_type\x18\x05 \x01(\r\x12\x16\n\x0eservice_repair\x18\x06 \x01(\r\"F\n,CFileVerification_SteamServiceCheck_Response\x12\x16\n\x0e\x61ttempt_repair\x18\x01 \x01(\x08\x32\xed\x01\n\x10\x46ileVerification\x12g\n\x0eSignatureCheck\x12).CFileVerification_SignatureCheck_Request\x1a*.CFileVerification_SignatureCheck_Response\x12p\n\x11SteamServiceCheck\x12,.CFileVerification_SteamServiceCheck_Request\x1a-.CFileVerification_SteamServiceCheck_ResponseB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_vac.steamclient_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_CFILEVERIFICATION_SIGNATURECHECK_REQUEST']._serialized_start=112
  _globals['_CFILEVERIFICATION_SIGNATURECHECK_REQUEST']._serialized_end=348
  _globals['_CFILEVERIFICATION_SIGNATURECHECK_RESPONSE']._serialized_start=350
  _globals['_CFILEVERIFICATION_SIGNATURECHECK_RESPONSE']._serialized_end=417
  _globals['_CFILEVERIFICATION_STEAMSERVICECHECK_REQUEST']._serialized_start=420
  _globals['_CFILEVERIFICATION_STEAMSERVICECHECK_REQUEST']._serialized_end=585
  _globals['_CFILEVERIFICATION_STEAMSERVICECHECK_RESPONSE']._serialized_start=587
  _globals['_CFILEVERIFICATION_STEAMSERVICECHECK_RESPONSE']._serialized_end=657
  _globals['_FILEVERIFICATION']._serialized_start=660
  _globals['_FILEVERIFICATION']._serialized_end=897
# @@protoc_insertion_point(module_scope)
