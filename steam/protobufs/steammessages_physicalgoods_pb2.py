# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_physicalgoods.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!steammessages_physicalgoods.proto\x1a steammessages_unified_base.proto\"`\n.CPhysicalGoods_RegisterSteamController_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\"1\n/CPhysicalGoods_RegisterSteamController_Response\"l\n:CPhysicalGoods_CompleteSteamControllerRegistration_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\"=\n;CPhysicalGoods_CompleteSteamControllerRegistration_Response\"h\n6CPhysicalGoods_QueryAccountsRegisteredToSerial_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\"k\n7CPhysicalGoods_QueryAccountsRegisteredToSerial_Accounts\x12\x11\n\taccountid\x18\x01 \x01(\r\x12\x1d\n\x15registration_complete\x18\x02 \x01(\x08\"\x85\x01\n7CPhysicalGoods_QueryAccountsRegisteredToSerial_Response\x12J\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x38.CPhysicalGoods_QueryAccountsRegisteredToSerial_Accounts\"~\n8CPhysicalGoods_SteamControllerSetConfig_ControllerConfig\x12\x13\n\x0b\x61ppidorname\x18\x01 \x01(\t\x12\x17\n\x0fpublishedfileid\x18\x02 \x01(\x04\x12\x14\n\x0ctemplatename\x18\x03 \x01(\t\"\x88\x02\n/CPhysicalGoods_SteamControllerSetConfig_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\x12\x11\n\taccountid\x18\x03 \x01(\r\x12Q\n\x0e\x63onfigurations\x18\x04 \x03(\x0b\x32\x39.CPhysicalGoods_SteamControllerSetConfig_ControllerConfig\x12\x1a\n\x0f\x63ontroller_type\x18\x05 \x01(\x05:\x01\x32\x12#\n\x14only_for_this_serial\x18\x06 \x01(\x08:\x05\x66\x61lse\"2\n0CPhysicalGoods_SteamControllerSetConfig_Response\"\xca\x01\n/CPhysicalGoods_SteamControllerGetConfig_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\x12\x11\n\taccountid\x18\x03 \x01(\r\x12\x13\n\x0b\x61ppidorname\x18\x04 \x01(\t\x12\x1a\n\x0f\x63ontroller_type\x18\x05 \x01(\x05:\x01\x32\x12#\n\x14only_for_this_serial\x18\x06 \x01(\x08:\x05\x66\x61lse\"\x95\x01\n8CPhysicalGoods_SteamControllerGetConfig_ControllerConfig\x12\x13\n\x0b\x61ppidorname\x18\x01 \x01(\t\x12\x17\n\x0fpublishedfileid\x18\x02 \x01(\x04\x12\x14\n\x0ctemplatename\x18\x03 \x01(\t\x12\x15\n\rserial_number\x18\x04 \x01(\t\"\x85\x01\n0CPhysicalGoods_SteamControllerGetConfig_Response\x12Q\n\x0e\x63onfigurations\x18\x01 \x03(\x0b\x32\x39.CPhysicalGoods_SteamControllerGetConfig_ControllerConfig\"u\n0CPhysicalGoods_DeRegisterSteamController_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\x12\x11\n\taccountid\x18\x03 \x01(\r\"3\n1CPhysicalGoods_DeRegisterSteamController_Response\"r\n-CPhysicalGoods_SetPersonalizationFile_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0fpublishedfileid\x18\x02 \x01(\x04\x12\x11\n\taccountid\x18\x03 \x01(\r\"0\n.CPhysicalGoods_SetPersonalizationFile_Response\"Y\n-CPhysicalGoods_GetPersonalizationFile_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x11\n\taccountid\x18\x02 \x01(\r\"I\n.CPhysicalGoods_GetPersonalizationFile_Response\x12\x17\n\x0fpublishedfileid\x18\x01 \x01(\x04\x32\xd7\x0c\n\rPhysicalGoods\x12\xd4\x01\n\x17RegisterSteamController\x12/.CPhysicalGoods_RegisterSteamController_Request\x1a\x30.CPhysicalGoods_RegisterSteamController_Response\"V\x82\xb5\x18RRecords a serial number and the calling user\'s account info for warranty purposes.\x12\xd3\x01\n#CompleteSteamControllerRegistration\x12;.CPhysicalGoods_CompleteSteamControllerRegistration_Request\x1a<.CPhysicalGoods_CompleteSteamControllerRegistration_Response\"1\x82\xb5\x18-Marks a controller\'s registration as complete\x12\xd7\x01\n#QueryAccountsRegisteredToController\x12\x37.CPhysicalGoods_QueryAccountsRegisteredToSerial_Request\x1a\x38.CPhysicalGoods_QueryAccountsRegisteredToSerial_Response\"=\x82\xb5\x18\x39Sends back a list of accounts registered to a controller.\x12\xb8\x01\n SetDesiredControllerConfigForApp\x12\x30.CPhysicalGoods_SteamControllerSetConfig_Request\x1a\x31.CPhysicalGoods_SteamControllerSetConfig_Response\"/\x82\xb5\x18+Sets a desired controller config for an app\x12\xb8\x01\n GetDesiredControllerConfigForApp\x12\x30.CPhysicalGoods_SteamControllerGetConfig_Request\x1a\x31.CPhysicalGoods_SteamControllerGetConfig_Response\"/\x82\xb5\x18+Gets a desired controller config for an app\x12\xa1\x01\n\x19\x44\x65RegisterSteamController\x12\x31.CPhysicalGoods_DeRegisterSteamController_Request\x1a\x32.CPhysicalGoods_DeRegisterSteamController_Response\"\x1d\x82\xb5\x18\x19\x44\x65 registers a controller\x12\xb7\x01\n SetControllerPersonalizationFile\x12..CPhysicalGoods_SetPersonalizationFile_Request\x1a/.CPhysicalGoods_SetPersonalizationFile_Response\"2\x82\xb5\x18.Stores the file ID of the personalization file\x12\xb5\x01\n GetControllerPersonalizationFile\x12..CPhysicalGoods_GetPersonalizationFile_Request\x1a/.CPhysicalGoods_GetPersonalizationFile_Response\"0\x82\xb5\x18,Gets the file ID of the personalization file\x1a\x33\x82\xb5\x18/A service to use physical goods related methodsB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_physicalgoods_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_PHYSICALGOODS']._loaded_options = None
  _globals['_PHYSICALGOODS']._serialized_options = b'\202\265\030/A service to use physical goods related methods'
  _globals['_PHYSICALGOODS'].methods_by_name['RegisterSteamController']._loaded_options = None
  _globals['_PHYSICALGOODS'].methods_by_name['RegisterSteamController']._serialized_options = b'\202\265\030RRecords a serial number and the calling user\'s account info for warranty purposes.'
  _globals['_PHYSICALGOODS'].methods_by_name['CompleteSteamControllerRegistration']._loaded_options = None
  _globals['_PHYSICALGOODS'].methods_by_name['CompleteSteamControllerRegistration']._serialized_options = b'\202\265\030-Marks a controller\'s registration as complete'
  _globals['_PHYSICALGOODS'].methods_by_name['QueryAccountsRegisteredToController']._loaded_options = None
  _globals['_PHYSICALGOODS'].methods_by_name['QueryAccountsRegisteredToController']._serialized_options = b'\202\265\0309Sends back a list of accounts registered to a controller.'
  _globals['_PHYSICALGOODS'].methods_by_name['SetDesiredControllerConfigForApp']._loaded_options = None
  _globals['_PHYSICALGOODS'].methods_by_name['SetDesiredControllerConfigForApp']._serialized_options = b'\202\265\030+Sets a desired controller config for an app'
  _globals['_PHYSICALGOODS'].methods_by_name['GetDesiredControllerConfigForApp']._loaded_options = None
  _globals['_PHYSICALGOODS'].methods_by_name['GetDesiredControllerConfigForApp']._serialized_options = b'\202\265\030+Gets a desired controller config for an app'
  _globals['_PHYSICALGOODS'].methods_by_name['DeRegisterSteamController']._loaded_options = None
  _globals['_PHYSICALGOODS'].methods_by_name['DeRegisterSteamController']._serialized_options = b'\202\265\030\031De registers a controller'
  _globals['_PHYSICALGOODS'].methods_by_name['SetControllerPersonalizationFile']._loaded_options = None
  _globals['_PHYSICALGOODS'].methods_by_name['SetControllerPersonalizationFile']._serialized_options = b'\202\265\030.Stores the file ID of the personalization file'
  _globals['_PHYSICALGOODS'].methods_by_name['GetControllerPersonalizationFile']._loaded_options = None
  _globals['_PHYSICALGOODS'].methods_by_name['GetControllerPersonalizationFile']._serialized_options = b'\202\265\030,Gets the file ID of the personalization file'
  _globals['_CPHYSICALGOODS_REGISTERSTEAMCONTROLLER_REQUEST']._serialized_start=71
  _globals['_CPHYSICALGOODS_REGISTERSTEAMCONTROLLER_REQUEST']._serialized_end=167
  _globals['_CPHYSICALGOODS_REGISTERSTEAMCONTROLLER_RESPONSE']._serialized_start=169
  _globals['_CPHYSICALGOODS_REGISTERSTEAMCONTROLLER_RESPONSE']._serialized_end=218
  _globals['_CPHYSICALGOODS_COMPLETESTEAMCONTROLLERREGISTRATION_REQUEST']._serialized_start=220
  _globals['_CPHYSICALGOODS_COMPLETESTEAMCONTROLLERREGISTRATION_REQUEST']._serialized_end=328
  _globals['_CPHYSICALGOODS_COMPLETESTEAMCONTROLLERREGISTRATION_RESPONSE']._serialized_start=330
  _globals['_CPHYSICALGOODS_COMPLETESTEAMCONTROLLERREGISTRATION_RESPONSE']._serialized_end=391
  _globals['_CPHYSICALGOODS_QUERYACCOUNTSREGISTEREDTOSERIAL_REQUEST']._serialized_start=393
  _globals['_CPHYSICALGOODS_QUERYACCOUNTSREGISTEREDTOSERIAL_REQUEST']._serialized_end=497
  _globals['_CPHYSICALGOODS_QUERYACCOUNTSREGISTEREDTOSERIAL_ACCOUNTS']._serialized_start=499
  _globals['_CPHYSICALGOODS_QUERYACCOUNTSREGISTEREDTOSERIAL_ACCOUNTS']._serialized_end=606
  _globals['_CPHYSICALGOODS_QUERYACCOUNTSREGISTEREDTOSERIAL_RESPONSE']._serialized_start=609
  _globals['_CPHYSICALGOODS_QUERYACCOUNTSREGISTEREDTOSERIAL_RESPONSE']._serialized_end=742
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERSETCONFIG_CONTROLLERCONFIG']._serialized_start=744
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERSETCONFIG_CONTROLLERCONFIG']._serialized_end=870
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERSETCONFIG_REQUEST']._serialized_start=873
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERSETCONFIG_REQUEST']._serialized_end=1137
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERSETCONFIG_RESPONSE']._serialized_start=1139
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERSETCONFIG_RESPONSE']._serialized_end=1189
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERGETCONFIG_REQUEST']._serialized_start=1192
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERGETCONFIG_REQUEST']._serialized_end=1394
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERGETCONFIG_CONTROLLERCONFIG']._serialized_start=1397
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERGETCONFIG_CONTROLLERCONFIG']._serialized_end=1546
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERGETCONFIG_RESPONSE']._serialized_start=1549
  _globals['_CPHYSICALGOODS_STEAMCONTROLLERGETCONFIG_RESPONSE']._serialized_end=1682
  _globals['_CPHYSICALGOODS_DEREGISTERSTEAMCONTROLLER_REQUEST']._serialized_start=1684
  _globals['_CPHYSICALGOODS_DEREGISTERSTEAMCONTROLLER_REQUEST']._serialized_end=1801
  _globals['_CPHYSICALGOODS_DEREGISTERSTEAMCONTROLLER_RESPONSE']._serialized_start=1803
  _globals['_CPHYSICALGOODS_DEREGISTERSTEAMCONTROLLER_RESPONSE']._serialized_end=1854
  _globals['_CPHYSICALGOODS_SETPERSONALIZATIONFILE_REQUEST']._serialized_start=1856
  _globals['_CPHYSICALGOODS_SETPERSONALIZATIONFILE_REQUEST']._serialized_end=1970
  _globals['_CPHYSICALGOODS_SETPERSONALIZATIONFILE_RESPONSE']._serialized_start=1972
  _globals['_CPHYSICALGOODS_SETPERSONALIZATIONFILE_RESPONSE']._serialized_end=2020
  _globals['_CPHYSICALGOODS_GETPERSONALIZATIONFILE_REQUEST']._serialized_start=2022
  _globals['_CPHYSICALGOODS_GETPERSONALIZATIONFILE_REQUEST']._serialized_end=2111
  _globals['_CPHYSICALGOODS_GETPERSONALIZATIONFILE_RESPONSE']._serialized_start=2113
  _globals['_CPHYSICALGOODS_GETPERSONALIZATIONFILE_RESPONSE']._serialized_end=2186
  _globals['_PHYSICALGOODS']._serialized_start=2189
  _globals['_PHYSICALGOODS']._serialized_end=3812
_builder.BuildServices(DESCRIPTOR, 'steammessages_physicalgoods_pb2', _globals)
# @@protoc_insertion_point(module_scope)
