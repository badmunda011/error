from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

__mod_name__ = "ғɪʟᴛᴇʀs"

__help__ = """
**Fɪʟᴛᴇʀs**

• /ғɪʟᴛᴇʀs: Lɪsᴛ ᴀʟʟ ᴀᴄᴛɪᴠᴇ ғɪʟᴛᴇʀs sᴀᴠᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

Aᴅᴍɪɴ ᴏɴʟʏ:
• /ғɪʟᴛᴇʀ "<ᴋᴇʏᴡᴏʀᴅ>" <ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ>: Aᴅᴅ ᴀ ғɪʟᴛᴇʀ ᴛᴏ ᴛʜɪs ᴄʜᴀᴛ. Tʜᴇ ʙᴏᴛ ᴡɪʟʟ ɴᴏᴡ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴡʜᴇɴᴇᴠᴇʀ 'ᴋᴇʏᴡᴏʀᴅ'
ɪs ᴍᴇɴᴛɪᴏɴᴇᴅ. Iғ ʏᴏᴜ ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴡɪᴛʜ ᴀ ᴋᴇʏᴡᴏʀᴅ, ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴀᴛ sᴛɪᴄᴋᴇʀ.

Iғ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴋᴇʏᴡᴏʀᴅ ᴛᴏ ʙᴇ ᴀ sᴇɴᴛᴇɴᴄᴇ, ᴜsᴇ ϙᴜᴏᴛᴇs. ᴇɢ: /ғɪʟᴛᴇʀ "ʜᴇʏ ᴛʜᴇʀᴇ" Hᴏᴡ ᴀʀᴇ ʏᴏᴜ ᴅᴏɪɴ?
Exᴀᴍᴘʟᴇ:
/ғɪʟᴛᴇʀ "ғɪʟᴛᴇʀɴᴀᴍᴇ" Rᴇᴘʟʏ Tᴇxᴛ

Aʟɪᴀsᴇs ғᴏʀ ғɪʟᴛᴇʀs ᴄᴀɴ ʙᴇ ᴛᴏᴏ sᴇᴛ, ᴊᴜsᴛ ᴘᴜᴛ '|' ʙᴇᴛᴡᴇᴇɴ ᴛʜᴇ ғɪʟᴛᴇʀɴᴀᴍᴇs ʏᴏᴜ ᴡᴀɴᴛ.
Exᴀᴍᴘʟᴇ:
/ғɪʟᴛᴇʀ "ғɪʟᴛᴇʀɴᴀᴍᴇ1|ғɪʟᴛᴇʀɴᴀᴍᴇ2" Rᴇᴘʟʏ Tᴇxᴛ
Usɪɴɢ ᴛʜᴇ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴛᴇʀ ᴡᴏʀᴋ ᴏɴ 2 ғɪʟᴛᴇʀɴᴀᴍᴇs ᴡɪᴛʜᴏᴜᴛ ᴍᴀɴᴜᴀʟʟʏ ᴀᴅᴅɪɴɢ ᴀɴᴏᴛʜᴇʀ ᴏɴᴇ.

• /sᴛᴏᴘ <ғɪʟᴛᴇʀ ᴋᴇʏᴡᴏʀᴅ>: Sᴛᴏᴘ ᴛʜᴀᴛ ғɪʟᴛᴇʀ.

Nᴏᴛᴇ:
Fᴏʀ ғɪʟᴛᴇʀs ᴡɪᴛʜ ᴀʟɪᴀsᴇs, ɪғ ʏᴏᴜ sᴛᴏᴘ ᴏɴᴇ ᴀʟɪᴀs, ᴛʜᴇ ғɪʟᴛᴇʀ ᴡɪʟʟ sᴛᴏᴘ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴏᴛʜᴇʀ ᴀʟɪᴀsᴇs ᴛᴏᴏ.

Fᴏʀ Exᴀᴍᴘʟᴇ:
Iғ ʏᴏᴜ sᴛᴏᴘ ᴛʜᴇ "ғɪʟᴛᴇʀɴᴀᴍᴇ1" ғʀᴏᴍ ᴀʙᴏᴠᴇ ᴇxᴀᴍᴘʟᴇ, ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ɴᴏᴛ ʀᴇsᴘᴏɴᴅ ᴛᴏ "ғɪʟᴛᴇʀɴᴀᴍᴇ2".

Cʜᴀᴛ ᴄʀᴇᴀᴛᴏʀ ᴏɴʟʏ:
• /ʀᴇᴍᴏᴠᴇᴀʟʟғɪʟᴛᴇʀs: Rᴇᴍᴏᴠᴇ ᴀʟʟ ᴄʜᴀᴛ ғɪʟᴛᴇʀs ᴀᴛ ᴏɴᴄᴇ.

Nᴏᴛᴇ:
Cᴜʀʀᴇɴᴛʟʏ ᴛʜᴇʀᴇ ɪs ᴀ ʟɪᴍɪᴛ ᴏғ 50 ғɪʟᴛᴇʀs ᴀɴᴅ 120 ᴀʟɪᴀsᴇs ᴘᴇʀ ᴄʜᴀᴛ.
Aʟʟ ғɪʟᴛᴇʀ ᴋᴇʏᴡᴏʀᴅs ᴀʀᴇ ɪɴ ʟᴏᴡᴇʀᴄᴀsᴇ."""
 
