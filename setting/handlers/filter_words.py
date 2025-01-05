import string

from aiogram.types import Message

from setting import views
from setting.config import BAN_WORDS, logger


async def check_message(message: Message):
    contains_ban_word = False

    if message.text:
        message_words = set(message.text.translate(str.maketrans('', '', string.punctuation)).split())
        filtered_message = message.text
        for word in message_words:
            if word.lower() in BAN_WORDS:
                filtered_message = filtered_message.replace(word, "*" * len(word))
                contains_ban_word = True

    if contains_ban_word:
        await message.delete()
        logger.info(f"Удалено сообщение от пользователя {message.from_user.username}: {message.text}")
        await message.answer_sticker('CAACAgIAAxkBAAEKbW1lGVW1I6zFVLyovwo2rSgIt1l35QADJQACYp0ISWYMy8-mubjIMAQ')
        await message.answer(views.filtered_message(message.from_user.username, filtered_message))
