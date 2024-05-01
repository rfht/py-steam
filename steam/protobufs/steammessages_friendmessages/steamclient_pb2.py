# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_friendmessages.steamclient.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.steammessages_friendmessages.steamclient.proto\x1a\x18steammessages_base.proto\x1a,steammessages_unified_base.steamclient.proto\"\xf3\x01\n)CFriendMessages_GetRecentMessages_Request\x12\x10\n\x08steamid1\x18\x01 \x01(\x06\x12\x10\n\x08steamid2\x18\x02 \x01(\x06\x12\r\n\x05\x63ount\x18\x03 \x01(\r\x12 \n\x18most_recent_conversation\x18\x04 \x01(\x08\x12\x1a\n\x12rtime32_start_time\x18\x05 \x01(\x07\x12\x15\n\rbbcode_format\x18\x06 \x01(\x08\x12\x15\n\rstart_ordinal\x18\x07 \x01(\r\x12\x11\n\ttime_last\x18\x08 \x01(\r\x12\x14\n\x0cordinal_last\x18\t \x01(\r\"\xcf\x03\n*CFriendMessages_GetRecentMessages_Response\x12K\n\x08messages\x18\x01 \x03(\x0b\x32\x39.CFriendMessages_GetRecentMessages_Response.FriendMessage\x12\x16\n\x0emore_available\x18\x04 \x01(\x08\x1a\xbb\x02\n\rFriendMessage\x12\x11\n\taccountid\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0f\n\x07ordinal\x18\x04 \x01(\r\x12\\\n\treactions\x18\x05 \x03(\x0b\x32I.CFriendMessages_GetRecentMessages_Response.FriendMessage.MessageReaction\x1a\x83\x01\n\x0fMessageReaction\x12L\n\rreaction_type\x18\x01 \x01(\x0e\x32\x15.EMessageReactionType:\x1ek_EMessageReactionType_Invalid\x12\x10\n\x08reaction\x18\x02 \x01(\t\x12\x10\n\x08reactors\x18\x03 \x03(\r\"s\n1CFriendsMessages_GetActiveMessageSessions_Request\x12\x19\n\x11lastmessage_since\x18\x01 \x01(\r\x12#\n\x1bonly_sessions_with_messages\x18\x02 \x01(\x08\"\xa4\x02\n2CFriendsMessages_GetActiveMessageSessions_Response\x12\x62\n\x10message_sessions\x18\x01 \x03(\x0b\x32H.CFriendsMessages_GetActiveMessageSessions_Response.FriendMessageSession\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x1aw\n\x14\x46riendMessageSession\x12\x18\n\x10\x61\x63\x63ountid_friend\x18\x01 \x01(\r\x12\x14\n\x0clast_message\x18\x02 \x01(\r\x12\x11\n\tlast_view\x18\x03 \x01(\r\x12\x1c\n\x14unread_message_count\x18\x04 \x01(\r\"\xc2\x01\n#CFriendMessages_SendMessage_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x17\n\x0f\x63hat_entry_type\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x17\n\x0f\x63ontains_bbcode\x18\x04 \x01(\x08\x12\x16\n\x0e\x65\x63ho_to_sender\x18\x05 \x01(\x08\x12\x14\n\x0clow_priority\x18\x06 \x01(\x08\x12\x19\n\x11\x63lient_message_id\x18\x08 \x01(\t\"\x8c\x01\n$CFriendMessages_SendMessage_Response\x12\x18\n\x10modified_message\x18\x01 \x01(\t\x12\x18\n\x10server_timestamp\x18\x02 \x01(\r\x12\x0f\n\x07ordinal\x18\x03 \x01(\r\x12\x1f\n\x17message_without_bb_code\x18\x04 \x01(\t\"U\n\'CFriendMessages_AckMessage_Notification\x12\x17\n\x0fsteamid_partner\x18\x01 \x01(\x06\x12\x11\n\ttimestamp\x18\x02 \x01(\r\"<\n)CFriendMessages_IsInFriendsUIBeta_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"e\n*CFriendMessages_IsInFriendsUIBeta_Response\x12\x1b\n\x13online_in_friendsui\x18\x01 \x01(\x08\x12\x1a\n\x12has_used_friendsui\x18\x02 \x01(\x08\"\xdb\x01\n-CFriendMessages_UpdateMessageReaction_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10server_timestamp\x18\x02 \x01(\r\x12\x0f\n\x07ordinal\x18\x03 \x01(\r\x12L\n\rreaction_type\x18\x04 \x01(\x0e\x32\x15.EMessageReactionType:\x1ek_EMessageReactionType_Invalid\x12\x10\n\x08reaction\x18\x05 \x01(\t\x12\x0e\n\x06is_add\x18\x06 \x01(\x08\"B\n.CFriendMessages_UpdateMessageReaction_Response\x12\x10\n\x08reactors\x18\x01 \x03(\r\"\x86\x02\n,CFriendMessages_IncomingMessage_Notification\x12\x16\n\x0esteamid_friend\x18\x01 \x01(\x06\x12\x17\n\x0f\x63hat_entry_type\x18\x02 \x01(\x05\x12\x1c\n\x14\x66rom_limited_account\x18\x03 \x01(\x08\x12\x0f\n\x07message\x18\x04 \x01(\t\x12 \n\x18rtime32_server_timestamp\x18\x05 \x01(\x07\x12\x0f\n\x07ordinal\x18\x06 \x01(\r\x12\x12\n\nlocal_echo\x18\x07 \x01(\x08\x12\x19\n\x11message_no_bbcode\x18\x08 \x01(\t\x12\x14\n\x0clow_priority\x18\t \x01(\x08\"\xf2\x01\n,CFriendMessages_MessageReaction_Notification\x12\x16\n\x0esteamid_friend\x18\x01 \x01(\x06\x12\x18\n\x10server_timestamp\x18\x02 \x01(\r\x12\x0f\n\x07ordinal\x18\x03 \x01(\r\x12\x0f\n\x07reactor\x18\x04 \x01(\x06\x12L\n\rreaction_type\x18\x05 \x01(\x0e\x32\x15.EMessageReactionType:\x1ek_EMessageReactionType_Invalid\x12\x10\n\x08reaction\x18\x06 \x01(\t\x12\x0e\n\x06is_add\x18\x07 \x01(\x08*\x83\x01\n\x14\x45MessageReactionType\x12\"\n\x1ek_EMessageReactionType_Invalid\x10\x00\x12#\n\x1fk_EMessageReactionType_Emoticon\x10\x01\x12\"\n\x1ek_EMessageReactionType_Sticker\x10\x02\x32\x8d\x05\n\x0e\x46riendMessages\x12l\n\x11GetRecentMessages\x12*.CFriendMessages_GetRecentMessages_Request\x1a+.CFriendMessages_GetRecentMessages_Response\x12\x83\x01\n\x18GetActiveMessageSessions\x12\x32.CFriendsMessages_GetActiveMessageSessions_Request\x1a\x33.CFriendsMessages_GetActiveMessageSessions_Response\x12Z\n\x0bSendMessage\x12$.CFriendMessages_SendMessage_Request\x1a%.CFriendMessages_SendMessage_Response\x12\x43\n\nAckMessage\x12(.CFriendMessages_AckMessage_Notification\x1a\x0b.NoResponse\x12l\n\x11IsInFriendsUIBeta\x12*.CFriendMessages_IsInFriendsUIBeta_Request\x1a+.CFriendMessages_IsInFriendsUIBeta_Response\x12x\n\x15UpdateMessageReaction\x12..CFriendMessages_UpdateMessageReaction_Request\x1a/.CFriendMessages_UpdateMessageReaction_Response2\x89\x02\n\x14\x46riendMessagesClient\x12M\n\x0fIncomingMessage\x12-.CFriendMessages_IncomingMessage_Notification\x1a\x0b.NoResponse\x12M\n\x14NotifyAckMessageEcho\x12(.CFriendMessages_AckMessage_Notification\x1a\x0b.NoResponse\x12M\n\x0fMessageReaction\x12-.CFriendMessages_MessageReaction_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_friendmessages.steamclient_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FRIENDMESSAGESCLIENT']._loaded_options = None
  _globals['_FRIENDMESSAGESCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_EMESSAGEREACTIONTYPE']._serialized_start=2639
  _globals['_EMESSAGEREACTIONTYPE']._serialized_end=2770
  _globals['_CFRIENDMESSAGES_GETRECENTMESSAGES_REQUEST']._serialized_start=123
  _globals['_CFRIENDMESSAGES_GETRECENTMESSAGES_REQUEST']._serialized_end=366
  _globals['_CFRIENDMESSAGES_GETRECENTMESSAGES_RESPONSE']._serialized_start=369
  _globals['_CFRIENDMESSAGES_GETRECENTMESSAGES_RESPONSE']._serialized_end=832
  _globals['_CFRIENDMESSAGES_GETRECENTMESSAGES_RESPONSE_FRIENDMESSAGE']._serialized_start=517
  _globals['_CFRIENDMESSAGES_GETRECENTMESSAGES_RESPONSE_FRIENDMESSAGE']._serialized_end=832
  _globals['_CFRIENDMESSAGES_GETRECENTMESSAGES_RESPONSE_FRIENDMESSAGE_MESSAGEREACTION']._serialized_start=701
  _globals['_CFRIENDMESSAGES_GETRECENTMESSAGES_RESPONSE_FRIENDMESSAGE_MESSAGEREACTION']._serialized_end=832
  _globals['_CFRIENDSMESSAGES_GETACTIVEMESSAGESESSIONS_REQUEST']._serialized_start=834
  _globals['_CFRIENDSMESSAGES_GETACTIVEMESSAGESESSIONS_REQUEST']._serialized_end=949
  _globals['_CFRIENDSMESSAGES_GETACTIVEMESSAGESESSIONS_RESPONSE']._serialized_start=952
  _globals['_CFRIENDSMESSAGES_GETACTIVEMESSAGESESSIONS_RESPONSE']._serialized_end=1244
  _globals['_CFRIENDSMESSAGES_GETACTIVEMESSAGESESSIONS_RESPONSE_FRIENDMESSAGESESSION']._serialized_start=1125
  _globals['_CFRIENDSMESSAGES_GETACTIVEMESSAGESESSIONS_RESPONSE_FRIENDMESSAGESESSION']._serialized_end=1244
  _globals['_CFRIENDMESSAGES_SENDMESSAGE_REQUEST']._serialized_start=1247
  _globals['_CFRIENDMESSAGES_SENDMESSAGE_REQUEST']._serialized_end=1441
  _globals['_CFRIENDMESSAGES_SENDMESSAGE_RESPONSE']._serialized_start=1444
  _globals['_CFRIENDMESSAGES_SENDMESSAGE_RESPONSE']._serialized_end=1584
  _globals['_CFRIENDMESSAGES_ACKMESSAGE_NOTIFICATION']._serialized_start=1586
  _globals['_CFRIENDMESSAGES_ACKMESSAGE_NOTIFICATION']._serialized_end=1671
  _globals['_CFRIENDMESSAGES_ISINFRIENDSUIBETA_REQUEST']._serialized_start=1673
  _globals['_CFRIENDMESSAGES_ISINFRIENDSUIBETA_REQUEST']._serialized_end=1733
  _globals['_CFRIENDMESSAGES_ISINFRIENDSUIBETA_RESPONSE']._serialized_start=1735
  _globals['_CFRIENDMESSAGES_ISINFRIENDSUIBETA_RESPONSE']._serialized_end=1836
  _globals['_CFRIENDMESSAGES_UPDATEMESSAGEREACTION_REQUEST']._serialized_start=1839
  _globals['_CFRIENDMESSAGES_UPDATEMESSAGEREACTION_REQUEST']._serialized_end=2058
  _globals['_CFRIENDMESSAGES_UPDATEMESSAGEREACTION_RESPONSE']._serialized_start=2060
  _globals['_CFRIENDMESSAGES_UPDATEMESSAGEREACTION_RESPONSE']._serialized_end=2126
  _globals['_CFRIENDMESSAGES_INCOMINGMESSAGE_NOTIFICATION']._serialized_start=2129
  _globals['_CFRIENDMESSAGES_INCOMINGMESSAGE_NOTIFICATION']._serialized_end=2391
  _globals['_CFRIENDMESSAGES_MESSAGEREACTION_NOTIFICATION']._serialized_start=2394
  _globals['_CFRIENDMESSAGES_MESSAGEREACTION_NOTIFICATION']._serialized_end=2636
  _globals['_FRIENDMESSAGES']._serialized_start=2773
  _globals['_FRIENDMESSAGES']._serialized_end=3426
  _globals['_FRIENDMESSAGESCLIENT']._serialized_start=3429
  _globals['_FRIENDMESSAGESCLIENT']._serialized_end=3694
# @@protoc_insertion_point(module_scope)
