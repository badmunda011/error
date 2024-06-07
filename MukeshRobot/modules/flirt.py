from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

__mod_name__ = "ғɪʟᴛᴇʀss"

__help__ = """
**Fɪʟᴛᴇʀs**
 ❍ /filters* ➛* ʟɪsᴛ ᴀʟʟ ᴀᴄᴛɪᴠᴇ ғɪʟᴛᴇʀs sᴀᴠᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

✿ *ᴀᴅᴍɪɴ ᴏɴʟʏ* ✿
 ❍ /filter <ᴋᴇʏᴡᴏʀᴅ> <ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ>* ➛* ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ᴛᴏ ᴛʜɪs ᴄʜᴀᴛ. ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ɴᴏᴡ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴡʜᴇɴᴇᴠᴇʀ 'ᴋᴇʏᴡᴏʀᴅ'\
 ❍ /stop  <ғɪʟᴛᴇʀ ᴋᴇʏᴡᴏʀᴅ>* ➛* sᴛᴏᴘ ᴛʜᴀᴛ ғɪʟᴛᴇʀ.

✿ *ᴄʜᴀᴛ ᴄʀᴇᴀᴛᴏʀ ᴏɴʟʏ* ✿ 

 ❍ /removeallfilters* ➛* ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴄʜᴀᴛ ғɪʟᴛᴇʀs ᴀᴛ ᴏɴᴄᴇ.

❍ *ɴᴏᴛᴇ* ➛ ғɪʟᴛᴇʀs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛᴛᴇʀs ʟɪᴋᴇ: {ғɪʀsᴛ}, {ʟᴀsᴛ} ᴇᴛᴄ.. ᴀɴᴅ ʙᴜᴛᴛᴏɴs.
❍ ᴄʜᴇᴄᴋ /markdownhelp ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ!

"""

