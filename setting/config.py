from dataclasses import dataclass
from aiogram import Bot
import logging

BAN_WORDS = set(line.strip() for line in open('res/words.txt', encoding='UTF-8'))

@dataclass
class Secrets:
    token: str = '8087031575:AAH03F-10RlTk33t4PXRMRHBM4vla3MVhh0'
    admin_id: int = 155030115
    group_id: int = -4663057803
    YANDEX_SHOP_ID = 'Ваш shopId'
    YANDEX_SECRET_KEY = 'Ваш secretKey'


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("logs.txt")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

bot = Bot(token=Secrets.token)

