# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_clientserver_friends.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(steammessages_clientserver_friends.proto\x1a\x18steammessages_base.proto\"\x8a\x01\n\x13\x43MsgClientFriendMsg\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x17\n\x0f\x63hat_entry_type\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\x0c\x12 \n\x18rtime32_server_timestamp\x18\x04 \x01(\x07\x12\x16\n\x0e\x65\x63ho_to_sender\x18\x05 \x01(\x08\"\x9d\x01\n\x1b\x43MsgClientFriendMsgIncoming\x12\x14\n\x0csteamid_from\x18\x01 \x01(\x06\x12\x17\n\x0f\x63hat_entry_type\x18\x02 \x01(\x05\x12\x1c\n\x14\x66rom_limited_account\x18\x03 \x01(\x08\x12\x0f\n\x07message\x18\x04 \x01(\x0c\x12 \n\x18rtime32_server_timestamp\x18\x05 \x01(\x07\"R\n\x13\x43MsgClientAddFriend\x12\x16\n\x0esteamid_to_add\x18\x01 \x01(\x06\x12#\n\x1b\x61\x63\x63ountname_or_email_to_add\x18\x02 \x01(\t\"e\n\x1b\x43MsgClientAddFriendResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x16\n\x0esteam_id_added\x18\x02 \x01(\x06\x12\x1a\n\x12persona_name_added\x18\x03 \x01(\t\"*\n\x16\x43MsgClientRemoveFriend\x12\x10\n\x08\x66riendid\x18\x01 \x01(\x06\"6\n\x14\x43MsgClientHideFriend\x12\x10\n\x08\x66riendid\x18\x01 \x01(\x06\x12\x0c\n\x04hide\x18\x02 \x01(\x08\"\xea\x01\n\x15\x43MsgClientFriendsList\x12\x14\n\x0c\x62incremental\x18\x01 \x01(\x08\x12.\n\x07\x66riends\x18\x02 \x03(\x0b\x32\x1d.CMsgClientFriendsList.Friend\x12\x18\n\x10max_friend_count\x18\x03 \x01(\r\x12\x1b\n\x13\x61\x63tive_friend_count\x18\x04 \x01(\r\x12\x19\n\x11\x66riends_limit_hit\x18\x05 \x01(\x08\x1a\x39\n\x06\x46riend\x12\x12\n\nulfriendid\x18\x01 \x01(\x06\x12\x1b\n\x13\x65\x66riendrelationship\x18\x02 \x01(\r\"\xc5\x02\n\x1b\x43MsgClientFriendsGroupsList\x12\x10\n\x08\x62removal\x18\x01 \x01(\x08\x12\x14\n\x0c\x62incremental\x18\x02 \x01(\x08\x12>\n\x0c\x66riendGroups\x18\x03 \x03(\x0b\x32(.CMsgClientFriendsGroupsList.FriendGroup\x12H\n\x0bmemberships\x18\x04 \x03(\x0b\x32\x33.CMsgClientFriendsGroupsList.FriendGroupsMembership\x1a\x35\n\x0b\x46riendGroup\x12\x10\n\x08nGroupID\x18\x01 \x01(\x05\x12\x14\n\x0cstrGroupName\x18\x02 \x01(\t\x1a=\n\x16\x46riendGroupsMembership\x12\x11\n\tulSteamID\x18\x01 \x01(\x06\x12\x10\n\x08nGroupID\x18\x02 \x01(\x05\"\xba\x01\n\x1c\x43MsgClientPlayerNicknameList\x12\x0f\n\x07removal\x18\x01 \x01(\x08\x12\x13\n\x0bincremental\x18\x02 \x01(\x08\x12?\n\tnicknames\x18\x03 \x03(\x0b\x32,.CMsgClientPlayerNicknameList.PlayerNickname\x1a\x33\n\x0ePlayerNickname\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x10\n\x08nickname\x18\x03 \x01(\t\"@\n\x1b\x43MsgClientSetPlayerNickname\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x10\n\x08nickname\x18\x02 \x01(\t\"6\n#CMsgClientSetPlayerNicknameResponse\x12\x0f\n\x07\x65result\x18\x01 \x01(\r\"O\n\x1b\x43MsgClientRequestFriendData\x12\x1f\n\x17persona_state_requested\x18\x01 \x01(\r\x12\x0f\n\x07\x66riends\x18\x02 \x03(\x06\"\xef\x01\n\x16\x43MsgClientChangeStatus\x12\x15\n\rpersona_state\x18\x01 \x01(\r\x12\x13\n\x0bplayer_name\x18\x02 \x01(\t\x12\x1e\n\x16is_auto_generated_name\x18\x03 \x01(\x08\x12\x15\n\rhigh_priority\x18\x04 \x01(\x08\x12\x1b\n\x13persona_set_by_user\x18\x05 \x01(\x08\x12\x1e\n\x13persona_state_flags\x18\x06 \x01(\r:\x01\x30\x12\x1d\n\x15need_persona_response\x18\x07 \x01(\x08\x12\x16\n\x0eis_client_idle\x18\x08 \x01(\x08\"@\n\x19\x43MsgPersonaChangeResponse\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x13\n\x0bplayer_name\x18\x02 \x01(\t\"\xa0\x08\n\x16\x43MsgClientPersonaState\x12\x14\n\x0cstatus_flags\x18\x01 \x01(\r\x12/\n\x07\x66riends\x18\x02 \x03(\x0b\x32\x1e.CMsgClientPersonaState.Friend\x1a\xbe\x07\n\x06\x46riend\x12\x10\n\x08\x66riendid\x18\x01 \x01(\x06\x12\x15\n\rpersona_state\x18\x02 \x01(\r\x12\x1a\n\x12game_played_app_id\x18\x03 \x01(\r\x12\x16\n\x0egame_server_ip\x18\x04 \x01(\r\x12\x18\n\x10game_server_port\x18\x05 \x01(\r\x12\x1b\n\x13persona_state_flags\x18\x06 \x01(\r\x12 \n\x18online_session_instances\x18\x07 \x01(\r\x12\x1b\n\x13persona_set_by_user\x18\n \x01(\x08\x12\x13\n\x0bplayer_name\x18\x0f \x01(\t\x12\x12\n\nquery_port\x18\x14 \x01(\r\x12\x16\n\x0esteamid_source\x18\x19 \x01(\x06\x12\x13\n\x0b\x61vatar_hash\x18\x1f \x01(\x0c\x12\x13\n\x0blast_logoff\x18- \x01(\r\x12\x12\n\nlast_logon\x18. \x01(\r\x12\x18\n\x10last_seen_online\x18/ \x01(\r\x12\x11\n\tclan_rank\x18\x32 \x01(\r\x12\x11\n\tgame_name\x18\x37 \x01(\t\x12\x0e\n\x06gameid\x18\x38 \x01(\x06\x12\x16\n\x0egame_data_blob\x18< \x01(\x0c\x12:\n\tclan_data\x18@ \x01(\x0b\x32\'.CMsgClientPersonaState.Friend.ClanData\x12\x10\n\x08\x63lan_tag\x18\x41 \x01(\t\x12\x38\n\rrich_presence\x18G \x03(\x0b\x32!.CMsgClientPersonaState.Friend.KV\x12\x14\n\x0c\x62roadcast_id\x18H \x01(\x06\x12\x15\n\rgame_lobby_id\x18I \x01(\x06\x12$\n\x1cwatching_broadcast_accountid\x18J \x01(\r\x12 \n\x18watching_broadcast_appid\x18K \x01(\r\x12\"\n\x1awatching_broadcast_viewers\x18L \x01(\r\x12 \n\x18watching_broadcast_title\x18M \x01(\t\x12\x1b\n\x13is_community_banned\x18N \x01(\x08\x12\"\n\x1aplayer_name_pending_review\x18O \x01(\x08\x12\x1d\n\x15\x61vatar_pending_review\x18P \x01(\x08\x1a\x35\n\x08\x43lanData\x12\x12\n\nogg_app_id\x18\x01 \x01(\r\x12\x15\n\rchat_group_id\x18\x02 \x01(\x04\x1a \n\x02KV\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"5\n\x1b\x43MsgClientFriendProfileInfo\x12\x16\n\x0esteamid_friend\x18\x01 \x01(\x06\"\xda\x01\n#CMsgClientFriendProfileInfoResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x16\n\x0esteamid_friend\x18\x02 \x01(\x06\x12\x14\n\x0ctime_created\x18\x03 \x01(\r\x12\x11\n\treal_name\x18\x04 \x01(\t\x12\x11\n\tcity_name\x18\x05 \x01(\t\x12\x12\n\nstate_name\x18\x06 \x01(\t\x12\x14\n\x0c\x63ountry_name\x18\x07 \x01(\t\x12\x10\n\x08headline\x18\x08 \x01(\t\x12\x0f\n\x07summary\x18\t \x01(\t\"[\n\x1c\x43MsgClientCreateFriendsGroup\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x11\n\tgroupname\x18\x02 \x01(\t\x12\x17\n\x0fsteamid_friends\x18\x03 \x03(\x06\"H\n$CMsgClientCreateFriendsGroupResponse\x12\x0f\n\x07\x65result\x18\x01 \x01(\r\x12\x0f\n\x07groupid\x18\x02 \x01(\x05\"@\n\x1c\x43MsgClientDeleteFriendsGroup\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x0f\n\x07groupid\x18\x02 \x01(\x05\"7\n$CMsgClientDeleteFriendsGroupResponse\x12\x0f\n\x07\x65result\x18\x01 \x01(\r\"\x82\x01\n\x1c\x43MsgClientManageFriendsGroup\x12\x0f\n\x07groupid\x18\x01 \x01(\x05\x12\x11\n\tgroupname\x18\x02 \x01(\t\x12\x1d\n\x15steamid_friends_added\x18\x03 \x03(\x06\x12\x1f\n\x17steamid_friends_removed\x18\x04 \x03(\x06\"7\n$CMsgClientManageFriendsGroupResponse\x12\x0f\n\x07\x65result\x18\x01 \x01(\r\"B\n\x1a\x43MsgClientAddFriendToGroup\x12\x0f\n\x07groupid\x18\x01 \x01(\x05\x12\x13\n\x0bsteamiduser\x18\x02 \x01(\x06\"5\n\"CMsgClientAddFriendToGroupResponse\x12\x0f\n\x07\x65result\x18\x01 \x01(\r\"G\n\x1f\x43MsgClientRemoveFriendFromGroup\x12\x0f\n\x07groupid\x18\x01 \x01(\x05\x12\x13\n\x0bsteamiduser\x18\x02 \x01(\x06\":\n\'CMsgClientRemoveFriendFromGroupResponse\x12\x0f\n\x07\x65result\x18\x01 \x01(\r\"\x1b\n\x19\x43MsgClientGetEmoticonList\"\x87\x04\n\x16\x43MsgClientEmoticonList\x12\x33\n\temoticons\x18\x01 \x03(\x0b\x32 .CMsgClientEmoticonList.Emoticon\x12\x31\n\x08stickers\x18\x02 \x03(\x0b\x32\x1f.CMsgClientEmoticonList.Sticker\x12/\n\x07\x65\x66\x66\x65\x63ts\x18\x03 \x03(\x0b\x32\x1e.CMsgClientEmoticonList.Effect\x1ax\n\x08\x45moticon\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x16\n\x0etime_last_used\x18\x03 \x01(\r\x12\x11\n\tuse_count\x18\x04 \x01(\r\x12\x15\n\rtime_received\x18\x05 \x01(\r\x12\r\n\x05\x61ppid\x18\x06 \x01(\r\x1aw\n\x07Sticker\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x15\n\rtime_received\x18\x03 \x01(\r\x12\r\n\x05\x61ppid\x18\x04 \x01(\r\x12\x16\n\x0etime_last_used\x18\x05 \x01(\r\x12\x11\n\tuse_count\x18\x06 \x01(\r\x1a\x61\n\x06\x45\x66\x66\x65\x63t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x15\n\rtime_received\x18\x03 \x01(\r\x12\x14\n\x0cinfinite_use\x18\x04 \x01(\x08\x12\r\n\x05\x61ppid\x18\x05 \x01(\rB\x05H\x01\x80\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientserver_friends_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\200\001\000'
  _globals['_CMSGCLIENTFRIENDMSG']._serialized_start=71
  _globals['_CMSGCLIENTFRIENDMSG']._serialized_end=209
  _globals['_CMSGCLIENTFRIENDMSGINCOMING']._serialized_start=212
  _globals['_CMSGCLIENTFRIENDMSGINCOMING']._serialized_end=369
  _globals['_CMSGCLIENTADDFRIEND']._serialized_start=371
  _globals['_CMSGCLIENTADDFRIEND']._serialized_end=453
  _globals['_CMSGCLIENTADDFRIENDRESPONSE']._serialized_start=455
  _globals['_CMSGCLIENTADDFRIENDRESPONSE']._serialized_end=556
  _globals['_CMSGCLIENTREMOVEFRIEND']._serialized_start=558
  _globals['_CMSGCLIENTREMOVEFRIEND']._serialized_end=600
  _globals['_CMSGCLIENTHIDEFRIEND']._serialized_start=602
  _globals['_CMSGCLIENTHIDEFRIEND']._serialized_end=656
  _globals['_CMSGCLIENTFRIENDSLIST']._serialized_start=659
  _globals['_CMSGCLIENTFRIENDSLIST']._serialized_end=893
  _globals['_CMSGCLIENTFRIENDSLIST_FRIEND']._serialized_start=836
  _globals['_CMSGCLIENTFRIENDSLIST_FRIEND']._serialized_end=893
  _globals['_CMSGCLIENTFRIENDSGROUPSLIST']._serialized_start=896
  _globals['_CMSGCLIENTFRIENDSGROUPSLIST']._serialized_end=1221
  _globals['_CMSGCLIENTFRIENDSGROUPSLIST_FRIENDGROUP']._serialized_start=1105
  _globals['_CMSGCLIENTFRIENDSGROUPSLIST_FRIENDGROUP']._serialized_end=1158
  _globals['_CMSGCLIENTFRIENDSGROUPSLIST_FRIENDGROUPSMEMBERSHIP']._serialized_start=1160
  _globals['_CMSGCLIENTFRIENDSGROUPSLIST_FRIENDGROUPSMEMBERSHIP']._serialized_end=1221
  _globals['_CMSGCLIENTPLAYERNICKNAMELIST']._serialized_start=1224
  _globals['_CMSGCLIENTPLAYERNICKNAMELIST']._serialized_end=1410
  _globals['_CMSGCLIENTPLAYERNICKNAMELIST_PLAYERNICKNAME']._serialized_start=1359
  _globals['_CMSGCLIENTPLAYERNICKNAMELIST_PLAYERNICKNAME']._serialized_end=1410
  _globals['_CMSGCLIENTSETPLAYERNICKNAME']._serialized_start=1412
  _globals['_CMSGCLIENTSETPLAYERNICKNAME']._serialized_end=1476
  _globals['_CMSGCLIENTSETPLAYERNICKNAMERESPONSE']._serialized_start=1478
  _globals['_CMSGCLIENTSETPLAYERNICKNAMERESPONSE']._serialized_end=1532
  _globals['_CMSGCLIENTREQUESTFRIENDDATA']._serialized_start=1534
  _globals['_CMSGCLIENTREQUESTFRIENDDATA']._serialized_end=1613
  _globals['_CMSGCLIENTCHANGESTATUS']._serialized_start=1616
  _globals['_CMSGCLIENTCHANGESTATUS']._serialized_end=1855
  _globals['_CMSGPERSONACHANGERESPONSE']._serialized_start=1857
  _globals['_CMSGPERSONACHANGERESPONSE']._serialized_end=1921
  _globals['_CMSGCLIENTPERSONASTATE']._serialized_start=1924
  _globals['_CMSGCLIENTPERSONASTATE']._serialized_end=2980
  _globals['_CMSGCLIENTPERSONASTATE_FRIEND']._serialized_start=2022
  _globals['_CMSGCLIENTPERSONASTATE_FRIEND']._serialized_end=2980
  _globals['_CMSGCLIENTPERSONASTATE_FRIEND_CLANDATA']._serialized_start=2893
  _globals['_CMSGCLIENTPERSONASTATE_FRIEND_CLANDATA']._serialized_end=2946
  _globals['_CMSGCLIENTPERSONASTATE_FRIEND_KV']._serialized_start=2948
  _globals['_CMSGCLIENTPERSONASTATE_FRIEND_KV']._serialized_end=2980
  _globals['_CMSGCLIENTFRIENDPROFILEINFO']._serialized_start=2982
  _globals['_CMSGCLIENTFRIENDPROFILEINFO']._serialized_end=3035
  _globals['_CMSGCLIENTFRIENDPROFILEINFORESPONSE']._serialized_start=3038
  _globals['_CMSGCLIENTFRIENDPROFILEINFORESPONSE']._serialized_end=3256
  _globals['_CMSGCLIENTCREATEFRIENDSGROUP']._serialized_start=3258
  _globals['_CMSGCLIENTCREATEFRIENDSGROUP']._serialized_end=3349
  _globals['_CMSGCLIENTCREATEFRIENDSGROUPRESPONSE']._serialized_start=3351
  _globals['_CMSGCLIENTCREATEFRIENDSGROUPRESPONSE']._serialized_end=3423
  _globals['_CMSGCLIENTDELETEFRIENDSGROUP']._serialized_start=3425
  _globals['_CMSGCLIENTDELETEFRIENDSGROUP']._serialized_end=3489
  _globals['_CMSGCLIENTDELETEFRIENDSGROUPRESPONSE']._serialized_start=3491
  _globals['_CMSGCLIENTDELETEFRIENDSGROUPRESPONSE']._serialized_end=3546
  _globals['_CMSGCLIENTMANAGEFRIENDSGROUP']._serialized_start=3549
  _globals['_CMSGCLIENTMANAGEFRIENDSGROUP']._serialized_end=3679
  _globals['_CMSGCLIENTMANAGEFRIENDSGROUPRESPONSE']._serialized_start=3681
  _globals['_CMSGCLIENTMANAGEFRIENDSGROUPRESPONSE']._serialized_end=3736
  _globals['_CMSGCLIENTADDFRIENDTOGROUP']._serialized_start=3738
  _globals['_CMSGCLIENTADDFRIENDTOGROUP']._serialized_end=3804
  _globals['_CMSGCLIENTADDFRIENDTOGROUPRESPONSE']._serialized_start=3806
  _globals['_CMSGCLIENTADDFRIENDTOGROUPRESPONSE']._serialized_end=3859
  _globals['_CMSGCLIENTREMOVEFRIENDFROMGROUP']._serialized_start=3861
  _globals['_CMSGCLIENTREMOVEFRIENDFROMGROUP']._serialized_end=3932
  _globals['_CMSGCLIENTREMOVEFRIENDFROMGROUPRESPONSE']._serialized_start=3934
  _globals['_CMSGCLIENTREMOVEFRIENDFROMGROUPRESPONSE']._serialized_end=3992
  _globals['_CMSGCLIENTGETEMOTICONLIST']._serialized_start=3994
  _globals['_CMSGCLIENTGETEMOTICONLIST']._serialized_end=4021
  _globals['_CMSGCLIENTEMOTICONLIST']._serialized_start=4024
  _globals['_CMSGCLIENTEMOTICONLIST']._serialized_end=4543
  _globals['_CMSGCLIENTEMOTICONLIST_EMOTICON']._serialized_start=4203
  _globals['_CMSGCLIENTEMOTICONLIST_EMOTICON']._serialized_end=4323
  _globals['_CMSGCLIENTEMOTICONLIST_STICKER']._serialized_start=4325
  _globals['_CMSGCLIENTEMOTICONLIST_STICKER']._serialized_end=4444
  _globals['_CMSGCLIENTEMOTICONLIST_EFFECT']._serialized_start=4446
  _globals['_CMSGCLIENTEMOTICONLIST_EFFECT']._serialized_end=4543
# @@protoc_insertion_point(module_scope)
