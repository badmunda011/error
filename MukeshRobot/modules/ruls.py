from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

__mod_name__ = "ʀᴜʟᴇs"

__help__ = """
**Rᴜʟᴇs**

Sᴇᴛ ʀᴜʟᴇs ғᴏʀ ʏᴏᴜ ᴄʜᴀᴛ sᴏ ᴛʜᴀᴛ ᴍᴇᴍʙᴇʀs ᴋɴᴏᴡ ᴡʜᴀᴛ ᴛᴏ ᴅᴏ ᴀɴᴅ ᴡʜᴀᴛ ɴᴏᴛ ᴛᴏ ᴅᴏ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

• /ʀᴜʟᴇs: ɢᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ.

Aᴅᴍɪɴ ᴏɴʟʏ:
• /sᴇᴛʀᴜʟᴇs <ʀᴜʟᴇs>: Sᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ, ᴀʟsᴏ ᴡᴏʀᴋs ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ.
• /ᴄʟᴇᴀʀʀᴜʟᴇs: Cʟᴇᴀʀ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.
• /ᴘʀɪᴠʀᴜʟᴇs <ᴏɴ/ʏᴇs/ɴᴏ/ᴏғғ>: Tᴜʀɴs ᴏɴ/ᴏғғ ᴛʜᴇ ᴏᴘᴛɪᴏɴ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ʀᴜʟᴇs ᴛᴏ PM ᴏғ ᴜsᴇʀ ᴏʀ ɢʀᴏᴜᴘ.

Nᴏᴛᴇ Fᴏʀᴍᴀᴛ
    Cʜᴇᴄᴋ /ᴍᴀʀᴋᴅᴏᴡɴʜᴇʟᴘ ғᴏʀ ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ғᴏʀᴍᴀᴛᴛɪɴɢ!
"""
