# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_market.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asteammessages_market.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"n\n(CEconMarket_IsMarketplaceAllowed_Request\x12\x42\n\twebcookie\x18\x01 \x01(\tB/\x82\xb5\x18+The user\'s Steam Guard machine auth cookie.\"\xf5\x05\n)CEconMarket_IsMarketplaceAllowed_Response\x12I\n\x07\x61llowed\x18\x01 \x01(\x08\x42\x38\x82\xb5\x18\x34Whether or not the user is allowed to use the market\x12K\n\x06reason\x18\x02 \x01(\rB;\x82\xb5\x18\x37The reason the user can\'t use the market, if applicable\x12P\n\x0f\x61llowed_at_time\x18\x03 \x01(\rB7\x82\xb5\x18\x33The time the user will be allowed to use the market\x12\x84\x01\n\x18steamguard_required_days\x18\x04 \x01(\rBb\x82\xb5\x18^The number of days any user is required to have had Steam Guard before they can use the market\x12W\n\x0f\x66orms_requested\x18\x07 \x01(\x08\x42>\x82\xb5\x18:Whether or not we\'ve requested the user fill out tax forms\x12h\n\x1a\x66orms_require_verification\x18\x08 \x01(\x08\x42\x44\x82\xb5\x18@True if we\'ve received forms but they require verification first\x12\x93\x01\n\x18new_device_cooldown_days\x18\t \x01(\rBq\x82\xb5\x18mThe number of days after initial device authorization a user must wait before using the market on that device2\xee\x01\n\nEconMarket\x12\xb8\x01\n\x14IsMarketplaceAllowed\x12).CEconMarket_IsMarketplaceAllowed_Request\x1a*.CEconMarket_IsMarketplaceAllowed_Response\"I\x82\xb5\x18\x45\x43hecks whether or not the authed account is allowed to use the market\x1a%\x82\xb5\x18!A service to use market functionsB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_market_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_REQUEST'].fields_by_name['webcookie']._loaded_options = None
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_REQUEST'].fields_by_name['webcookie']._serialized_options = b'\202\265\030+The user\'s Steam Guard machine auth cookie.'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['allowed']._loaded_options = None
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['allowed']._serialized_options = b'\202\265\0304Whether or not the user is allowed to use the market'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['reason']._loaded_options = None
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['reason']._serialized_options = b'\202\265\0307The reason the user can\'t use the market, if applicable'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['allowed_at_time']._loaded_options = None
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['allowed_at_time']._serialized_options = b'\202\265\0303The time the user will be allowed to use the market'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['steamguard_required_days']._loaded_options = None
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['steamguard_required_days']._serialized_options = b'\202\265\030^The number of days any user is required to have had Steam Guard before they can use the market'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['forms_requested']._loaded_options = None
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['forms_requested']._serialized_options = b'\202\265\030:Whether or not we\'ve requested the user fill out tax forms'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['forms_require_verification']._loaded_options = None
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['forms_require_verification']._serialized_options = b'\202\265\030@True if we\'ve received forms but they require verification first'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['new_device_cooldown_days']._loaded_options = None
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE'].fields_by_name['new_device_cooldown_days']._serialized_options = b'\202\265\030mThe number of days after initial device authorization a user must wait before using the market on that device'
  _globals['_ECONMARKET']._loaded_options = None
  _globals['_ECONMARKET']._serialized_options = b'\202\265\030!A service to use market functions'
  _globals['_ECONMARKET'].methods_by_name['IsMarketplaceAllowed']._loaded_options = None
  _globals['_ECONMARKET'].methods_by_name['IsMarketplaceAllowed']._serialized_options = b'\202\265\030EChecks whether or not the authed account is allowed to use the market'
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_REQUEST']._serialized_start=90
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_REQUEST']._serialized_end=200
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE']._serialized_start=203
  _globals['_CECONMARKET_ISMARKETPLACEALLOWED_RESPONSE']._serialized_end=960
  _globals['_ECONMARKET']._serialized_start=963
  _globals['_ECONMARKET']._serialized_end=1201
_builder.BuildServices(DESCRIPTOR, 'steammessages_market_pb2', _globals)
# @@protoc_insertion_point(module_scope)
