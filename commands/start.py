

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import config


def start(bot, update):
    chat_id = update.message.chat.id
    keyboard = [[
        InlineKeyboardButton('Support Chat',
                             url=config.supportChatUrl)
    ],
        [
            InlineKeyboardButton('Android App Link',
                                 url=config.appUrl)
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.sendMessage(chat_id, "<b>Hi, I Can Search Torrent's From My Database For Your Query.</b>\n\n"
                             "<b>Supports Inline Mode</b> \n<b>See /help For More Info 😉</b>\n",
                    parse_mode='HTML',
                    reply_markup=reply_markup)