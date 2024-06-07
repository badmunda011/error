from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

__mod_name__ = "ʀᴇᴘᴏʀᴛ"

__help__ = """
**Report**

• /report `<reason>`: reply to a message to report it to admins.
× @admin: reply to a message to report it to admins.

**NOTE:** Neither of these will get triggered if used by admins.

**Admins Only:**
• /reports `<on/off/yes/no>`: change report setting, or view current status.
    ‣ If done in PM, toggles your status.
    ‣ If in group, toggles that groups's status."""
 
