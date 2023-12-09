import random

import telebot
from yadisk import YaDisk
from config_executor import bot_config_access
from game_helper import meta
from game_helper.meta import get_files_from_yadisk, send_image_from_yadisk

TELEGRAM_TOKEN = bot_config_access('telegram_bot_token')
YANDEX_DISK_TOKEN = bot_config_access('ya_disk_token')
YANDEX_DISK_PUBLIC_FOLDER = bot_config_access('disk_public_folder')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
y = YaDisk(token=YANDEX_DISK_TOKEN)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я бот помощник для ролевой игры. Начинай')

@bot.message_handler(commands=["get_picture"])
def get_picture(m, res=False):
    items = meta.meta(YANDEX_DISK_PUBLIC_FOLDER)
    files = meta.get_files_from_yadisk(YANDEX_DISK_PUBLIC_FOLDER)
    selected_file = files[random.randint(0, len(files))]
    send_image_from_yadisk(m.chat.id, items[selected_file])

bot.polling(none_stop=True, interval=0)

