from io import BytesIO
from time import sleep
from pyrogram import filters
from pyrogram.types import Message
from telegram import TelegramError, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler
import MukeshRobot.modules.no_sql.users_db as user_db 
from MukeshRobot import pbot as Mukesh
from MukeshRobot import DEV_USERS, LOGGER as  logger, OWNER_ID, dispatcher
from MukeshRobot.modules.helper_funcs.chat_status import dev_plus, sudo_plus
from MukeshRobot.modules.no_sql.users_db import get_all_users
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    UserIsBlocked,
    PeerIdInvalid,
)
import time, asyncio, logging, datetime



__mod_name__ = "ɢ-ᴄᴀsᴛ"

__help__ = """
 ❍ *ʙʀᴏᴀᴅᴄᴀsᴛ ➛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)*

 ❍ *ɴᴏᴛᴇ ➛* ᴛʜɪs sᴜᴘᴘᴏʀᴛs ʙᴀsɪᴄ ᴍᴀʀᴋᴅᴏᴡɴ

 ❍ /broadcastall *➛* ʙʀᴏᴀᴅᴄᴀsᴛs ᴇᴠᴇʀʏᴡʜᴇʀᴇ
 
 ❍ /broadcastusers *➛* ʙʀᴏᴀᴅᴄᴀsᴛs ᴛᴏᴏ ᴀʟʟ ᴜsᴇʀs
 
 ❍ /broadcastgroups *➛* ʙʀᴏᴀᴅᴄᴀsᴛs ᴛᴏᴏ ᴀʟʟ ɢʀᴏᴜᴘs
 """
