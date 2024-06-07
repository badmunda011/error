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


__mod_name__ = "ᴡᴇʟᴄᴏᴍ"
