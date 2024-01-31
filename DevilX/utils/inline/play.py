import math

from pyrogram.types import InlineKeyboardButton

from DevilX.utils.formatters import time_to_seconds

from DevilX import app

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [

        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            ],
            [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(text="Replay", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="End", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        
    ]

    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 15:
        bar = "◈▱▱▱▱▱▱▱"
    elif 15 < umm < 30:
        bar = "▰◈▱▱▱▱▱▱"
    elif 30 <= umm < 45:
        bar = "▰▰◈▱▱▱▱▱"
    elif 45 <= umm < 60:
        bar = "▰▰▰◈▱▱▱▱"
    elif 60 <= umm < 75:
        bar = "▰▰▰▰◈▱▱▱"
    elif 75 <= umm < 90:
        bar = "▰▰▰▰▰◈▱▱"
    elif 90 <= umm < 105:
        bar = "▰▰▰▰▰▰◈▱"
    else:
        bar = "▰▰▰▰▰▰▰◈"
        
    buttons  = [
          [
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⏸️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏭️", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⏹️", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="**sᴘᴇᴇᴅ**", callback_data="SPEED_BTN"),
        ],
        [
            InlineKeyboardButton(text="𐏓 ⃪⃝🇺🇸 ꯭𝗗ᴇᴠɪ𝗟 ꯭༎ࠫ⛧‌", url="https://t.me/ll_mxni_ll"),
            InlineKeyboardButton(text="⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂⎯꯭ ꯭̽🌸", url="https://t.me/II_BAD_BBY_II"),
        ],
    ]


def stream_markup(_, chat_id):
    buttons  = [

        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
          ],
          [
            InlineKeyboardButton(
                text="ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="𐏓 ⃪⃝🇺🇸 ꯭𝗗ᴇᴠɪ𝗟 ꯭༎ࠫ⛧‌", url="https://t.me/ll_mxni_ll"),
            InlineKeyboardButton(text="⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂⎯꯭ ꯭̽🌸", url="https://t.me/II_BAD_BBY_II"),
        ],
            
    ]

    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"VIPPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"VIPPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
           InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),

        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
           InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),

        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
     ]
    return buttons

        
## Queue Markup

def queue_markup(_, videoid, chat_id):

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            ],
            [
            InlineKeyboardButton(
                text="ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"⛦ ᴊᴏɪɴ ⛦",
              url="https://t.me/Devils_Hell_0",
            ),
        ],
    ]

    return buttons
