import asyncio
import logging

from setting.handlers import send_file
from setting.handlers.events import start_bot, stop_bot, on_user_join, on_user_left
from setting.config import bot
from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER

from setting.handlers.filter_words import check_message
from setting.utils import simple
from setting.utils.statesform import SendFileSteps


async def start():
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    # )

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(send_file.send_file_start, Command(commands='get_file'))
    dp.message.register(send_file.send_file_get_data, SendFileSteps.get_code_from_user)
    dp.message.register(simple.about_command, Command(commands='about'))
    dp.message.register(simple.help_command, Command(commands='help'))
    dp.message.register(simple.start_command, Command(commands='start'))
    dp.chat_member.register(on_user_join, ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
    dp.chat_member.register(on_user_left, ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
    dp.message.register(check_message)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


async def echo(message: Message):
    await message.answer(message.text)


if __name__ == "__main__":
    asyncio.run(start())
