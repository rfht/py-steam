# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_depotbuilder.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_base_pb2 as steammessages__base__pb2
import steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n steammessages_depotbuilder.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\x8e\x01\n&CContentBuilder_InitDepotBuild_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x17\n\x0fworkshop_itemid\x18\x03 \x01(\x04\x12\x14\n\x0c\x66or_local_cs\x18\x04 \x01(\x08\x12\x15\n\rtarget_branch\x18\x05 \x01(\t\"\x88\x03\n\'CContentBuilder_InitDepotBuild_Response\x12\x1b\n\x13\x62\x61seline_manifestid\x18\x01 \x01(\x04\x12\x12\n\nchunk_size\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x65s_key\x18\x03 \x01(\x0c\x12\x0f\n\x07rsa_key\x18\x04 \x01(\x0c\x12\x10\n\x08url_host\x18\x05 \x01(\t\x12 \n\x18offset_detection_enabled\x18\x06 \x01(\x08\x12(\n offset_detection_min_clean_chunk\x18\x07 \x01(\r\x12)\n!offset_detection_blast_radius_pre\x18\x08 \x01(\r\x12*\n\"offset_detection_blast_radius_post\x18\t \x01(\r\x12)\n!offset_detection_max_distance_pre\x18\n \x01(\r\x12*\n\"offset_detection_max_distance_post\x18\x0b \x01(\r\"\xad\x01\n(CContentBuilder_StartDepotUpload_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x17\n\x0fworkshop_itemid\x18\x03 \x01(\x04\x12\x14\n\x0c\x66or_local_cs\x18\x04 \x01(\x08\x12\x1b\n\x13\x62\x61seline_manifestid\x18\x05 \x01(\x04\x12\x15\n\rmanifest_size\x18\x06 \x01(\r\"G\n)CContentBuilder_StartDepotUpload_Response\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x01 \x01(\x04\"Z\n-CContentBuilder_GetMissingDepotChunks_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x02 \x01(\x04\"\xd2\x01\n.CContentBuilder_GetMissingDepotChunks_Response\x12N\n\x0emissing_chunks\x18\x01 \x03(\x0b\x32\x36.CContentBuilder_GetMissingDepotChunks_Response.Chunks\x12\x1c\n\x14total_missing_chunks\x18\x02 \x01(\r\x12\x1b\n\x13total_missing_bytes\x18\x03 \x01(\x04\x1a\x15\n\x06\x43hunks\x12\x0b\n\x03sha\x18\x01 \x01(\x0c\"V\n)CContentBuilder_FinishDepotUpload_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x02 \x01(\x04\"U\n*CContentBuilder_FinishDepotUpload_Response\x12\x12\n\nmanifestid\x18\x01 \x01(\x04\x12\x13\n\x0bprev_reused\x18\x02 \x01(\x08\"\xd9\x01\n&CContentBuilder_CommitAppBuild_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12G\n\x0f\x64\x65pot_manifests\x18\x02 \x03(\x0b\x32..CContentBuilder_CommitAppBuild_Request.Depots\x12\x13\n\x0b\x62uild_notes\x18\x04 \x01(\t\x12\x13\n\x0blive_branch\x18\x05 \x01(\t\x1a-\n\x06\x44\x65pots\x12\x0f\n\x07\x64\x65potid\x18\x01 \x01(\r\x12\x12\n\nmanifestid\x18\x02 \x01(\x04\":\n\'CContentBuilder_CommitAppBuild_Response\x12\x0f\n\x07\x62uildid\x18\x01 \x01(\r\"c\n)CContentBuilder_SignInstallScript_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x16\n\x0einstall_script\x18\x03 \x01(\t\"K\n*CContentBuilder_SignInstallScript_Response\x12\x1d\n\x15signed_install_script\x18\x01 \x01(\t2\x92\x08\n\x0e\x43ontentBuilder\x12\x98\x01\n\x0eInitDepotBuild\x12\'.CContentBuilder_InitDepotBuild_Request\x1a(.CContentBuilder_InitDepotBuild_Response\"3\x82\xb5\x18/Get inital parameters to start building a depot\x12\x9e\x01\n\x10StartDepotUpload\x12).CContentBuilder_StartDepotUpload_Request\x1a*.CContentBuilder_StartDepotUpload_Response\"3\x82\xb5\x18/Start uploading manifest and chunks for a depot\x12\xa9\x01\n\x15GetMissingDepotChunks\x12..CContentBuilder_GetMissingDepotChunks_Request\x1a/.CContentBuilder_GetMissingDepotChunks_Response\"/\x82\xb5\x18+Get list of missing chunks for depot upload\x12\xb1\x01\n\x11\x46inishDepotUpload\x12*.CContentBuilder_FinishDepotUpload_Request\x1a+.CContentBuilder_FinishDepotUpload_Response\"C\x82\xb5\x18?Commit a depot build after manifest and all chunks are uploaded\x12\xa7\x01\n\x0e\x43ommitAppBuild\x12\'.CContentBuilder_CommitAppBuild_Request\x1a(.CContentBuilder_CommitAppBuild_Response\"B\x82\xb5\x18>Combine previous depot uploads into an app build and commit it\x12\x88\x01\n\x11SignInstallScript\x12*.CContentBuilder_SignInstallScript_Request\x1a+.CContentBuilder_SignInstallScript_Response\"\x1a\x82\xb5\x18\x16Sign an install script\x1a/\x82\xb5\x18+Interface to build and upload depot contentB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_depotbuilder_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CONTENTBUILDER']._loaded_options = None
  _globals['_CONTENTBUILDER']._serialized_options = b'\202\265\030+Interface to build and upload depot content'
  _globals['_CONTENTBUILDER'].methods_by_name['InitDepotBuild']._loaded_options = None
  _globals['_CONTENTBUILDER'].methods_by_name['InitDepotBuild']._serialized_options = b'\202\265\030/Get inital parameters to start building a depot'
  _globals['_CONTENTBUILDER'].methods_by_name['StartDepotUpload']._loaded_options = None
  _globals['_CONTENTBUILDER'].methods_by_name['StartDepotUpload']._serialized_options = b'\202\265\030/Start uploading manifest and chunks for a depot'
  _globals['_CONTENTBUILDER'].methods_by_name['GetMissingDepotChunks']._loaded_options = None
  _globals['_CONTENTBUILDER'].methods_by_name['GetMissingDepotChunks']._serialized_options = b'\202\265\030+Get list of missing chunks for depot upload'
  _globals['_CONTENTBUILDER'].methods_by_name['FinishDepotUpload']._loaded_options = None
  _globals['_CONTENTBUILDER'].methods_by_name['FinishDepotUpload']._serialized_options = b'\202\265\030?Commit a depot build after manifest and all chunks are uploaded'
  _globals['_CONTENTBUILDER'].methods_by_name['CommitAppBuild']._loaded_options = None
  _globals['_CONTENTBUILDER'].methods_by_name['CommitAppBuild']._serialized_options = b'\202\265\030>Combine previous depot uploads into an app build and commit it'
  _globals['_CONTENTBUILDER'].methods_by_name['SignInstallScript']._loaded_options = None
  _globals['_CONTENTBUILDER'].methods_by_name['SignInstallScript']._serialized_options = b'\202\265\030\026Sign an install script'
  _globals['_CCONTENTBUILDER_INITDEPOTBUILD_REQUEST']._serialized_start=97
  _globals['_CCONTENTBUILDER_INITDEPOTBUILD_REQUEST']._serialized_end=239
  _globals['_CCONTENTBUILDER_INITDEPOTBUILD_RESPONSE']._serialized_start=242
  _globals['_CCONTENTBUILDER_INITDEPOTBUILD_RESPONSE']._serialized_end=634
  _globals['_CCONTENTBUILDER_STARTDEPOTUPLOAD_REQUEST']._serialized_start=637
  _globals['_CCONTENTBUILDER_STARTDEPOTUPLOAD_REQUEST']._serialized_end=810
  _globals['_CCONTENTBUILDER_STARTDEPOTUPLOAD_RESPONSE']._serialized_start=812
  _globals['_CCONTENTBUILDER_STARTDEPOTUPLOAD_RESPONSE']._serialized_end=883
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_REQUEST']._serialized_start=885
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_REQUEST']._serialized_end=975
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE']._serialized_start=978
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE']._serialized_end=1188
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS']._serialized_start=1167
  _globals['_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS']._serialized_end=1188
  _globals['_CCONTENTBUILDER_FINISHDEPOTUPLOAD_REQUEST']._serialized_start=1190
  _globals['_CCONTENTBUILDER_FINISHDEPOTUPLOAD_REQUEST']._serialized_end=1276
  _globals['_CCONTENTBUILDER_FINISHDEPOTUPLOAD_RESPONSE']._serialized_start=1278
  _globals['_CCONTENTBUILDER_FINISHDEPOTUPLOAD_RESPONSE']._serialized_end=1363
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST']._serialized_start=1366
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST']._serialized_end=1583
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS']._serialized_start=1538
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS']._serialized_end=1583
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_RESPONSE']._serialized_start=1585
  _globals['_CCONTENTBUILDER_COMMITAPPBUILD_RESPONSE']._serialized_end=1643
  _globals['_CCONTENTBUILDER_SIGNINSTALLSCRIPT_REQUEST']._serialized_start=1645
  _globals['_CCONTENTBUILDER_SIGNINSTALLSCRIPT_REQUEST']._serialized_end=1744
  _globals['_CCONTENTBUILDER_SIGNINSTALLSCRIPT_RESPONSE']._serialized_start=1746
  _globals['_CCONTENTBUILDER_SIGNINSTALLSCRIPT_RESPONSE']._serialized_end=1821
  _globals['_CONTENTBUILDER']._serialized_start=1824
  _globals['_CONTENTBUILDER']._serialized_end=2866
_builder.BuildServices(DESCRIPTOR, 'steammessages_depotbuilder_pb2', _globals)
# @@protoc_insertion_point(module_scope)
