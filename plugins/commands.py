# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Há´Êá´â ð", callback_data="help_data"),
                        InlineKeyboardButton("AÊá´á´á´ ð¥", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Sá´á´á´á´Êá´ GÊá´á´á´ ð¥",
                            url="https://t.me/XRoid_Support",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Bá´á´á´ð", callback_data="start_data"),
                        InlineKeyboardButton("AÊá´á´á´ð¥", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Sá´á´á´á´Êá´ GÊá´á´á´ ð¥",
                            url="https://t.me/XRoid_Support",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Bá´á´á´ ð", callback_data="help_data"),
                        InlineKeyboardButton("Sá´á´Êá´â¡", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Sá´á´á´á´Êá´ GÊá´á´á´ ð¥",
                            url="https://t.me/XRoid_Support",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass
