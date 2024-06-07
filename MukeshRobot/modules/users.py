from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler
from MukeshRobot.modules.helper_funcs.chat_status import dev_plus, sudo_plus




__mod_name__ = "ɢ-ᴄᴀsᴛ"

__help__ = """
 ❍ *ʙʀᴏᴀᴅᴄᴀsᴛ ➛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)*

 ❍ *ɴᴏᴛᴇ ➛* ᴛʜɪs sᴜᴘᴘᴏʀᴛs ʙᴀsɪᴄ ᴍᴀʀᴋᴅᴏᴡɴ

 ❍ /broadcastall *➛* ʙʀᴏᴀᴅᴄᴀsᴛs ᴇᴠᴇʀʏᴡʜᴇʀᴇ

 ❍ /broadcast *➛* ᴍsɢ -ᴀʟʟ -ᴘɪɴ
 
 ❍ /broadcastusers *➛* ʙʀᴏᴀᴅᴄᴀsᴛs ᴛᴏᴏ ᴀʟʟ ᴜsᴇʀs
 
 ❍ /broadcastgroups *➛* ʙʀᴏᴀᴅᴄᴀsᴛs ᴛᴏᴏ ᴀʟʟ ɢʀᴏᴜᴘs
 """
