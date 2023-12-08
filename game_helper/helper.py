import telebot
from yadisk import YaDisk
from config_executor import bot_config_access
import os
from files_ids import images

TELEGRAM_TOKEN = bot_config_access('telegram_bot_token')
YANDEX_DISK_TOKEN = bot_config_access('ya_disk_token')
YANDEX_DISK_PUBLIC_FOLDER = bot_config_access('disk_public_folder')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
y = YaDisk(token=YANDEX_DISK_TOKEN)


def get_files_from_yadisk(folder_path):
    files = y.listdir(folder_path)

    return [file['name'] for file in files]


def send_image_from_yadisk(chat_id, image_name):
    p = 'https://disk.yandex.ru/i/' + images[image_name]
    bot.send_photo(chat_id, p)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я бот помощник для ролевой игры. Начинай')

@bot.message_handler(commands=["get_picture"])
def get_picture(m, res=False):
    files = get_files_from_yadisk(YANDEX_DISK_PUBLIC_FOLDER)
    if files:
        selected_file = files[0].replace('.jpg', '')
        send_image_from_yadisk(m.chat.id, 'aggressive')
    else:
        print('No files found on Yandex.Disk.')

bot.polling(none_stop=True, interval=0)

