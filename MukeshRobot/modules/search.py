from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

__mod_name__ = "sᴇᴀʀᴄʜ"

__help__ = """
**Sᴇᴀʀᴄʜ**

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /ɢᴏᴏɢʟᴇ <ϙᴜᴇʀʏ> : Sᴇᴀʀᴄʜ ᴛʜᴇ ɢᴏᴏɢʟᴇ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ϙᴜᴇʀʏ.
• /ᴀɴɪᴍᴇ <ϙᴜᴇʀʏ>  : Sᴇᴀʀᴄʜ ᴍʏᴀɴɪᴍᴇʟɪsᴛ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ϙᴜᴇʀʏ.
• /sᴛᴀᴄᴋ <ϙᴜᴇʀʏ>  : Sᴇᴀʀᴄʜ sᴛᴀᴄᴋᴏᴠᴇʀғʟᴏᴡ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ϙᴜᴇʀʏ.
• /ɪᴍᴀɢᴇs (/ɪᴍɢs) <ϙᴜᴇʀʏ> : Gᴇᴛ ᴛʜᴇ ɪᴍᴀɢᴇs ʀᴇɢᴀʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ϙᴜᴇʀʏ

Exᴀᴍᴘʟᴇ:
/ɢᴏᴏɢʟᴇ ᴘʏʀᴏɢʀᴀᴍ: ʀᴇᴛᴜʀɴ ᴛᴏᴘ 5 ʀᴇᴜsʟᴛs.
"""
