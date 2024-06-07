from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

__mod_name__ = "ᴡᴇʙ sᴜᴘᴘᴏʀᴛ"

__help__ = """
**Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs**
• /ʀᴍʙɢ (/ʀᴇᴍᴏᴠᴇʙɢ, /ʀᴇᴍᴏᴠᴇʙᴀᴄᴋɢʀᴏᴜɴᴅ) : Rᴇᴘʟʏ ᴛᴏ ɪᴍᴀɢᴇ ғɪʟᴇ ᴏʀ sᴛɪᴄᴋᴇʀ ᴏғ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ ʙᴀᴄᴋɢʀᴏᴜɴᴅ
• /sᴏɴɢ (/ʏᴛᴀ)  : Dᴏᴡɴʟᴏᴀᴅ ᴀᴜᴅɪᴏ ᴏɴʟʏ ғʀᴏᴍ ᴘʀᴏᴠɪᴅᴇᴅ ʏᴏᴜᴛᴜʙᴇ ᴜʀʟ
• /ᴠsᴏɴɢ (/ʏᴛᴠ)  : Dᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ᴘʀᴏᴠɪᴅᴇᴅ ʏᴏᴜᴛᴜʙᴇ ᴜʀʟ
• /ɪɢ (/ɪɴsᴛᴀɢʀᴀᴍ , /ɪɴsᴛᴀ) <ʀᴇᴇʟ's ᴜʀʟ> : Dᴏᴡɴʟᴏᴀᴅ ʀᴇᴇʟ ғʀᴏᴍ ɪᴛ's ᴜʀʟ

Bᴏᴛ ᴡɪʟʟ ɴᴏᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ sᴏɴɢ ᴏʀ ᴠɪᴅᴇᴏ ʜᴀᴠɪɴɢ ᴅᴜʀᴀᴛɪᴏɴ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 10 ᴍɪɴᴜᴛᴇs (ᴛᴏ ʀᴇᴅᴜᴄᴇ ᴛʜᴇ ʟᴏᴀᴅ ᴏɴ ʙᴏᴛ's sᴇʀᴠᴇʀ)
"""
 
