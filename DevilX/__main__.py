import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DevilX import LOGGER, app, userbot
from DevilX.core.call import MXNI
from DevilX.misc import sudo
from DevilX.plugins import ALL_MODULES
from DevilX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 V2 𝐒𝐞𝐬𝐬𝐢𝐨𝐧🤬")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DevilX.plugins" + all_module)
    LOGGER("DevilX.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await MXNI.start()
    await MXNI.decorators()
    LOGGER("DevilX").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  🌪️𝐌𝐀𝐃𝐄 𝐁𝐘 𝗠𝗔𝗡𝗜 𝘅 𝗗𝗘𝗩𝗜𝗟🌪️\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DevilX").info("╔═════ஜ۩۞۩ஜ════╗\n  🌪️𝐌𝐀𝐃𝐄 𝐁𝐘 𝗠ᴀɴɪ 𝗫 𝗗ᴇᴠɪʟ🌪️\n╚═════ஜ۩۞۩ஜ════╝")
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
