from setting import views
from setting.config import bot, Secrets
from setting.utils.commands import set_commands
from setting.views import start_bot_msg, stop_bot_msg
from aiogram.types import ChatMemberUpdated


async def start_bot():
    await set_commands(bot)
    await bot.send_message(Secrets.admin_id, start_bot_msg())


async def stop_bot():
    await bot.send_message(Secrets.admin_id, stop_bot_msg())

async def on_user_join(event: ChatMemberUpdated):
    await event.answer(views.join_message(event.new_chat_member.user.first_name))


async def on_user_left(event: ChatMemberUpdated):
    await event.answer(views.left_message(event.old_chat_member.user.first_name))