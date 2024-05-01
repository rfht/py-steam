# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_familygroups.steamclient.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,steammessages_familygroups.steamclient.proto\x1a\x18steammessages_base.proto\x1a,steammessages_unified_base.steamclient.proto\"H\n\'CFamilyGroups_CreateFamilyGroup_Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\"B\n(CFamilyGroups_CreateFamilyGroup_Response\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\"Y\n$CFamilyGroups_GetFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x19\n\x11send_running_apps\x18\x02 \x01(\x08\"\x97\x01\n\x11\x46\x61milyGroupMember\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x38\n\x04role\x18\x02 \x01(\x0e\x32\x11.EFamilyGroupRole:\x17k_EFamilyGroupRole_None\x12\x13\n\x0btime_joined\x18\x03 \x01(\r\x12\"\n\x1a\x63ooldown_seconds_remaining\x18\x04 \x01(\r\"e\n\x18\x46\x61milyGroupPendingInvite\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x38\n\x04role\x18\x02 \x01(\x0e\x32\x11.EFamilyGroupRole:\x17k_EFamilyGroupRole_None\"*\n\x17\x46\x61milyGroupFormerMember\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\xaf\x02\n%CFamilyGroups_GetFamilyGroup_Response\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x07members\x18\x02 \x03(\x0b\x32\x12.FamilyGroupMember\x12\x32\n\x0fpending_invites\x18\x03 \x03(\x0b\x32\x19.FamilyGroupPendingInvite\x12\x12\n\nfree_spots\x18\x04 \x01(\r\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\x12\'\n\x1fslot_cooldown_remaining_seconds\x18\x06 \x01(\r\x12\x30\n\x0e\x66ormer_members\x18\x07 \x03(\x0b\x32\x18.FamilyGroupFormerMember\x12\x1f\n\x17slot_cooldown_overrides\x18\x08 \x01(\r\"e\n+CFamilyGroups_GetFamilyGroupForUser_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x04\x12%\n\x1dinclude_family_group_response\x18\x02 \x01(\x08\"\x8c\x01\n\x1f\x46\x61milyGroupPendingInviteForUser\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x38\n\x04role\x18\x02 \x01(\x0e\x32\x11.EFamilyGroupRole:\x17k_EFamilyGroupRole_None\x12\x17\n\x0finviter_steamid\x18\x03 \x01(\x06\"\xdd\x02\n,CFamilyGroups_GetFamilyGroupForUser_Response\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\"\n\x1ais_not_member_of_any_group\x18\x02 \x01(\x08\x12\x1a\n\x12latest_time_joined\x18\x03 \x01(\r\x12$\n\x1clatest_joined_family_groupid\x18\x04 \x01(\x04\x12?\n\x15pending_group_invites\x18\x05 \x03(\x0b\x32 .FamilyGroupPendingInviteForUser\x12\x0c\n\x04role\x18\x06 \x01(\r\x12\"\n\x1a\x63ooldown_seconds_remaining\x18\x07 \x01(\r\x12<\n\x0c\x66\x61mily_group\x18\x08 \x01(\x0b\x32&.CFamilyGroups_GetFamilyGroup_Response\"V\n.CFamilyGroups_ModifyFamilyGroupDetails_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\"1\n/CFamilyGroups_ModifyFamilyGroupDetails_Response\"\xa0\x01\n)CFamilyGroups_InviteToFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x18\n\x10receiver_steamid\x18\x02 \x01(\x06\x12\x41\n\rreceiver_role\x18\x03 \x01(\x0e\x32\x11.EFamilyGroupRole:\x17k_EFamilyGroupRole_None\"\x9d\x01\n*CFamilyGroups_InviteToFamilyGroup_Response\x12\x11\n\tinvite_id\x18\x01 \x01(\x04\x12\\\n\x11two_factor_method\x18\x02 \x01(\x0e\x32\x1d.EFamilyGroupsTwoFactorMethod:\"k_EFamilyGroupsTwoFactorMethodNone\"l\n0CFamilyGroups_ConfirmInviteToFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x11\n\tinvite_id\x18\x02 \x01(\x04\x12\r\n\x05nonce\x18\x03 \x01(\x04\"3\n1CFamilyGroups_ConfirmInviteToFamilyGroup_Response\"^\n3CFamilyGroups_ResendInvitationToFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\"6\n4CFamilyGroups_ResendInvitationToFamilyGroup_Response\"N\n%CFamilyGroups_JoinFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\r\n\x05nonce\x18\x02 \x01(\x04\"\x86\x01\n&CFamilyGroups_JoinFamilyGroup_Response\x12\\\n\x11two_factor_method\x18\x02 \x01(\x0e\x32\x1d.EFamilyGroupsTwoFactorMethod:\"k_EFamilyGroupsTwoFactorMethodNone\"h\n,CFamilyGroups_ConfirmJoinFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x11\n\tinvite_id\x18\x02 \x01(\x04\x12\r\n\x05nonce\x18\x03 \x01(\x04\"/\n-CFamilyGroups_ConfirmJoinFamilyGroup_Response\"`\n+CFamilyGroups_RemoveFromFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x19\n\x11steamid_to_remove\x18\x02 \x01(\x06\".\n,CFamilyGroups_RemoveFromFamilyGroup_Response\"b\n-CFamilyGroups_CancelFamilyGroupInvite_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x19\n\x11steamid_to_cancel\x18\x02 \x01(\x06\"0\n.CFamilyGroups_CancelFamilyGroupInvite_Response\"a\n+CFamilyGroups_GetUsersSharingDevice_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x1a\n\x12\x63lient_instance_id\x18\x02 \x01(\x04\"=\n,CFamilyGroups_GetUsersSharingDevice_Response\x12\r\n\x05users\x18\x01 \x03(\x06\"A\n\'CFamilyGroups_DeleteFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\"*\n(CFamilyGroups_DeleteFamilyGroup_Response\"B\n(CFamilyGroups_GetPlaytimeSummary_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x06\"\x82\x01\n\x1b\x43\x46\x61milyGroups_PlaytimeEntry\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x14\n\x0c\x66irst_played\x18\x03 \x01(\r\x12\x15\n\rlatest_played\x18\x04 \x01(\r\x12\x16\n\x0eseconds_played\x18\x05 \x01(\r\"Z\n)CFamilyGroups_GetPlaytimeSummary_Response\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.CFamilyGroups_PlaytimeEntry\"\x8e\x01\n%CFamilyGroups_RequestPurchase_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x17\n\x0fgidshoppingcart\x18\x02 \x01(\x04\x12\x1a\n\x12store_country_code\x18\x03 \x01(\t\x12\x18\n\x10use_account_cart\x18\x04 \x01(\x08\"U\n&CFamilyGroups_RequestPurchase_Response\x12\x17\n\x0fgidshoppingcart\x18\x01 \x01(\x04\x12\x12\n\nrequest_id\x18\x02 \x01(\x04\"|\n)CFamilyGroups_GetPurchaseRequests_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x13\n\x0brequest_ids\x18\x03 \x03(\x04\x12\"\n\x1art_include_completed_since\x18\x04 \x01(\r\"\x81\x03\n\x0fPurchaseRequest\x12\x19\n\x11requester_steamid\x18\x01 \x01(\x06\x12\x17\n\x0fgidshoppingcart\x18\x02 \x01(\x04\x12\x16\n\x0etime_requested\x18\x03 \x01(\r\x12\x16\n\x0etime_responded\x18\x04 \x01(\r\x12\x19\n\x11responder_steamid\x18\x05 \x01(\x06\x12O\n\x0fresponse_action\x18\x06 \x01(\x0e\x32\x17.EPurchaseRequestAction:\x1dk_EPurchaseRequestAction_None\x12\x14\n\x0cis_completed\x18\x07 \x01(\x08\x12\x12\n\nrequest_id\x18\x08 \x01(\x04\x12\x1c\n\x14requested_packageids\x18\t \x03(\r\x12\x1c\n\x14purchased_packageids\x18\n \x03(\r\x12\x1b\n\x13requested_bundleids\x18\x0b \x03(\r\x12\x1b\n\x13purchased_bundleids\x18\x0c \x03(\r\"P\n*CFamilyGroups_GetPurchaseRequests_Response\x12\"\n\x08requests\x18\x01 \x03(\x0b\x32\x10.PurchaseRequest\"\xa6\x01\n0CFamilyGroups_RespondToRequestedPurchase_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x46\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x17.EPurchaseRequestAction:\x1dk_EPurchaseRequestAction_None\x12\x12\n\nrequest_id\x18\x04 \x01(\x04\"3\n1CFamilyGroups_RespondToRequestedPurchase_Response\"<\n\"CFamilyGroups_GetChangeLog_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\"\xf9\x01\n#CFamilyGroups_GetChangeLog_Response\x12<\n\x07\x63hanges\x18\x01 \x03(\x0b\x32+.CFamilyGroups_GetChangeLog_Response.Change\x1a\x93\x01\n\x06\x43hange\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\x12\x15\n\ractor_steamid\x18\x02 \x01(\x06\x12=\n\x04type\x18\x03 \x01(\x0e\x32\x1a.EFamilyGroupChangeLogType:\x13k_InvalidChangeType\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x12\n\nby_support\x18\x05 \x01(\x08\"b\n0CFamilyGroups_SetFamilyCooldownOverrides_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x16\n\x0e\x63ooldown_count\x18\x02 \x01(\r\"3\n1CFamilyGroups_SetFamilyCooldownOverrides_Response\"\x97\x01\n*CFamilyGroups_GetSharedLibraryApps_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x06\x12\x13\n\x0binclude_own\x18\x02 \x01(\x08\x12\x18\n\x10include_excluded\x18\x03 \x01(\x08\x12\x10\n\x08language\x18\x05 \x01(\t\x12\x10\n\x08max_apps\x18\x06 \x01(\r\"\x90\x03\n+CFamilyGroups_GetSharedLibraryApps_Response\x12\x44\n\x04\x61pps\x18\x01 \x03(\x0b\x32\x36.CFamilyGroups_GetSharedLibraryApps_Response.SharedApp\x1a\x9a\x02\n\tSharedApp\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x16\n\x0eowner_steamids\x18\x02 \x03(\x06\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07sort_as\x18\x07 \x01(\t\x12\x18\n\x10\x63\x61psule_filename\x18\x08 \x01(\t\x12\x15\n\rimg_icon_hash\x18\t \x01(\t\x12O\n\x0e\x65xclude_reason\x18\n \x01(\x0e\x32\x1c.ESharedLibraryExcludeReason:\x19k_ESharedLibrary_Included\x12\x18\n\x10rt_time_acquired\x18\x0b \x01(\r\x12\x16\n\x0ert_last_played\x18\x0c \x01(\r\x12\x13\n\x0brt_playtime\x18\r \x01(\r\"i\n(CFamilyGroups_SetPreferredLender_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x16\n\x0elender_steamid\x18\x03 \x01(\x06\"+\n)CFamilyGroups_SetPreferredLender_Response\"C\n)CFamilyGroups_GetPreferredLenders_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\"\xb2\x01\n*CFamilyGroups_GetPreferredLenders_Response\x12I\n\x07members\x18\x01 \x03(\x0b\x32\x38.CFamilyGroups_GetPreferredLenders_Response.FamilyMember\x1a\x39\n\x0c\x46\x61milyMember\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10preferred_appids\x18\x02 \x03(\r\"F\n,CFamilyGroups_GetDispersionForFamily_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\"\xa1\x01\n#CFamilyGroups_FamilyDispersionGraph\x12\x38\n\x05\x65\x64ges\x18\x01 \x03(\x0b\x32).CFamilyGroups_FamilyDispersionGraph.Edge\x1a@\n\x04\x45\x64ge\x12\x12\n\naccountid1\x18\x01 \x01(\r\x12\x12\n\naccountid2\x18\x02 \x01(\r\x12\x10\n\x08\x64istance\x18\x03 \x01(\x01\"~\n-CFamilyGroups_GetDispersionForFamily_Response\x12\x18\n\x10total_dispersion\x18\x01 \x01(\x01\x12\x33\n\x05graph\x18\x02 \x01(\x0b\x32$.CFamilyGroups_FamilyDispersionGraph\"\xdb\x02\n2CFamilyGroupsClient_NotifyRunningApps_Notification\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12T\n\x0crunning_apps\x18\x02 \x03(\x0b\x32>.CFamilyGroupsClient_NotifyRunningApps_Notification.RunningApp\x1a>\n\rPlayingMember\x12\x16\n\x0emember_steamid\x18\x01 \x01(\x06\x12\x15\n\rowner_steamid\x18\x02 \x01(\x06\x1aw\n\nRunningApp\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12Z\n\x0fplaying_members\x18\x03 \x03(\x0b\x32\x41.CFamilyGroupsClient_NotifyRunningApps_Notification.PlayingMember\"/\n-CFamilyGroupsClient_InviteStatus_Notification\"G\n-CFamilyGroupsClient_GroupChanged_Notification\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04*\x87\x01\n\x10\x45\x46\x61milyGroupRole\x12\x1b\n\x17k_EFamilyGroupRole_None\x10\x00\x12\x1c\n\x18k_EFamilyGroupRole_Adult\x10\x01\x12\x1c\n\x18k_EFamilyGroupRole_Child\x10\x02\x12\x1a\n\x16k_EFamilyGroupRole_MAX\x10\x03*\x99\x01\n\x1c\x45\x46\x61milyGroupsTwoFactorMethod\x12&\n\"k_EFamilyGroupsTwoFactorMethodNone\x10\x00\x12(\n$k_EFamilyGroupsTwoFactorMethodMobile\x10\x01\x12\'\n#k_EFamilyGroupsTwoFactorMethodEmail\x10\x02*\xf8\x01\n\x16\x45PurchaseRequestAction\x12!\n\x1dk_EPurchaseRequestAction_None\x10\x00\x12$\n k_EPurchaseRequestAction_Decline\x10\x01\x12&\n\"k_EPurchaseRequestAction_Purchased\x10\x02\x12&\n\"k_EPurchaseRequestAction_Abandoned\x10\x03\x12#\n\x1fk_EPurchaseRequestAction_Cancel\x10\x04\x12 \n\x1ck_EPurchaseRequestAction_MAX\x10\x05*\x9d\x05\n\x19\x45\x46\x61milyGroupChangeLogType\x12\x17\n\x13k_InvalidChangeType\x10\x00\x12\x18\n\x14k_FamilyGroupCreated\x10\x01\x12\x19\n\x15k_FamilyGroupModified\x10\x02\x12\x18\n\x14k_FamilyGroupDeleted\x10\x03\x12\x14\n\x10k_AccountInvited\x10\x04\x12\x1d\n\x19k_InviteDeniedByGroupSize\x10\x05\x12\x17\n\x13k_JoinedFamilyGroup\x10\x06\x12 \n\x1ck_JoinDeniedByRegionMismatch\x10\x07\x12\"\n\x1ek_JoinDeniedByMissingIpAddress\x10\x08\x12 \n\x1ck_JoinDeniedByFamilyCooldown\x10\t\x12\x1e\n\x1ak_JoinDeniedByUserCooldown\x10\n\x12\x1c\n\x18k_JoinDeniedByOtherGroup\x10\x0b\x12\x14\n\x10k_AccountRemoved\x10\x0c\x12\x14\n\x10k_InviteCanceled\x10\r\x12\x17\n\x13k_PurchaseRequested\x10\x0e\x12\x1d\n\x19k_ParentalSettingsEnabled\x10\x0f\x12\x1e\n\x1ak_ParentalSettingsDisabled\x10\x10\x12\x1d\n\x19k_ParentalSettingsChanged\x10\x11\x12$\n k_FamilyCooldownOverridesChanged\x10\x12\x12\x1d\n\x19k_PurchaseRequestCanceled\x10\x13\x12\x1d\n\x19k_PurchaseRequestApproved\x10\x14\x12\x1d\n\x19k_PurchaseRequestDeclined\x10\x15*\xd0\x0b\n\x1b\x45SharedLibraryExcludeReason\x12\x1d\n\x19k_ESharedLibrary_Included\x10\x00\x12*\n&k_ESharedLibrary_AppExcluded_ByPartner\x10\x01\x12$\n k_ESharedLibrary_LicenseExcluded\x10\x02\x12\x1d\n\x19k_ESharedLibrary_FreeGame\x10\x03\x12#\n\x1fk_ESharedLibrary_LicensePrivate\x10\x04\x12-\n)k_ESharedLibrary_AppExcluded_WrongAppType\x10\x06\x12\x31\n-k_ESharedLibrary_AppExcluded_NonrefundableDLC\x10\x07\x12.\n*k_ESharedLibrary_AppExcluded_UnreleasedApp\x10\x08\x12\x32\n.k_ESharedLibrary_AppExcluded_ParentAppExcluded\x10\t\x12.\n*k_ESharedLibrary_PackageExcluded_ByPartner\x10\n\x12,\n(k_ESharedLibrary_PackageExcluded_Special\x10\x0b\x12(\n$k_ESharedLibrary_PackageExcluded_Dev\x10\x0c\x12\x30\n,k_ESharedLibrary_PackageExcluded_FreeWeekend\x10\r\x12\x32\n.k_ESharedLibrary_PackageExcluded_FreePromotion\x10\x0e\x12,\n(k_ESharedLibrary_PackageExcluded_Invalid\x10\x0f\x12\x35\n1k_ESharedLibrary_PackageExcluded_RecurringLicense\x10\x10\x12\x35\n1k_ESharedLibrary_PackageExcluded_WrongLicenseType\x10\x11\x12.\n*k_ESharedLibrary_PackageExcluded_MasterSub\x10\x12\x12\x34\n0k_ESharedLibrary_PackageExcluded_NoShareableApps\x10\x13\x12\x35\n1k_ESharedLibrary_LicenseExcluded_PaymentMasterSub\x10\x14\x12\x37\n3k_ESharedLibrary_LicenseExcluded_PaymentFamilyGroup\x10\x15\x12<\n8k_ESharedLibrary_LicenseExcluded_PaymentAuthorizedDevice\x10\x16\x12\x35\n1k_ESharedLibrary_LicenseExcluded_PaymentAutoGrant\x10\x17\x12\x30\n,k_ESharedLibrary_LicenseExcluded_FlagPending\x10\x18\x12\x36\n2k_ESharedLibrary_LicenseExcluded_FlagPendingRefund\x10\x19\x12\x31\n-k_ESharedLibrary_LicenseExcluded_FlagBorrowed\x10\x1a\x12\x32\n.k_ESharedLibrary_LicenseExcluded_FlagAutoGrant\x10\x1b\x12\x33\n/k_ESharedLibrary_LicenseExcluded_FlagTimedTrial\x10\x1c\x12,\n(k_ESharedLibrary_LicenseExcluded_FreeSub\x10\x1d\x12-\n)k_ESharedLibrary_LicenseExcluded_Inactive\x10\x1e\x32\xf3\x14\n\x0c\x46\x61milyGroups\x12h\n\x11\x43reateFamilyGroup\x12(.CFamilyGroups_CreateFamilyGroup_Request\x1a).CFamilyGroups_CreateFamilyGroup_Response\x12_\n\x0eGetFamilyGroup\x12%.CFamilyGroups_GetFamilyGroup_Request\x1a&.CFamilyGroups_GetFamilyGroup_Response\x12t\n\x15GetFamilyGroupForUser\x12,.CFamilyGroups_GetFamilyGroupForUser_Request\x1a-.CFamilyGroups_GetFamilyGroupForUser_Response\x12}\n\x18ModifyFamilyGroupDetails\x12/.CFamilyGroups_ModifyFamilyGroupDetails_Request\x1a\x30.CFamilyGroups_ModifyFamilyGroupDetails_Response\x12n\n\x13InviteToFamilyGroup\x12*.CFamilyGroups_InviteToFamilyGroup_Request\x1a+.CFamilyGroups_InviteToFamilyGroup_Response\x12\x83\x01\n\x1a\x43onfirmInviteToFamilyGroup\x12\x31.CFamilyGroups_ConfirmInviteToFamilyGroup_Request\x1a\x32.CFamilyGroups_ConfirmInviteToFamilyGroup_Response\x12\x8c\x01\n\x1dResendInvitationToFamilyGroup\x12\x34.CFamilyGroups_ResendInvitationToFamilyGroup_Request\x1a\x35.CFamilyGroups_ResendInvitationToFamilyGroup_Response\x12\x62\n\x0fJoinFamilyGroup\x12&.CFamilyGroups_JoinFamilyGroup_Request\x1a\'.CFamilyGroups_JoinFamilyGroup_Response\x12w\n\x16\x43onfirmJoinFamilyGroup\x12-.CFamilyGroups_ConfirmJoinFamilyGroup_Request\x1a..CFamilyGroups_ConfirmJoinFamilyGroup_Response\x12t\n\x15RemoveFromFamilyGroup\x12,.CFamilyGroups_RemoveFromFamilyGroup_Request\x1a-.CFamilyGroups_RemoveFromFamilyGroup_Response\x12z\n\x17\x43\x61ncelFamilyGroupInvite\x12..CFamilyGroups_CancelFamilyGroupInvite_Request\x1a/.CFamilyGroups_CancelFamilyGroupInvite_Response\x12t\n\x15GetUsersSharingDevice\x12,.CFamilyGroups_GetUsersSharingDevice_Request\x1a-.CFamilyGroups_GetUsersSharingDevice_Response\x12h\n\x11\x44\x65leteFamilyGroup\x12(.CFamilyGroups_DeleteFamilyGroup_Request\x1a).CFamilyGroups_DeleteFamilyGroup_Response\x12k\n\x12GetPlaytimeSummary\x12).CFamilyGroups_GetPlaytimeSummary_Request\x1a*.CFamilyGroups_GetPlaytimeSummary_Response\x12\x62\n\x0fRequestPurchase\x12&.CFamilyGroups_RequestPurchase_Request\x1a\'.CFamilyGroups_RequestPurchase_Response\x12n\n\x13GetPurchaseRequests\x12*.CFamilyGroups_GetPurchaseRequests_Request\x1a+.CFamilyGroups_GetPurchaseRequests_Response\x12\x83\x01\n\x1aRespondToRequestedPurchase\x12\x31.CFamilyGroups_RespondToRequestedPurchase_Request\x1a\x32.CFamilyGroups_RespondToRequestedPurchase_Response\x12Y\n\x0cGetChangeLog\x12#.CFamilyGroups_GetChangeLog_Request\x1a$.CFamilyGroups_GetChangeLog_Response\x12\x83\x01\n\x1aSetFamilyCooldownOverrides\x12\x31.CFamilyGroups_SetFamilyCooldownOverrides_Request\x1a\x32.CFamilyGroups_SetFamilyCooldownOverrides_Response\x12q\n\x14GetSharedLibraryApps\x12+.CFamilyGroups_GetSharedLibraryApps_Request\x1a,.CFamilyGroups_GetSharedLibraryApps_Response\x12k\n\x12SetPreferredLender\x12).CFamilyGroups_SetPreferredLender_Request\x1a*.CFamilyGroups_SetPreferredLender_Response\x12n\n\x13GetPreferredLenders\x12*.CFamilyGroups_GetPreferredLenders_Request\x1a+.CFamilyGroups_GetPreferredLenders_Response\x12w\n\x16GetDispersionForFamily\x12-.CFamilyGroups_GetDispersionForFamily_Request\x1a..CFamilyGroups_GetDispersionForFamily_Response2\x97\x02\n\x12\x46\x61milyGroupsClient\x12U\n\x11NotifyRunningApps\x12\x33.CFamilyGroupsClient_NotifyRunningApps_Notification\x1a\x0b.NoResponse\x12Q\n\x12NotifyInviteStatus\x12..CFamilyGroupsClient_InviteStatus_Notification\x1a\x0b.NoResponse\x12Q\n\x12NotifyGroupChanged\x12..CFamilyGroupsClient_GroupChanged_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_familygroups.steamclient_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FAMILYGROUPSCLIENT']._loaded_options = None
  _globals['_FAMILYGROUPSCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_EFAMILYGROUPROLE']._serialized_start=6882
  _globals['_EFAMILYGROUPROLE']._serialized_end=7017
  _globals['_EFAMILYGROUPSTWOFACTORMETHOD']._serialized_start=7020
  _globals['_EFAMILYGROUPSTWOFACTORMETHOD']._serialized_end=7173
  _globals['_EPURCHASEREQUESTACTION']._serialized_start=7176
  _globals['_EPURCHASEREQUESTACTION']._serialized_end=7424
  _globals['_EFAMILYGROUPCHANGELOGTYPE']._serialized_start=7427
  _globals['_EFAMILYGROUPCHANGELOGTYPE']._serialized_end=8096
  _globals['_ESHAREDLIBRARYEXCLUDEREASON']._serialized_start=8099
  _globals['_ESHAREDLIBRARYEXCLUDEREASON']._serialized_end=9587
  _globals['_CFAMILYGROUPS_CREATEFAMILYGROUP_REQUEST']._serialized_start=120
  _globals['_CFAMILYGROUPS_CREATEFAMILYGROUP_REQUEST']._serialized_end=192
  _globals['_CFAMILYGROUPS_CREATEFAMILYGROUP_RESPONSE']._serialized_start=194
  _globals['_CFAMILYGROUPS_CREATEFAMILYGROUP_RESPONSE']._serialized_end=260
  _globals['_CFAMILYGROUPS_GETFAMILYGROUP_REQUEST']._serialized_start=262
  _globals['_CFAMILYGROUPS_GETFAMILYGROUP_REQUEST']._serialized_end=351
  _globals['_FAMILYGROUPMEMBER']._serialized_start=354
  _globals['_FAMILYGROUPMEMBER']._serialized_end=505
  _globals['_FAMILYGROUPPENDINGINVITE']._serialized_start=507
  _globals['_FAMILYGROUPPENDINGINVITE']._serialized_end=608
  _globals['_FAMILYGROUPFORMERMEMBER']._serialized_start=610
  _globals['_FAMILYGROUPFORMERMEMBER']._serialized_end=652
  _globals['_CFAMILYGROUPS_GETFAMILYGROUP_RESPONSE']._serialized_start=655
  _globals['_CFAMILYGROUPS_GETFAMILYGROUP_RESPONSE']._serialized_end=958
  _globals['_CFAMILYGROUPS_GETFAMILYGROUPFORUSER_REQUEST']._serialized_start=960
  _globals['_CFAMILYGROUPS_GETFAMILYGROUPFORUSER_REQUEST']._serialized_end=1061
  _globals['_FAMILYGROUPPENDINGINVITEFORUSER']._serialized_start=1064
  _globals['_FAMILYGROUPPENDINGINVITEFORUSER']._serialized_end=1204
  _globals['_CFAMILYGROUPS_GETFAMILYGROUPFORUSER_RESPONSE']._serialized_start=1207
  _globals['_CFAMILYGROUPS_GETFAMILYGROUPFORUSER_RESPONSE']._serialized_end=1556
  _globals['_CFAMILYGROUPS_MODIFYFAMILYGROUPDETAILS_REQUEST']._serialized_start=1558
  _globals['_CFAMILYGROUPS_MODIFYFAMILYGROUPDETAILS_REQUEST']._serialized_end=1644
  _globals['_CFAMILYGROUPS_MODIFYFAMILYGROUPDETAILS_RESPONSE']._serialized_start=1646
  _globals['_CFAMILYGROUPS_MODIFYFAMILYGROUPDETAILS_RESPONSE']._serialized_end=1695
  _globals['_CFAMILYGROUPS_INVITETOFAMILYGROUP_REQUEST']._serialized_start=1698
  _globals['_CFAMILYGROUPS_INVITETOFAMILYGROUP_REQUEST']._serialized_end=1858
  _globals['_CFAMILYGROUPS_INVITETOFAMILYGROUP_RESPONSE']._serialized_start=1861
  _globals['_CFAMILYGROUPS_INVITETOFAMILYGROUP_RESPONSE']._serialized_end=2018
  _globals['_CFAMILYGROUPS_CONFIRMINVITETOFAMILYGROUP_REQUEST']._serialized_start=2020
  _globals['_CFAMILYGROUPS_CONFIRMINVITETOFAMILYGROUP_REQUEST']._serialized_end=2128
  _globals['_CFAMILYGROUPS_CONFIRMINVITETOFAMILYGROUP_RESPONSE']._serialized_start=2130
  _globals['_CFAMILYGROUPS_CONFIRMINVITETOFAMILYGROUP_RESPONSE']._serialized_end=2181
  _globals['_CFAMILYGROUPS_RESENDINVITATIONTOFAMILYGROUP_REQUEST']._serialized_start=2183
  _globals['_CFAMILYGROUPS_RESENDINVITATIONTOFAMILYGROUP_REQUEST']._serialized_end=2277
  _globals['_CFAMILYGROUPS_RESENDINVITATIONTOFAMILYGROUP_RESPONSE']._serialized_start=2279
  _globals['_CFAMILYGROUPS_RESENDINVITATIONTOFAMILYGROUP_RESPONSE']._serialized_end=2333
  _globals['_CFAMILYGROUPS_JOINFAMILYGROUP_REQUEST']._serialized_start=2335
  _globals['_CFAMILYGROUPS_JOINFAMILYGROUP_REQUEST']._serialized_end=2413
  _globals['_CFAMILYGROUPS_JOINFAMILYGROUP_RESPONSE']._serialized_start=2416
  _globals['_CFAMILYGROUPS_JOINFAMILYGROUP_RESPONSE']._serialized_end=2550
  _globals['_CFAMILYGROUPS_CONFIRMJOINFAMILYGROUP_REQUEST']._serialized_start=2552
  _globals['_CFAMILYGROUPS_CONFIRMJOINFAMILYGROUP_REQUEST']._serialized_end=2656
  _globals['_CFAMILYGROUPS_CONFIRMJOINFAMILYGROUP_RESPONSE']._serialized_start=2658
  _globals['_CFAMILYGROUPS_CONFIRMJOINFAMILYGROUP_RESPONSE']._serialized_end=2705
  _globals['_CFAMILYGROUPS_REMOVEFROMFAMILYGROUP_REQUEST']._serialized_start=2707
  _globals['_CFAMILYGROUPS_REMOVEFROMFAMILYGROUP_REQUEST']._serialized_end=2803
  _globals['_CFAMILYGROUPS_REMOVEFROMFAMILYGROUP_RESPONSE']._serialized_start=2805
  _globals['_CFAMILYGROUPS_REMOVEFROMFAMILYGROUP_RESPONSE']._serialized_end=2851
  _globals['_CFAMILYGROUPS_CANCELFAMILYGROUPINVITE_REQUEST']._serialized_start=2853
  _globals['_CFAMILYGROUPS_CANCELFAMILYGROUPINVITE_REQUEST']._serialized_end=2951
  _globals['_CFAMILYGROUPS_CANCELFAMILYGROUPINVITE_RESPONSE']._serialized_start=2953
  _globals['_CFAMILYGROUPS_CANCELFAMILYGROUPINVITE_RESPONSE']._serialized_end=3001
  _globals['_CFAMILYGROUPS_GETUSERSSHARINGDEVICE_REQUEST']._serialized_start=3003
  _globals['_CFAMILYGROUPS_GETUSERSSHARINGDEVICE_REQUEST']._serialized_end=3100
  _globals['_CFAMILYGROUPS_GETUSERSSHARINGDEVICE_RESPONSE']._serialized_start=3102
  _globals['_CFAMILYGROUPS_GETUSERSSHARINGDEVICE_RESPONSE']._serialized_end=3163
  _globals['_CFAMILYGROUPS_DELETEFAMILYGROUP_REQUEST']._serialized_start=3165
  _globals['_CFAMILYGROUPS_DELETEFAMILYGROUP_REQUEST']._serialized_end=3230
  _globals['_CFAMILYGROUPS_DELETEFAMILYGROUP_RESPONSE']._serialized_start=3232
  _globals['_CFAMILYGROUPS_DELETEFAMILYGROUP_RESPONSE']._serialized_end=3274
  _globals['_CFAMILYGROUPS_GETPLAYTIMESUMMARY_REQUEST']._serialized_start=3276
  _globals['_CFAMILYGROUPS_GETPLAYTIMESUMMARY_REQUEST']._serialized_end=3342
  _globals['_CFAMILYGROUPS_PLAYTIMEENTRY']._serialized_start=3345
  _globals['_CFAMILYGROUPS_PLAYTIMEENTRY']._serialized_end=3475
  _globals['_CFAMILYGROUPS_GETPLAYTIMESUMMARY_RESPONSE']._serialized_start=3477
  _globals['_CFAMILYGROUPS_GETPLAYTIMESUMMARY_RESPONSE']._serialized_end=3567
  _globals['_CFAMILYGROUPS_REQUESTPURCHASE_REQUEST']._serialized_start=3570
  _globals['_CFAMILYGROUPS_REQUESTPURCHASE_REQUEST']._serialized_end=3712
  _globals['_CFAMILYGROUPS_REQUESTPURCHASE_RESPONSE']._serialized_start=3714
  _globals['_CFAMILYGROUPS_REQUESTPURCHASE_RESPONSE']._serialized_end=3799
  _globals['_CFAMILYGROUPS_GETPURCHASEREQUESTS_REQUEST']._serialized_start=3801
  _globals['_CFAMILYGROUPS_GETPURCHASEREQUESTS_REQUEST']._serialized_end=3925
  _globals['_PURCHASEREQUEST']._serialized_start=3928
  _globals['_PURCHASEREQUEST']._serialized_end=4313
  _globals['_CFAMILYGROUPS_GETPURCHASEREQUESTS_RESPONSE']._serialized_start=4315
  _globals['_CFAMILYGROUPS_GETPURCHASEREQUESTS_RESPONSE']._serialized_end=4395
  _globals['_CFAMILYGROUPS_RESPONDTOREQUESTEDPURCHASE_REQUEST']._serialized_start=4398
  _globals['_CFAMILYGROUPS_RESPONDTOREQUESTEDPURCHASE_REQUEST']._serialized_end=4564
  _globals['_CFAMILYGROUPS_RESPONDTOREQUESTEDPURCHASE_RESPONSE']._serialized_start=4566
  _globals['_CFAMILYGROUPS_RESPONDTOREQUESTEDPURCHASE_RESPONSE']._serialized_end=4617
  _globals['_CFAMILYGROUPS_GETCHANGELOG_REQUEST']._serialized_start=4619
  _globals['_CFAMILYGROUPS_GETCHANGELOG_REQUEST']._serialized_end=4679
  _globals['_CFAMILYGROUPS_GETCHANGELOG_RESPONSE']._serialized_start=4682
  _globals['_CFAMILYGROUPS_GETCHANGELOG_RESPONSE']._serialized_end=4931
  _globals['_CFAMILYGROUPS_GETCHANGELOG_RESPONSE_CHANGE']._serialized_start=4784
  _globals['_CFAMILYGROUPS_GETCHANGELOG_RESPONSE_CHANGE']._serialized_end=4931
  _globals['_CFAMILYGROUPS_SETFAMILYCOOLDOWNOVERRIDES_REQUEST']._serialized_start=4933
  _globals['_CFAMILYGROUPS_SETFAMILYCOOLDOWNOVERRIDES_REQUEST']._serialized_end=5031
  _globals['_CFAMILYGROUPS_SETFAMILYCOOLDOWNOVERRIDES_RESPONSE']._serialized_start=5033
  _globals['_CFAMILYGROUPS_SETFAMILYCOOLDOWNOVERRIDES_RESPONSE']._serialized_end=5084
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_REQUEST']._serialized_start=5087
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_REQUEST']._serialized_end=5238
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_RESPONSE']._serialized_start=5241
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_RESPONSE']._serialized_end=5641
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_RESPONSE_SHAREDAPP']._serialized_start=5359
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_RESPONSE_SHAREDAPP']._serialized_end=5641
  _globals['_CFAMILYGROUPS_SETPREFERREDLENDER_REQUEST']._serialized_start=5643
  _globals['_CFAMILYGROUPS_SETPREFERREDLENDER_REQUEST']._serialized_end=5748
  _globals['_CFAMILYGROUPS_SETPREFERREDLENDER_RESPONSE']._serialized_start=5750
  _globals['_CFAMILYGROUPS_SETPREFERREDLENDER_RESPONSE']._serialized_end=5793
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_REQUEST']._serialized_start=5795
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_REQUEST']._serialized_end=5862
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_RESPONSE']._serialized_start=5865
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_RESPONSE']._serialized_end=6043
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_RESPONSE_FAMILYMEMBER']._serialized_start=5986
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_RESPONSE_FAMILYMEMBER']._serialized_end=6043
  _globals['_CFAMILYGROUPS_GETDISPERSIONFORFAMILY_REQUEST']._serialized_start=6045
  _globals['_CFAMILYGROUPS_GETDISPERSIONFORFAMILY_REQUEST']._serialized_end=6115
  _globals['_CFAMILYGROUPS_FAMILYDISPERSIONGRAPH']._serialized_start=6118
  _globals['_CFAMILYGROUPS_FAMILYDISPERSIONGRAPH']._serialized_end=6279
  _globals['_CFAMILYGROUPS_FAMILYDISPERSIONGRAPH_EDGE']._serialized_start=6215
  _globals['_CFAMILYGROUPS_FAMILYDISPERSIONGRAPH_EDGE']._serialized_end=6279
  _globals['_CFAMILYGROUPS_GETDISPERSIONFORFAMILY_RESPONSE']._serialized_start=6281
  _globals['_CFAMILYGROUPS_GETDISPERSIONFORFAMILY_RESPONSE']._serialized_end=6407
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION']._serialized_start=6410
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION']._serialized_end=6757
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION_PLAYINGMEMBER']._serialized_start=6574
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION_PLAYINGMEMBER']._serialized_end=6636
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION_RUNNINGAPP']._serialized_start=6638
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION_RUNNINGAPP']._serialized_end=6757
  _globals['_CFAMILYGROUPSCLIENT_INVITESTATUS_NOTIFICATION']._serialized_start=6759
  _globals['_CFAMILYGROUPSCLIENT_INVITESTATUS_NOTIFICATION']._serialized_end=6806
  _globals['_CFAMILYGROUPSCLIENT_GROUPCHANGED_NOTIFICATION']._serialized_start=6808
  _globals['_CFAMILYGROUPSCLIENT_GROUPCHANGED_NOTIFICATION']._serialized_end=6879
  _globals['_FAMILYGROUPS']._serialized_start=9590
  _globals['_FAMILYGROUPS']._serialized_end=12265
  _globals['_FAMILYGROUPSCLIENT']._serialized_start=12268
  _globals['_FAMILYGROUPSCLIENT']._serialized_end=12547
# @@protoc_insertion_point(module_scope)
