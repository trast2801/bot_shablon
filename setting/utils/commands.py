from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from setting.config import Secrets


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='get_file',
            description='получение файла с материалами'
        ),
        BotCommand(
            command='help',
            description='Помощь по доступным командам'
        ),
        BotCommand(
            command='about',
            description='Информация о боте'
        ),
    ]
    commands_chat = [
        BotCommand(
            command='help',
            description='помощь по доступным командам'
        ),
        BotCommand(
            command='about',
            description='Информация о боте'
        )
    ]


    await bot.set_my_commands(commands, BotCommandScopeDefault())
    await bot.set_my_commands(commands_chat, BotCommandScopeChat(chat_id=Secrets.group_id))