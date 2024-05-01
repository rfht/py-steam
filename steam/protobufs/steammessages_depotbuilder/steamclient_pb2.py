# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_depotbuilder.steamclient.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_base_pb2 as steammessages__base__pb2
from steammessages_unified_base import steamclient_pb2 as steammessages__unified__base_dot_steamclient__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,steammessages_depotbuilder.steamclient.proto\x1a\x18steammessages_base.proto\x1a,steammessages_unified_base.steamclient.proto\"\x8e\x01\n&CContentBuilder_InitDepotBuild_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x17\n\x0fworkshop_itemid\x18\x03 \x01(\x04\x12\x14\n\x0c\x66or_local_cs\x18\x04 \x01(\x08\x12\x15\n\rtarget_branch\x18\x05 \x01(\t\"\x88\x03\n\'CContentBuilder_InitDepotBuild_Response\x12\x1b\n\x13\x62\x61seline_manifestid\x18\x01 \x01(\x04\x12\x12\n\nchunk_size\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x65s_key\x18\x03 \x01(\x0c\x12\x0f\n\x07rsa_key\x18\x04 \x01(\x0c\x12\x10\n\x08url_host\x18\x05 \x01(\t\x12 \n\x18offset_detection_enabled\x18\x06 \x01(\x08\x12(\n offset_detection_min_clean_chunk\x18\x07 \x01(\r\x12)\n!offset_detection_blast_radius_pre\x18\x08 \x01(\r\x12*\n\"offset_detection_blast_radius_post\x18\t \x01(\r\x12)\n!offset_detection_max_distance_pre\x18\n \x01(\r\x12*\n\"offset_detection_max_distance_post\x18\x0b \x01(\r\"\xad\x01\n(CContentBuilder_StartDepotUpload_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x17\n\x0fworkshop_itemid\x18\x03 \x01(\x04\x12\x14\n\x0c\x66or_local_cs\x18\x04 \x01(\x08\x12\x1b\n\x13\x62\x61seline_manifestid\x18\x05 \x01(\x04\x12\x15\n\rmanifest_size\x18\x06 \x01(\r\"G\n)CContentBuilder_StartDepotUpload_Response\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x01 \x01(\x04\"Z\n-CContentBuilder_GetMissingDepotChunks_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x02 \x01(\x04\"\xd2\x01\n.CContentBuilder_GetMissingDepotChunks_Response\x12N\n\x0emissing_chunks\x18\x01 \x03(\x0b\x32\x36.CContentBuilder_GetMissingDepotChunks_Response.Chunks\x12\x1c\n\x14total_missing_chunks\x18\x02 \x01(\r\x12\x1b\n\x13total_missing_bytes\x18\x03 \x01(\x04\x1a\x15\n\x06\x43hunks\x12\x0b\n\x03sha\x18\x01 \x01(\x0c\"V\n)CContentBuilder_FinishDepotUpload_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x02 \x01(\x04\"U\n*CContentBuilder_FinishDepotUpload_Response\x12\x12\n\nmanifestid\x18\x01 \x01(\x04\x12\x13\n\x0bprev_reused\x18\x02 \x01(\x08\"\xd9\x01\n&CContentBuilder_CommitAppBuild_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12G\n\x0f\x64\x65pot_manifests\x18\x02 \x03(\x0b\x32..CContentBuilder_CommitAppBuild_Request.Depots\x12\x13\n\x0b\x62uild_notes\x18\x04 \x01(\t\x12\x13\n\x0blive_branch\x18\x05 \x01(\t\x1a-\n\x06\x44\x65pots\x12\x0f\n\x07\x64\x65potid\x18\x01 \x01(\r\x12\x12\n\nmanifestid\x18\x02 \x01(\x04\":\n\'CContentBuilder_CommitAppBuild_Response\x12\x0f\n\x07\x62uildid\x18\x01 \x01(\r\"c\n)CContentBuilder_SignInstallScript_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x16\n\x0einstall_script\x18\x03 \x01(\t\"K\n*CContentBuilder_SignInstallScript_Response\x12\x1d\n\x15signed_install_script\x18\x01 \x01(\t2\x9b\x05\n\x0e\x43ontentBuilder\x12\x63\n\x0eInitDepotBuild\x12\'.CContentBuilder_InitDepotBuild_Request\x1a(.CContentBuilder_InitDepotBuild_Response\x12i\n\x10StartDepotUpload\x12).CContentBuilder_StartDepotUpload_Request\x1a*.CContentBuilder_StartDepotUpload_Response\x12x\n\x15GetMissingDepotChunks\x12..CContentBuilder_GetMissingDepotChunks_Request\x1a/.CContentBuilder_GetMissingDepotChunks_Response\x12l\n\x11\x46inishDepotUpload\x12*.CContentBuilder_FinishDepotUpload_Request\x1a+.CContentBuilder_FinishDepotUpload_Response\x12\x63\n\x0e\x43ommitAppBuild\x12\'.CContentBuilder_CommitAppBuild_Request\x1a(.CContentBuilder_CommitAppBuild_Response\x12l\n\x11SignInstallScript\x12*.CContentBuilder_SignInstallScript_Request\x1a+.CContentBuilder_SignInstallScript_ResponseB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_depotbuilder.steamclient_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_CCONTENTBUILDER_INITDEPOTBUILD_REQUEST']._serialized_start=121
  _globals['_CCONTENTBUILDER_INITDEPOTBUILD_REQUEST']._serialized_end=263
  _globals['_CCONTENTBUILDER_INITDEPOTBUILD_RESPONSE']._serialized_start=266
  _globals['_CCONTENTBUILDER_INITDEPOTBUILD_RESPONSE']._serialized_end=658
  _globals['_CCONTENTBUILDER_STARTDEPOTUPLOAD_REQUEST']._serialized_start=661
  _globals['_CCONTENTBUILDER_STARTDEPOTUPLOAD_REQUEST']._serialized_end=834
  _globals['_CCONTENTBUILDER_STARTDEPOTUPLOAD_RESPONSE']._serialized_start=836
  _globals['_CCONTENTBUILDER_STARTDEPOTUPLOAD_RESPONSE']._serialized_end=907
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_REQUEST']._serialized_start=909
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_REQUEST']._serialized_end=999
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE']._serialized_start=1002
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE']._serialized_end=1212
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS']._serialized_start=1191
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS']._serialized_end=1212
  _globals['_CCONTENTBUILDER_FINISHDEPOTUPLOAD_REQUEST']._serialized_start=1214
  _globals['_CCONTENTBUILDER_FINISHDEPOTUPLOAD_REQUEST']._serialized_end=1300
  _globals['_CCONTENTBUILDER_FINISHDEPOTUPLOAD_RESPONSE']._serialized_start=1302
  _globals['_CCONTENTBUILDER_FINISHDEPOTUPLOAD_RESPONSE']._serialized_end=1387
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST']._serialized_start=1390
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST']._serialized_end=1607
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS']._serialized_start=1562
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS']._serialized_end=1607
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_RESPONSE']._serialized_start=1609
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_RESPONSE']._serialized_end=1667
  _globals['_CCONTENTBUILDER_SIGNINSTALLSCRIPT_REQUEST']._serialized_start=1669
  _globals['_CCONTENTBUILDER_SIGNINSTALLSCRIPT_REQUEST']._serialized_end=1768
  _globals['_CCONTENTBUILDER_SIGNINSTALLSCRIPT_RESPONSE']._serialized_start=1770
  _globals['_CCONTENTBUILDER_SIGNINSTALLSCRIPT_RESPONSE']._serialized_end=1845
  _globals['_CONTENTBUILDER']._serialized_start=1848
  _globals['_CONTENTBUILDER']._serialized_end=2515
# @@protoc_insertion_point(module_scope)
