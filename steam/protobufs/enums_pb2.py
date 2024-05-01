# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enums.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65nums.proto\x1a\x18steammessages_base.proto*\x80\n\n\x17\x45PublishedFileQueryType\x12)\n%k_PublishedFileQueryType_RankedByVote\x10\x00\x12\x34\n0k_PublishedFileQueryType_RankedByPublicationDate\x10\x01\x12\x42\n>k_PublishedFileQueryType_AcceptedForGameRankedByAcceptanceDate\x10\x02\x12*\n&k_PublishedFileQueryType_RankedByTrend\x10\x03\x12\x46\nBk_PublishedFileQueryType_FavoritedByFriendsRankedByPublicationDate\x10\x04\x12\x44\n@k_PublishedFileQueryType_CreatedByFriendsRankedByPublicationDate\x10\x05\x12\x35\n1k_PublishedFileQueryType_RankedByNumTimesReported\x10\x06\x12J\nFk_PublishedFileQueryType_CreatedByFollowedUsersRankedByPublicationDate\x10\x07\x12(\n$k_PublishedFileQueryType_NotYetRated\x10\x08\x12=\n9k_PublishedFileQueryType_RankedByTotalUniqueSubscriptions\x10\t\x12\x32\n.k_PublishedFileQueryType_RankedByTotalVotesAsc\x10\n\x12,\n(k_PublishedFileQueryType_RankedByVotesUp\x10\x0b\x12/\n+k_PublishedFileQueryType_RankedByTextSearch\x10\x0c\x12\x32\n.k_PublishedFileQueryType_RankedByPlaytimeTrend\x10\r\x12\x32\n.k_PublishedFileQueryType_RankedByTotalPlaytime\x10\x0e\x12\x39\n5k_PublishedFileQueryType_RankedByAveragePlaytimeTrend\x10\x0f\x12<\n8k_PublishedFileQueryType_RankedByLifetimeAveragePlaytime\x10\x10\x12:\n6k_PublishedFileQueryType_RankedByPlaytimeSessionsTrend\x10\x11\x12=\n9k_PublishedFileQueryType_RankedByLifetimePlaytimeSessions\x10\x12\x12?\n;k_PublishedFileQueryType_RankedByInappropriateContentRating\x10\x13\x12\x34\n0k_PublishedFileQueryType_RankedByBanContentCheck\x10\x14\x12\x34\n0k_PublishedFileQueryType_RankedByLastUpdatedDate\x10\x15*\xbc\x01\n#EPublishedFileInappropriateProvider\x12\x31\n-k_EPublishedFileInappropriateProvider_Invalid\x10\x00\x12\x30\n,k_EPublishedFileInappropriateProvider_Google\x10\x01\x12\x30\n,k_EPublishedFileInappropriateProvider_Amazon\x10\x02*\xd5\x02\n!EPublishedFileInappropriateResult\x12\x32\n.k_EPublishedFileInappropriateResult_NotScanned\x10\x00\x12\x34\n0k_EPublishedFileInappropriateResult_VeryUnlikely\x10\x01\x12\x30\n,k_EPublishedFileInappropriateResult_Unlikely\x10\x1e\x12\x30\n,k_EPublishedFileInappropriateResult_Possible\x10\x32\x12.\n*k_EPublishedFileInappropriateResult_Likely\x10K\x12\x32\n.k_EPublishedFileInappropriateResult_VeryLikely\x10\x64*\xb1\x03\n\x11\x45PersonaStateFlag\x12\'\n#k_EPersonaStateFlag_HasRichPresence\x10\x01\x12&\n\"k_EPersonaStateFlag_InJoinableGame\x10\x02\x12\x1e\n\x1ak_EPersonaStateFlag_Golden\x10\x04\x12*\n&k_EPersonaStateFlag_RemotePlayTogether\x10\x08\x12&\n!k_EPersonaStateFlag_ClientTypeWeb\x10\x80\x02\x12)\n$k_EPersonaStateFlag_ClientTypeMobile\x10\x80\x04\x12*\n%k_EPersonaStateFlag_ClientTypeTenfoot\x10\x80\x08\x12%\n k_EPersonaStateFlag_ClientTypeVR\x10\x80\x10\x12*\n%k_EPersonaStateFlag_LaunchTypeGamepad\x10\x80 \x12-\n(k_EPersonaStateFlag_LaunchTypeCompatTool\x10\x80@*\xa7\x01\n\x15\x45\x43ontentCheckProvider\x12#\n\x1fk_EContentCheckProvider_Invalid\x10\x00\x12\"\n\x1ek_EContentCheckProvider_Google\x10\x01\x12\"\n\x1ek_EContentCheckProvider_Amazon\x10\x02\x12!\n\x1dk_EContentCheckProvider_Local\x10\x03*\xec\x08\n\x19\x45ProfileCustomizationType\x12&\n\"k_EProfileCustomizationTypeInvalid\x10\x00\x12\x36\n2k_EProfileCustomizationTypeRareAchievementShowcase\x10\x01\x12,\n(k_EProfileCustomizationTypeGameCollector\x10\x02\x12+\n\'k_EProfileCustomizationTypeItemShowcase\x10\x03\x12,\n(k_EProfileCustomizationTypeTradeShowcase\x10\x04\x12%\n!k_EProfileCustomizationTypeBadges\x10\x05\x12+\n\'k_EProfileCustomizationTypeFavoriteGame\x10\x06\x12\x31\n-k_EProfileCustomizationTypeScreenshotShowcase\x10\x07\x12)\n%k_EProfileCustomizationTypeCustomText\x10\x08\x12,\n(k_EProfileCustomizationTypeFavoriteGroup\x10\t\x12-\n)k_EProfileCustomizationTypeRecommendation\x10\n\x12+\n\'k_EProfileCustomizationTypeWorkshopItem\x10\x0b\x12)\n%k_EProfileCustomizationTypeMyWorkshop\x10\x0c\x12.\n*k_EProfileCustomizationTypeArtworkShowcase\x10\r\x12,\n(k_EProfileCustomizationTypeVideoShowcase\x10\x0e\x12%\n!k_EProfileCustomizationTypeGuides\x10\x0f\x12\'\n#k_EProfileCustomizationTypeMyGuides\x10\x10\x12+\n\'k_EProfileCustomizationTypeAchievements\x10\x11\x12)\n%k_EProfileCustomizationTypeGreenlight\x10\x12\x12+\n\'k_EProfileCustomizationTypeMyGreenlight\x10\x13\x12%\n!k_EProfileCustomizationTypeSalien\x10\x14\x12\x35\n1k_EProfileCustomizationTypeLoyaltyRewardReactions\x10\x15\x12\x34\n0k_EProfileCustomizationTypeSingleArtworkShowcase\x10\x16\x12\x38\n4k_EProfileCustomizationTypeAchievementsCompletionist\x10\x17*\xc8\x01\n\x1b\x45PublishedFileStorageSystem\x12(\n$k_EPublishedFileStorageSystemInvalid\x10\x00\x12,\n(k_EPublishedFileStorageSystemLegacyCloud\x10\x01\x12&\n\"k_EPublishedFileStorageSystemDepot\x10\x02\x12)\n%k_EPublishedFileStorageSystemUGCCloud\x10\x03*\x97\x01\n\x19\x45\x43loudStoragePersistState\x12(\n$k_ECloudStoragePersistStatePersisted\x10\x00\x12(\n$k_ECloudStoragePersistStateForgotten\x10\x01\x12&\n\"k_ECloudStoragePersistStateDeleted\x10\x02*\xe8\x01\n\x12\x45SDCardFormatStage\x12 \n\x1ck_ESDCardFormatStage_Invalid\x10\x00\x12!\n\x1dk_ESDCardFormatStage_Starting\x10\x01\x12 \n\x1ck_ESDCardFormatStage_Testing\x10\x02\x12!\n\x1dk_ESDCardFormatStage_Rescuing\x10\x03\x12#\n\x1fk_ESDCardFormatStage_Formatting\x10\x04\x12#\n\x1fk_ESDCardFormatStage_Finalizing\x10\x05*\x84\x01\n\x15\x45SystemFanControlMode\x12\"\n\x1ek_SystemFanControlMode_Invalid\x10\x00\x12#\n\x1fk_SystemFanControlMode_Disabled\x10\x01\x12\"\n\x1ek_SystemFanControlMode_Default\x10\x02*\x81\x01\n\rEColorProfile\x12\x1b\n\x17k_EColorProfile_Invalid\x10\x00\x12\x1a\n\x16k_EColorProfile_Native\x10\x01\x12\x1c\n\x18k_EColorProfile_Standard\x10\x02\x12\x19\n\x15k_EColorProfile_Vivid\x10\x03*\xc0\x03\n\x14\x45\x42luetoothDeviceType\x12!\n\x1dk_BluetoothDeviceType_Invalid\x10\x00\x12!\n\x1dk_BluetoothDeviceType_Unknown\x10\x01\x12\x1f\n\x1bk_BluetoothDeviceType_Phone\x10\x02\x12\"\n\x1ek_BluetoothDeviceType_Computer\x10\x03\x12!\n\x1dk_BluetoothDeviceType_Headset\x10\x04\x12$\n k_BluetoothDeviceType_Headphones\x10\x05\x12\"\n\x1ek_BluetoothDeviceType_Speakers\x10\x06\x12$\n k_BluetoothDeviceType_OtherAudio\x10\x07\x12\x1f\n\x1bk_BluetoothDeviceType_Mouse\x10\x08\x12\"\n\x1ek_BluetoothDeviceType_Joystick\x10\t\x12!\n\x1dk_BluetoothDeviceType_Gamepad\x10\n\x12\"\n\x1ek_BluetoothDeviceType_Keyboard\x10\x0b*\x80\x01\n\x15\x45SystemAudioDirection\x12\"\n\x1ek_SystemAudioDirection_Invalid\x10\x00\x12 \n\x1ck_SystemAudioDirection_Input\x10\x01\x12!\n\x1dk_SystemAudioDirection_Output\x10\x02*\xf1\x02\n\x13\x45SystemAudioChannel\x12 \n\x1ck_SystemAudioChannel_Invalid\x10\x00\x12#\n\x1fk_SystemAudioChannel_Aggregated\x10\x01\x12\"\n\x1ek_SystemAudioChannel_FrontLeft\x10\x02\x12#\n\x1fk_SystemAudioChannel_FrontRight\x10\x03\x12\x1c\n\x18k_SystemAudioChannel_LFE\x10\x04\x12!\n\x1dk_SystemAudioChannel_BackLeft\x10\x05\x12\"\n\x1ek_SystemAudioChannel_BackRight\x10\x06\x12$\n k_SystemAudioChannel_FrontCenter\x10\x07\x12 \n\x1ck_SystemAudioChannel_Unknown\x10\x08\x12\x1d\n\x19k_SystemAudioChannel_Mono\x10\t*\xc9\x01\n\x14\x45SystemAudioPortType\x12!\n\x1dk_SystemAudioPortType_Invalid\x10\x00\x12!\n\x1dk_SystemAudioPortType_Unknown\x10\x01\x12\"\n\x1ek_SystemAudioPortType_Audio32f\x10\x02\x12 \n\x1ck_SystemAudioPortType_Midi8b\x10\x03\x12%\n!k_SystemAudioPortType_Video32RGBA\x10\x04*\x90\x01\n\x19\x45SystemAudioPortDirection\x12&\n\"k_SystemAudioPortDirection_Invalid\x10\x00\x12$\n k_SystemAudioPortDirection_Input\x10\x01\x12%\n!k_SystemAudioPortDirection_Output\x10\x02*\x83\x01\n\x13\x45SystemServiceState\x12%\n!k_ESystemServiceState_Unavailable\x10\x00\x12\"\n\x1ek_ESystemServiceState_Disabled\x10\x01\x12!\n\x1dk_ESystemServiceState_Enabled\x10\x02*\xe1\x01\n\x19\x45GraphicsPerfOverlayLevel\x12&\n\"k_EGraphicsPerfOverlayLevel_Hidden\x10\x00\x12%\n!k_EGraphicsPerfOverlayLevel_Basic\x10\x01\x12&\n\"k_EGraphicsPerfOverlayLevel_Medium\x10\x02\x12$\n k_EGraphicsPerfOverlayLevel_Full\x10\x03\x12\'\n#k_EGraphicsPerfOverlayLevel_Minimal\x10\x04*\xe5\x01\n\x14\x45GPUPerformanceLevel\x12\"\n\x1ek_EGPUPerformanceLevel_Invalid\x10\x00\x12\x1f\n\x1bk_EGPUPerformanceLevel_Auto\x10\x01\x12!\n\x1dk_EGPUPerformanceLevel_Manual\x10\x02\x12\x1e\n\x1ak_EGPUPerformanceLevel_Low\x10\x03\x12\x1f\n\x1bk_EGPUPerformanceLevel_High\x10\x04\x12$\n k_EGPUPerformanceLevel_Profiling\x10\x05*\xbb\x01\n\x0e\x45ScalingFilter\x12\x1c\n\x18k_EScalingFilter_Invalid\x10\x00\x12\x18\n\x14k_EScalingFilter_FSR\x10\x01\x12\x1c\n\x18k_EScalingFilter_Nearest\x10\x02\x12\x1c\n\x18k_EScalingFilter_Integer\x10\x03\x12\x1b\n\x17k_EScalingFilter_Linear\x10\x04\x12\x18\n\x14k_EScalingFilter_NIS\x10\x05*|\n\x0c\x45\x43PUGovernor\x12\x1a\n\x16k_ECPUGovernor_Invalid\x10\x00\x12\x17\n\x13k_ECPUGovernor_Perf\x10\x01\x12\x1c\n\x18k_ECPUGovernor_Powersave\x10\x02\x12\x19\n\x15k_ECPUGovernor_Manual\x10\x03*\xe2\x01\n\x0c\x45UpdaterType\x12\x1a\n\x16k_EUpdaterType_Invalid\x10\x00\x12\x19\n\x15k_EUpdaterType_Client\x10\x01\x12\x15\n\x11k_EUpdaterType_OS\x10\x02\x12\x17\n\x13k_EUpdaterType_BIOS\x10\x03\x12\x1d\n\x19k_EUpdaterType_Aggregated\x10\x04\x12\x18\n\x14k_EUpdaterType_Test1\x10\x05\x12\x18\n\x14k_EUpdaterType_Test2\x10\x06\x12\x18\n\x14k_EUpdaterType_Dummy\x10\x07*\xf9\x01\n\rEUpdaterState\x12\x1b\n\x17k_EUpdaterState_Invalid\x10\x00\x12\x1c\n\x18k_EUpdaterState_UpToDate\x10\x02\x12\x1c\n\x18k_EUpdaterState_Checking\x10\x03\x12\x1d\n\x19k_EUpdaterState_Available\x10\x04\x12\x1c\n\x18k_EUpdaterState_Applying\x10\x05\x12(\n$k_EUpdaterState_ClientRestartPending\x10\x06\x12(\n$k_EUpdaterState_SystemRestartPending\x10\x07*\xe1\x01\n\x18\x45StorageBlockContentType\x12&\n\"k_EStorageBlockContentType_Invalid\x10\x00\x12&\n\"k_EStorageBlockContentType_Unknown\x10\x01\x12)\n%k_EStorageBlockContentType_FileSystem\x10\x02\x12%\n!k_EStorageBlockContentType_Crypto\x10\x03\x12#\n\x1fk_EStorageBlockContentType_Raid\x10\x04*\xc3\x01\n\x1b\x45StorageBlockFileSystemType\x12)\n%k_EStorageBlockFileSystemType_Invalid\x10\x00\x12)\n%k_EStorageBlockFileSystemType_Unknown\x10\x01\x12&\n\"k_EStorageBlockFileSystemType_VFat\x10\x02\x12&\n\"k_EStorageBlockFileSystemType_Ext4\x10\x03*\xe3\x01\n\x1f\x45SteamDeckCompatibilityCategory\x12-\n)k_ESteamDeckCompatibilityCategory_Unknown\x10\x00\x12\x31\n-k_ESteamDeckCompatibilityCategory_Unsupported\x10\x01\x12.\n*k_ESteamDeckCompatibilityCategory_Playable\x10\x02\x12.\n*k_ESteamDeckCompatibilityCategory_Verified\x10\x03*\xd0\x02\n(ESteamDeckCompatibilityResultDisplayType\x12\x38\n4k_ESteamDeckCompatibilityResultDisplayType_Invisible\x10\x00\x12<\n8k_ESteamDeckCompatibilityResultDisplayType_Informational\x10\x01\x12:\n6k_ESteamDeckCompatibilityResultDisplayType_Unsupported\x10\x02\x12\x37\n3k_ESteamDeckCompatibilityResultDisplayType_Playable\x10\x03\x12\x37\n3k_ESteamDeckCompatibilityResultDisplayType_Verified\x10\x04*w\n\x08\x45\x41\x43State\x12\x16\n\x12k_EACState_Unknown\x10\x00\x12\x1b\n\x17k_EACState_Disconnected\x10\x01\x12\x18\n\x14k_EACState_Connected\x10\x02\x12\x1c\n\x18k_EACState_ConnectedSlow\x10\x03*\x85\x01\n\rEBatteryState\x12\x1b\n\x17k_EBatteryState_Unknown\x10\x00\x12\x1f\n\x1bk_EBatteryState_Discharging\x10\x01\x12\x1c\n\x18k_EBatteryState_Charging\x10\x02\x12\x18\n\x14k_EBatteryState_Full\x10\x03*\xaa\x01\n\tEOSBranch\x12\x17\n\x13k_EOSBranch_Unknown\x10\x00\x12\x17\n\x13k_EOSBranch_Release\x10\x01\x12 \n\x1ck_EOSBranch_ReleaseCandidate\x10\x02\x12\x14\n\x10k_EOSBranch_Beta\x10\x03\x12\x1d\n\x19k_EOSBranch_BetaCandidate\x10\x04\x12\x14\n\x10k_EOSBranch_Main\x10\x05*\xac\x05\n\x13\x45\x43ommunityItemClass\x12!\n\x1dk_ECommunityItemClass_Invalid\x10\x00\x12\x1f\n\x1bk_ECommunityItemClass_Badge\x10\x01\x12\"\n\x1ek_ECommunityItemClass_GameCard\x10\x02\x12+\n\'k_ECommunityItemClass_ProfileBackground\x10\x03\x12\"\n\x1ek_ECommunityItemClass_Emoticon\x10\x04\x12%\n!k_ECommunityItemClass_BoosterPack\x10\x05\x12$\n k_ECommunityItemClass_Consumable\x10\x06\x12!\n\x1dk_ECommunityItemClass_GameGoo\x10\x07\x12)\n%k_ECommunityItemClass_ProfileModifier\x10\x08\x12\x1f\n\x1bk_ECommunityItemClass_Scene\x10\t\x12$\n k_ECommunityItemClass_SalienItem\x10\n\x12!\n\x1dk_ECommunityItemClass_Sticker\x10\x0b\x12$\n k_ECommunityItemClass_ChatEffect\x10\x0c\x12/\n+k_ECommunityItemClass_MiniProfileBackground\x10\r\x12%\n!k_ECommunityItemClass_AvatarFrame\x10\x0e\x12(\n$k_ECommunityItemClass_AnimatedAvatar\x10\x0f\x12/\n+k_ECommunityItemClass_SteamDeckKeyboardSkin\x10\x10*\xd9\x01\n\x1f\x45SteamDeckCompatibilityFeedback\x12+\n\'k_ESteamDeckCompatibilityFeedback_Unset\x10\x00\x12+\n\'k_ESteamDeckCompatibilityFeedback_Agree\x10\x01\x12.\n*k_ESteamDeckCompatibilityFeedback_Disagree\x10\x02\x12,\n(k_ESteamDeckCompatibilityFeedback_Ignore\x10\x03*\x9f\x01\n\x1e\x45ProvideDeckFeedbackPreference\x12*\n&k_EProvideDeckFeedbackPreference_Unset\x10\x00\x12(\n$k_EProvideDeckFeedbackPreference_Yes\x10\x01\x12\'\n#k_EProvideDeckFeedbackPreference_No\x10\x02*\xb1\x03\n\rETouchGesture\x12\x17\n\x13k_ETouchGestureNone\x10\x00\x12\x18\n\x14k_ETouchGestureTouch\x10\x01\x12\x16\n\x12k_ETouchGestureTap\x10\x02\x12\x1c\n\x18k_ETouchGestureDoubleTap\x10\x03\x12\x1d\n\x19k_ETouchGestureShortPress\x10\x04\x12\x1c\n\x18k_ETouchGestureLongPress\x10\x05\x12\x1a\n\x16k_ETouchGestureLongTap\x10\x06\x12\x1f\n\x1bk_ETouchGestureTwoFingerTap\x10\x07\x12\x1f\n\x1bk_ETouchGestureTapCancelled\x10\x08\x12\x1d\n\x19k_ETouchGesturePinchBegin\x10\t\x12\x1e\n\x1ak_ETouchGesturePinchUpdate\x10\n\x12\x1b\n\x17k_ETouchGesturePinchEnd\x10\x0b\x12\x1d\n\x19k_ETouchGestureFlingStart\x10\x0c\x12!\n\x1dk_ETouchGestureFlingCancelled\x10\r*\x8c\x01\n\x13\x45SessionPersistence\x12*\n\x1dk_ESessionPersistence_Invalid\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x1fk_ESessionPersistence_Ephemeral\x10\x00\x12$\n k_ESessionPersistence_Persistent\x10\x01\x42\tH\x01\x90\x01\x01\x80\xb5\x18\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\001\200\265\030\001'
  _globals['_EPUBLISHEDFILEQUERYTYPE']._serialized_start=42
  _globals['_EPUBLISHEDFILEQUERYTYPE']._serialized_end=1322
  _globals['_EPUBLISHEDFILEINAPPROPRIATEPROVIDER']._serialized_start=1325
  _globals['_EPUBLISHEDFILEINAPPROPRIATEPROVIDER']._serialized_end=1513
  _globals['_EPUBLISHEDFILEINAPPROPRIATERESULT']._serialized_start=1516
  _globals['_EPUBLISHEDFILEINAPPROPRIATERESULT']._serialized_end=1857
  _globals['_EPERSONASTATEFLAG']._serialized_start=1860
  _globals['_EPERSONASTATEFLAG']._serialized_end=2293
  _globals['_ECONTENTCHECKPROVIDER']._serialized_start=2296
  _globals['_ECONTENTCHECKPROVIDER']._serialized_end=2463
  _globals['_EPROFILECUSTOMIZATIONTYPE']._serialized_start=2466
  _globals['_EPROFILECUSTOMIZATIONTYPE']._serialized_end=3598
  _globals['_EPUBLISHEDFILESTORAGESYSTEM']._serialized_start=3601
  _globals['_EPUBLISHEDFILESTORAGESYSTEM']._serialized_end=3801
  _globals['_ECLOUDSTORAGEPERSISTSTATE']._serialized_start=3804
  _globals['_ECLOUDSTORAGEPERSISTSTATE']._serialized_end=3955
  _globals['_ESDCARDFORMATSTAGE']._serialized_start=3958
  _globals['_ESDCARDFORMATSTAGE']._serialized_end=4190
  _globals['_ESYSTEMFANCONTROLMODE']._serialized_start=4193
  _globals['_ESYSTEMFANCONTROLMODE']._serialized_end=4325
  _globals['_ECOLORPROFILE']._serialized_start=4328
  _globals['_ECOLORPROFILE']._serialized_end=4457
  _globals['_EBLUETOOTHDEVICETYPE']._serialized_start=4460
  _globals['_EBLUETOOTHDEVICETYPE']._serialized_end=4908
  _globals['_ESYSTEMAUDIODIRECTION']._serialized_start=4911
  _globals['_ESYSTEMAUDIODIRECTION']._serialized_end=5039
  _globals['_ESYSTEMAUDIOCHANNEL']._serialized_start=5042
  _globals['_ESYSTEMAUDIOCHANNEL']._serialized_end=5411
  _globals['_ESYSTEMAUDIOPORTTYPE']._serialized_start=5414
  _globals['_ESYSTEMAUDIOPORTTYPE']._serialized_end=5615
  _globals['_ESYSTEMAUDIOPORTDIRECTION']._serialized_start=5618
  _globals['_ESYSTEMAUDIOPORTDIRECTION']._serialized_end=5762
  _globals['_ESYSTEMSERVICESTATE']._serialized_start=5765
  _globals['_ESYSTEMSERVICESTATE']._serialized_end=5896
  _globals['_EGRAPHICSPERFOVERLAYLEVEL']._serialized_start=5899
  _globals['_EGRAPHICSPERFOVERLAYLEVEL']._serialized_end=6124
  _globals['_EGPUPERFORMANCELEVEL']._serialized_start=6127
  _globals['_EGPUPERFORMANCELEVEL']._serialized_end=6356
  _globals['_ESCALINGFILTER']._serialized_start=6359
  _globals['_ESCALINGFILTER']._serialized_end=6546
  _globals['_ECPUGOVERNOR']._serialized_start=6548
  _globals['_ECPUGOVERNOR']._serialized_end=6672
  _globals['_EUPDATERTYPE']._serialized_start=6675
  _globals['_EUPDATERTYPE']._serialized_end=6901
  _globals['_EUPDATERSTATE']._serialized_start=6904
  _globals['_EUPDATERSTATE']._serialized_end=7153
  _globals['_ESTORAGEBLOCKCONTENTTYPE']._serialized_start=7156
  _globals['_ESTORAGEBLOCKCONTENTTYPE']._serialized_end=7381
  _globals['_ESTORAGEBLOCKFILESYSTEMTYPE']._serialized_start=7384
  _globals['_ESTORAGEBLOCKFILESYSTEMTYPE']._serialized_end=7579
  _globals['_ESTEAMDECKCOMPATIBILITYCATEGORY']._serialized_start=7582
  _globals['_ESTEAMDECKCOMPATIBILITYCATEGORY']._serialized_end=7809
  _globals['_ESTEAMDECKCOMPATIBILITYRESULTDISPLAYTYPE']._serialized_start=7812
  _globals['_ESTEAMDECKCOMPATIBILITYRESULTDISPLAYTYPE']._serialized_end=8148
  _globals['_EACSTATE']._serialized_start=8150
  _globals['_EACSTATE']._serialized_end=8269
  _globals['_EBATTERYSTATE']._serialized_start=8272
  _globals['_EBATTERYSTATE']._serialized_end=8405
  _globals['_EOSBRANCH']._serialized_start=8408
  _globals['_EOSBRANCH']._serialized_end=8578
  _globals['_ECOMMUNITYITEMCLASS']._serialized_start=8581
  _globals['_ECOMMUNITYITEMCLASS']._serialized_end=9265
  _globals['_ESTEAMDECKCOMPATIBILITYFEEDBACK']._serialized_start=9268
  _globals['_ESTEAMDECKCOMPATIBILITYFEEDBACK']._serialized_end=9485
  _globals['_EPROVIDEDECKFEEDBACKPREFERENCE']._serialized_start=9488
  _globals['_EPROVIDEDECKFEEDBACKPREFERENCE']._serialized_end=9647
  _globals['_ETOUCHGESTURE']._serialized_start=9650
  _globals['_ETOUCHGESTURE']._serialized_end=10083
  _globals['_ESESSIONPERSISTENCE']._serialized_start=10086
  _globals['_ESESSIONPERSISTENCE']._serialized_end=10226
# @@protoc_insertion_point(module_scope)
