# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_qms.steamclient.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#steammessages_qms.steamclient.proto\x1a\x18steammessages_base.proto\x1a,steammessages_unified_base.steamclient.proto\"2\n\x0fGameSearchParam\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x03(\t\"\xe9\x01\n(CQueuedMatchmaking_SearchForGame_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12<\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x12.EGameSearchAction:\x18k_EGameSearchAction_None\x12 \n\x06params\x18\x03 \x03(\x0b\x32\x10.GameSearchParam\x12\x12\n\nplayer_min\x18\x04 \x01(\r\x12\x12\n\nplayer_max\x18\x05 \x01(\r\x12\x14\n\x0csteamidlobby\x18\x06 \x01(\x06\x12\x10\n\x08searchid\x18\x07 \x01(\x04\"\x87\x03\n)CQueuedMatchmaking_SearchForGame_Response\x12I\n\x10gamesearchresult\x18\x01 \x01(\x0e\x32\x12.EGameSearchResult:\x1bk_EGameSearchResult_Invalid\x12\x10\n\x08searchid\x18\x02 \x01(\x04\x12\x1d\n\x15seconds_time_estimate\x18\x03 \x01(\r\x12\x16\n\x0epoll_frequency\x18\x04 \x01(\r\x12\x17\n\x0f\x63ount_searching\x18\x05 \x01(\r\x12\x18\n\x10players_in_match\x18\x06 \x01(\r\x12\x18\n\x10players_accepted\x18\x07 \x01(\r\x12\x16\n\x0e\x63onnect_string\x18\t \x01(\t\x12\x13\n\x0bsteamidhost\x18\n \x01(\x06\x12\x18\n\x10rtime_match_made\x18\x0b \x01(\r\x12\x11\n\trtime_now\x18\x0c \x01(\r\x12\x1f\n\x17steamid_canceled_search\x18\r \x01(\x06\"\x97\x02\n3CQueuedMatchmakingGameHost_SearchForPlayers_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12<\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x12.EGameSearchAction:\x18k_EGameSearchAction_None\x12 \n\x06params\x18\x03 \x03(\x0b\x32\x10.GameSearchParam\x12\x12\n\nplayer_min\x18\x04 \x01(\r\x12\x12\n\nplayer_max\x18\x05 \x01(\r\x12\x1c\n\x14player_max_team_size\x18\x06 \x01(\r\x12\x19\n\x11\x63onnection_string\x18\x07 \x01(\t\x12\x10\n\x08searchid\x18\x08 \x01(\x04\"\x93\x01\n\x0bPlayerFound\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12<\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x12.EGameSearchAction:\x18k_EGameSearchAction_None\x12 \n\x06params\x18\x03 \x03(\x0b\x32\x10.GameSearchParam\x12\x13\n\x0bteam_number\x18\x04 \x01(\r\"\x88\x02\n4CQueuedMatchmakingGameHost_SearchForPlayers_Response\x12I\n\x10gamesearchresult\x18\x01 \x01(\x0e\x32\x12.EGameSearchResult:\x1bk_EGameSearchResult_Invalid\x12\x10\n\x08searchid\x18\x02 \x01(\x04\x12\x16\n\x0epoll_frequency\x18\x03 \x01(\r\x12\x0f\n\x07matchid\x18\x04 \x01(\x04\x12\x1d\n\x07players\x18\x05 \x03(\x0b\x32\x0c.PlayerFound\x12\x18\n\x10rtime_match_made\x18\x06 \x01(\r\x12\x11\n\trtime_now\x18\x07 \x01(\r\".\n\x0cPlayerResult\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\r\"~\n5CQueuedMatchmakingGameHost_SubmitPlayerResult_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07matchid\x18\x02 \x01(\x04\x12%\n\x0eplayer_results\x18\x03 \x03(\x0b\x32\r.PlayerResult\"8\n6CQueuedMatchmakingGameHost_SubmitPlayerResult_Response\"L\n*CQueuedMatchmakingGameHost_EndGame_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07matchid\x18\x02 \x01(\x04\"-\n+CQueuedMatchmakingGameHost_EndGame_Response*\x92\x01\n\x11\x45GameSearchAction\x12\x1c\n\x18k_EGameSearchAction_None\x10\x00\x12\x1e\n\x1ak_EGameSearchAction_Accept\x10\x01\x12\x1f\n\x1bk_EGameSearchAction_Decline\x10\x02\x12\x1e\n\x1ak_EGameSearchAction_Cancel\x10\x03*\xbc\x02\n\x11\x45GameSearchResult\x12\x1f\n\x1bk_EGameSearchResult_Invalid\x10\x00\x12(\n$k_EGameSearchResult_SearchInProgress\x10\x01\x12+\n\'k_EGameSearchResult_SearchFailedNoHosts\x10\x02\x12\'\n#k_EGameSearchResult_SearchGameFound\x10\x03\x12.\n*k_EGameSearchResult_SearchCompleteAccepted\x10\x04\x12.\n*k_EGameSearchResult_SearchCompleteDeclined\x10\x05\x12&\n\"k_EGameSearchResult_SearchCanceled\x10\x06\x32{\n\x11QueuedMatchmaking\x12\x66\n\rSearchForGame\x12).CQueuedMatchmaking_SearchForGame_Request\x1a*.CQueuedMatchmaking_SearchForGame_Response2\x8a\x03\n\x19QueuedMatchmakingGameHost\x12\x7f\n\x10SearchForPlayers\x12\x34.CQueuedMatchmakingGameHost_SearchForPlayers_Request\x1a\x35.CQueuedMatchmakingGameHost_SearchForPlayers_Response\x12\x85\x01\n\x12SubmitPlayerResult\x12\x36.CQueuedMatchmakingGameHost_SubmitPlayerResult_Request\x1a\x37.CQueuedMatchmakingGameHost_SubmitPlayerResult_Response\x12\x64\n\x07\x45ndGame\x12+.CQueuedMatchmakingGameHost_EndGame_Request\x1a,.CQueuedMatchmakingGameHost_EndGame_ResponseB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_qms.steamclient_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_EGAMESEARCHACTION']._serialized_start=1852
  _globals['_EGAMESEARCHACTION']._serialized_end=1998
  _globals['_EGAMESEARCHRESULT']._serialized_start=2001
  _globals['_EGAMESEARCHRESULT']._serialized_end=2317
  _globals['_GAMESEARCHPARAM']._serialized_start=111
  _globals['_GAMESEARCHPARAM']._serialized_end=161
  _globals['_CQUEUEDMATCHMAKING_SEARCHFORGAME_REQUEST']._serialized_start=164
  _globals['_CQUEUEDMATCHMAKING_SEARCHFORGAME_REQUEST']._serialized_end=397
  _globals['_CQUEUEDMATCHMAKING_SEARCHFORGAME_RESPONSE']._serialized_start=400
  _globals['_CQUEUEDMATCHMAKING_SEARCHFORGAME_RESPONSE']._serialized_end=791
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_SEARCHFORPLAYERS_REQUEST']._serialized_start=794
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_SEARCHFORPLAYERS_REQUEST']._serialized_end=1073
  _globals['_PLAYERFOUND']._serialized_start=1076
  _globals['_PLAYERFOUND']._serialized_end=1223
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_SEARCHFORPLAYERS_RESPONSE']._serialized_start=1226
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_SEARCHFORPLAYERS_RESPONSE']._serialized_end=1490
  _globals['_PLAYERRESULT']._serialized_start=1492
  _globals['_PLAYERRESULT']._serialized_end=1538
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_SUBMITPLAYERRESULT_REQUEST']._serialized_start=1540
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_SUBMITPLAYERRESULT_REQUEST']._serialized_end=1666
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_SUBMITPLAYERRESULT_RESPONSE']._serialized_start=1668
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_SUBMITPLAYERRESULT_RESPONSE']._serialized_end=1724
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_ENDGAME_REQUEST']._serialized_start=1726
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_ENDGAME_REQUEST']._serialized_end=1802
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_ENDGAME_RESPONSE']._serialized_start=1804
  _globals['_CQUEUEDMATCHMAKINGGAMEHOST_ENDGAME_RESPONSE']._serialized_end=1849
  _globals['_QUEUEDMATCHMAKING']._serialized_start=2319
  _globals['_QUEUEDMATCHMAKING']._serialized_end=2442
  _globals['_QUEUEDMATCHMAKINGGAMEHOST']._serialized_start=2445
  _globals['_QUEUEDMATCHMAKINGGAMEHOST']._serialized_end=2839
# @@protoc_insertion_point(module_scope)
