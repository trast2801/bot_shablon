from aiogram.types import Message


def start_bot_msg():
    return 'Бот запущен'


def stop_bot_msg():
    return 'Бот остановлен'


def send_file_start_msg():
    return 'Введите код из поста'


def send_file_please_wait():
    return """Запрос обрабатывается - ожидайте"""


def send_file_not_found():
    return "файл не найден, проверьте правильность введенного кода"


def send_file_wrong_input():
    return "Неверный код файла, повторите ввод"


def about_message():
    return "о боте информация какую напишу"


def help_message():
    return "Вы находитесь здесь"

def start_message(first_name, last_name):
    if last_name == None:
        last_name = ''
    return f"{first_name} {last_name}, привет!"
    pass

def join_message(first_name):
    return f" Добро пожаловать в нашу группу {first_name}"

def left_message(first_name):
    return f'К сожалению нас покинул {first_name} '

def filtered_message(username, message):
    return (f"Очищенное сообщение от пользователя {username}:"
            f"<code>{message}</code>")