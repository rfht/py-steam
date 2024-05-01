# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: webuimessages_gamescope.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.enums_pb2 as enums__pb2
import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.webuimessages_base_pb2 as webuimessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwebuimessages_gamescope.proto\x1a\x0b\x65nums.proto\x1a\x18steammessages_base.proto\x1a\x18webuimessages_base.proto\"\xcb\x01\n\x0f\x43MsgDisplayInfo\x12\x0c\n\x04make\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x16\n\x0e\x63onnector_name\x18\x03 \x01(\t\x12\x1f\n\x17supported_refresh_rates\x18\x04 \x03(\x05\x12\x1d\n\x15supported_frame_rates\x18\x05 \x03(\x05\x12\x13\n\x0bis_external\x18\x06 \x01(\x08\x12\x16\n\x0eis_hdr_capable\x18\x07 \x01(\x08\x12\x16\n\x0eis_vrr_capable\x18\x08 \x01(\x08\"\x90\x03\n\x12\x43MsgGamescopeState\x12\x1c\n\x14is_service_available\x18\x01 \x01(\x08\x12\x1c\n\x14is_reshade_supported\x18\x02 \x01(\x08\x12\x1a\n\x12is_app_hdr_enabled\x18\x03 \x01(\x08\x12%\n\x1dis_app_refresh_rate_supported\x18\x04 \x01(\x08\x12-\n\x13\x61\x63tive_display_info\x18\x05 \x01(\x0b\x32\x10.CMsgDisplayInfo\x12#\n\x1bis_app_refresh_rate_capable\x18\x06 \x01(\x08\x12+\n#is_refresh_rate_switching_supported\x18\x07 \x01(\x08\x12,\n$is_refresh_rate_switching_restricted\x18\x08 \x01(\x08\x12&\n\x1eis_hdr_visualization_supported\x18\t \x01(\x08\x12$\n\x1cis_mura_correction_supported\x18\n \x01(\x08\"\x1d\n\x1b\x43Gamescope_GetState_Request\"B\n\x1c\x43Gamescope_GetState_Response\x12\"\n\x05state\x18\x01 \x01(\x0b\x32\x13.CMsgGamescopeState\"&\n$CGamescope_StateChanged_Notification\"\x8e\x01\n CGamescope_SetBlurParams_Request\x12@\n\x04mode\x18\x01 \x01(\x0e\x32\x13.EGamescopeBlurMode:\x1dk_EGamescopeBlurMode_Disabled\x12\x0e\n\x06radius\x18\x02 \x01(\x05\x12\x18\n\x10\x66\x61\x64\x65_duration_ms\x18\x03 \x01(\x05\"#\n!CGamescope_SetBlurParams_Response2\x81\x02\n\tGamescope\x12G\n\x08GetState\x12\x1c.CGamescope_GetState_Request\x1a\x1d.CGamescope_GetState_Response\x12M\n\x12NotifyStateChanged\x12%.CGamescope_StateChanged_Notification\x1a\x10.WebUINoResponse\x12V\n\rSetBlurParams\x12!.CGamescope_SetBlurParams_Request\x1a\".CGamescope_SetBlurParams_Response\x1a\x04\x80\x97\"\x01\x42\x05H\x01\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webuimessages_gamescope_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\200\001\001'
  _globals['_GAMESCOPE']._loaded_options = None
  _globals['_GAMESCOPE']._serialized_options = b'\200\227\"\001'
  _globals['_CMSGDISPLAYINFO']._serialized_start=99
  _globals['_CMSGDISPLAYINFO']._serialized_end=302
  _globals['_CMSGGAMESCOPESTATE']._serialized_start=305
  _globals['_CMSGGAMESCOPESTATE']._serialized_end=705
  _globals['_CGAMESCOPE_GETSTATE_REQUEST']._serialized_start=707
  _globals['_CGAMESCOPE_GETSTATE_REQUEST']._serialized_end=736
  _globals['_CGAMESCOPE_GETSTATE_RESPONSE']._serialized_start=738
  _globals['_CGAMESCOPE_GETSTATE_RESPONSE']._serialized_end=804
  _globals['_CGAMESCOPE_STATECHANGED_NOTIFICATION']._serialized_start=806
  _globals['_CGAMESCOPE_STATECHANGED_NOTIFICATION']._serialized_end=844
  _globals['_CGAMESCOPE_SETBLURPARAMS_REQUEST']._serialized_start=847
  _globals['_CGAMESCOPE_SETBLURPARAMS_REQUEST']._serialized_end=989
  _globals['_CGAMESCOPE_SETBLURPARAMS_RESPONSE']._serialized_start=991
  _globals['_CGAMESCOPE_SETBLURPARAMS_RESPONSE']._serialized_end=1026
  _globals['_GAMESCOPE']._serialized_start=1029
  _globals['_GAMESCOPE']._serialized_end=1286
# @@protoc_insertion_point(module_scope)
