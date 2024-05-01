# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_offline.steamclient.proto
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
import steam.protobufs.offline_ticket_pb2 as offline__ticket__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'steammessages_offline.steamclient.proto\x1a\x18steammessages_base.proto\x1a,steammessages_unified_base.steamclient.proto\x1a\x14offline_ticket.proto\"V\n&COffline_GetOfflineLogonTicket_Request\x12\x10\n\x08priority\x18\x01 \x01(\r\x12\x1a\n\x12perform_encryption\x18\x02 \x01(\x08\"\x82\x01\n\'COffline_GetOfflineLogonTicket_Response\x12\x19\n\x11serialized_ticket\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12)\n\x10\x65ncrypted_ticket\x18\x03 \x01(\x0b\x32\x0f.Offline_Ticket\"0\n.COffline_GetUnsignedOfflineLogonTicket_Request\"O\n\x1b\x43Offline_OfflineLogonTicket\x12\x11\n\taccountid\x18\x01 \x01(\r\x12\x1d\n\x15rtime32_creation_time\x18\x02 \x01(\x07\"_\n/COffline_GetUnsignedOfflineLogonTicket_Response\x12,\n\x06ticket\x18\x01 \x01(\x0b\x32\x1c.COffline_OfflineLogonTicket2\xfa\x01\n\x07Offline\x12j\n\x15GetOfflineLogonTicket\x12\'.COffline_GetOfflineLogonTicket_Request\x1a(.COffline_GetOfflineLogonTicket_Response\x12\x82\x01\n\x1dGetUnsignedOfflineLogonTicket\x12/.COffline_GetUnsignedOfflineLogonTicket_Request\x1a\x30.COffline_GetUnsignedOfflineLogonTicket_ResponseB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_offline.steamclient_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_COFFLINE_GETOFFLINELOGONTICKET_REQUEST']._serialized_start=137
  _globals['_COFFLINE_GETOFFLINELOGONTICKET_REQUEST']._serialized_end=223
  _globals['_COFFLINE_GETOFFLINELOGONTICKET_RESPONSE']._serialized_start=226
  _globals['_COFFLINE_GETOFFLINELOGONTICKET_RESPONSE']._serialized_end=356
  _globals['_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_REQUEST']._serialized_start=358
  _globals['_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_REQUEST']._serialized_end=406
  _globals['_COFFLINE_OFFLINELOGONTICKET']._serialized_start=408
  _globals['_COFFLINE_OFFLINELOGONTICKET']._serialized_end=487
  _globals['_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_RESPONSE']._serialized_start=489
  _globals['_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_RESPONSE']._serialized_end=584
  _globals['_OFFLINE']._serialized_start=587
  _globals['_OFFLINE']._serialized_end=837
# @@protoc_insertion_point(module_scope)
