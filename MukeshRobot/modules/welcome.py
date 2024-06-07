import html
import random
import re
import time
from contextlib import suppress
from functools import partial

from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown

import MukeshRobot
import MukeshRobot.modules.sql.welcome_sql as sql
from MukeshRobot import (
    DEMONS,
    DEV_USERS,
    DRAGONS,
    EVENT_LOGS,
    LOGGER,
    OWNER_ID,
    TIGERS,
    WOLVES,
    dispatcher,
)
from MukeshRobot.modules.helper_funcs.chat_status import (
    is_user_ban_protected,
    user_admin,
)
from MukeshRobot.modules.helper_funcs.misc import build_keyboard, revert_buttons
from MukeshRobot.modules.helper_funcs.msg_types import get_welcome_type
from MukeshRobot.modules.helper_funcs.string_handling import (
    escape_invalid_curly_brackets,
    markdown_parser,
)
from MukeshRobot.modules.log_channel import loggable
from MukeshRobot.modules.sql.global_bans_sql import is_user_gbanned


__help__ = """
 ❍ /welcome <on/off>* ➛* ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs.
 ❍ /welcome *➛* sʜᴏᴡs ᴄᴜʀʀᴇɴᴛ ᴡᴇʟᴄᴏᴍᴇ sᴇᴛᴛɪɴɢs.
 ❍ /welcome  ɴᴏ ғᴏʀᴍᴀᴛ* ➛* sʜᴏᴡs ᴄᴜʀʀᴇɴᴛ ᴡᴇʟᴄᴏᴍᴇ sᴇᴛᴛɪɴɢs, ᴡɪᴛʜᴏᴜᴛ ᴛʜᴇ ғᴏʀᴍᴀᴛᴛɪɴɢ - ᴜsᴇғᴜʟ ᴛᴏ ʀᴇᴄʏᴄʟᴇ ʏᴏᴜʀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs!
 ❍ /goodbye *➛* sᴀᴍᴇ ᴜsᴀɢᴇ ᴀɴᴅ ᴀʀɢs ᴀs `/welcome`.
 ❍ /setwelcome <sᴏᴍᴇᴛᴇxᴛ>* ➛* sᴇᴛ ᴀ ᴄᴜsᴛᴏᴍ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ. ɪғ ᴜsᴇᴅ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴍᴇᴅɪᴀ, ᴜsᴇs ᴛʜᴀᴛ ᴍᴇᴅɪᴀ.
 ❍ /setgoodbye  <sᴏᴍᴇᴛᴇxᴛ>* ➛* sᴇᴛ ᴀ ᴄᴜsᴛᴏᴍ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ. ɪғ ᴜsᴇᴅ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴍᴇᴅɪᴀ, ᴜsᴇs ᴛʜᴀᴛ ᴍᴇᴅɪᴀ.
 ❍ /resetwelcome *➛* ʀᴇsᴇᴛ ᴛᴏ ᴛʜᴇ ᴅᴇғᴀᴜʟᴛ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ.
 ❍ /resetgoodbye *➛* ʀᴇsᴇᴛ ᴛᴏ ᴛʜᴇ ᴅᴇғᴀᴜʟᴛ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ.
 ❍ /cleanwelcome  <on/off>* ➛* ᴏɴ ɴᴇᴡ ᴍᴇᴍʙᴇʀ, ᴛʀʏ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜs ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ᴛʜᴇ ᴄʜᴀᴛ.
 ❍ /welcomemutehelp *➛* ɢɪᴠᴇs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴡᴇʟᴄᴏᴍᴇ ᴍᴜᴛᴇs.
 ❍ /cleanservice <on/off* ➛* ᴅᴇʟᴇᴛᴇs ᴛᴇʟᴇɢʀᴀᴍs ᴡᴇʟᴄᴏᴍᴇ/ʟᴇғᴛ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇs. 
 ❍ /welcomehelp *➛* ᴠɪᴇᴡ ᴍᴏʀᴇ ғᴏʀᴍᴀᴛᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғᴏʀ ᴄᴜsᴛᴏᴍ ᴡᴇʟᴄᴏᴍᴇ/ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇs.
"""

NEW_MEM_HANDLER = MessageHandler(
    Filters.status_update.new_chat_members, new_member, run_async=True
)
LEFT_MEM_HANDLER = MessageHandler(
    Filters.status_update.left_chat_member, left_member, run_async=True
)
WELC_PREF_HANDLER = CommandHandler(
    "welcome", welcome, filters=Filters.chat_type.groups, run_async=True
)
GOODBYE_PREF_HANDLER = CommandHandler(
    "goodbye", goodbye, filters=Filters.chat_type.groups, run_async=True
)
SET_WELCOME = CommandHandler(
    "setwelcome", set_welcome, filters=Filters.chat_type.groups, run_async=True
)
SET_GOODBYE = CommandHandler(
    "setgoodbye", set_goodbye, filters=Filters.chat_type.groups, run_async=True
)
RESET_WELCOME = CommandHandler(
    "resetwelcome", reset_welcome, filters=Filters.chat_type.groups, run_async=True
)
RESET_GOODBYE = CommandHandler(
    "resetgoodbye", reset_goodbye, filters=Filters.chat_type.groups, run_async=True
)
WELCOMEMUTE_HANDLER = CommandHandler(
    "welcomemute", welcomemute, filters=Filters.chat_type.groups, run_async=True
)
CLEAN_SERVICE_HANDLER = CommandHandler(
    "cleanservice", cleanservice, filters=Filters.chat_type.groups, run_async=True
)
CLEAN_WELCOME = CommandHandler(
    "cleanwelcome", clean_welcome, filters=Filters.chat_type.groups, run_async=True
)
WELCOME_HELP = CommandHandler("welcomehelp", welcome_help, run_async=True)
WELCOME_MUTE_HELP = CommandHandler("welcomemutehelp", welcome_mute_help, run_async=True)
BUTTON_VERIFY_HANDLER = CallbackQueryHandler(
    user_button, pattern=r"user_join_", run_async=True
)

dispatcher.add_handler(NEW_MEM_HANDLER)
dispatcher.add_handler(LEFT_MEM_HANDLER)
dispatcher.add_handler(WELC_PREF_HANDLER)
dispatcher.add_handler(GOODBYE_PREF_HANDLER)
dispatcher.add_handler(SET_WELCOME)
dispatcher.add_handler(SET_GOODBYE)
dispatcher.add_handler(RESET_WELCOME)
dispatcher.add_handler(RESET_GOODBYE)
dispatcher.add_handler(CLEAN_WELCOME)
dispatcher.add_handler(WELCOME_HELP)
dispatcher.add_handler(WELCOMEMUTE_HANDLER)
dispatcher.add_handler(CLEAN_SERVICE_HANDLER)
dispatcher.add_handler(BUTTON_VERIFY_HANDLER)
dispatcher.add_handler(WELCOME_MUTE_HELP)

__mod_name__ = "ᴡᴇʟᴄᴏᴍᴇ"
__command_list__ = []
__handlers__ = [
    NEW_MEM_HANDLER,
    LEFT_MEM_HANDLER,
    WELC_PREF_HANDLER,
    GOODBYE_PREF_HANDLER,
    SET_WELCOME,
    SET_GOODBYE,
    RESET_WELCOME,
    RESET_GOODBYE,
    CLEAN_WELCOME,
    WELCOME_HELP,
    WELCOMEMUTE_HANDLER,
    CLEAN_SERVICE_HANDLER,
    BUTTON_VERIFY_HANDLER,
    WELCOME_MUTE_HELP,
]
