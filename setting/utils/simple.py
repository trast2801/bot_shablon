from aiogram.types import Message

from setting import views


async def about_command(message: Message):
    await message.answer(views.about_message())


async def help_command(message: Message):
    await message.answer(views.help_message())

async  def start_command(message: Message):
    await message.answer(views.start_message(message.from_user.first_name, message.from_user.last_name))
