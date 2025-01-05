from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from setting import views
from setting.config import bot
from setting.utils.statesform import SendFileSteps
from setting.utils.api_actions import get_path


async def send_file_start(message: Message, state: FSMContext):
    await message.answer(views.send_file_start_msg())
    await state.set_state(SendFileSteps.get_code_from_user)

async def send_file_get_data(message: Message, state: FSMContext):
    if message.text.isdigit():
        await message.answer(views.send_file_please_wait())
        data = get_path(message.text)
        if data:
            file = FSInputFile(path=data['file_path'])
            await bot.delete_message(message.chat.id, message.message_id + 1)
            await bot.send_document(message.chat.id, document=file, caption=views.file_caption(data['title']))
            await state.clear()
        else:
            await message.answer(views.send_file_not_found())
    else:
        await message.answer(views.send_file_wrong_input())