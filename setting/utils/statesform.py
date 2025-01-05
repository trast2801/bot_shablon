from aiogram.fsm.state import StatesGroup, State


class SendFileSteps(StatesGroup):
    get_code_from_user = State()