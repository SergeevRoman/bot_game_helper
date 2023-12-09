import random

import telebot
from yadisk import YaDisk
from config_executor import bot_config_access
from game_helper import meta
from game_helper.meta import get_files_from_yadisk

TELEGRAM_TOKEN = bot_config_access('telegram_bot_token')
YANDEX_DISK_TOKEN = bot_config_access('ya_disk_token')
YANDEX_DISK_PUBLIC_FOLDER = bot_config_access('disk_public_folder')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
y = YaDisk(token=YANDEX_DISK_TOKEN)


def send_image_from_yadisk(chat_id, image_name):
    p = image_name
    image = 'https://downloader.disk.yandex.ru/disk/527ee554525c34aedda4733f82b7c8b81c04c300a1da9648bcd65fe0973a2905/65747240/VXQz01F7SyF61ZFc1-2W_kj1-xqpOXzjgM3IMUrvUghOVx66VsSeKI1eYp8v3-fvvB5WuUosX4605ZcuKRjrCA%3D%3D?uid=654435540&filename=agressive.jpg&disposition=attachment&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=654435540&fsize=226468&hid=3ffd28a863d34f11e9a02634fdf041c0&media_type=image&tknv=v2&etag=40e708108017a6eba3cb9055a3fd279b'
    # дергать из объекта 'https://downloader.disk.yandex.ru/disk/8a1feb638c8e70eca28ece8898f79b8670e7447698d8a61edc022cbe47c0c5f0/657468d7/VXQz01F7SyF61ZFc1-2W_vghu09KPeWHj5IfC8gJRrNo362DCP6dRGgfhw79139qSa1q60CjRZqov4m3G77oFQ%3D%3D?uid=654435540&filename=ice_cave_ork.jpg&disposition=attachment&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=654435540&fsize=145417&hid=848e1fc7eb951c69afb1d45e3e3da4dd&media_type=image&tknv=v2&etag=06789569e672ff98034bc7271e7fb1f8'

    # как вариант отправлять такую ссылку текстом 'https://disk.yandex.ru/client/disk/gamecards?idApp=client&dialog=slider&idDialog=%2Fdisk%2Fgamecards%2Fswamp_skeleton.jpg'
    print(image)
    bot.send_photo(chat_id, image)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я бот помощник для ролевой игры. Начинай')

@bot.message_handler(commands=["get_picture"])
def get_picture(m, res=False):
    files = meta.get_files_from_yadisk(YANDEX_DISK_PUBLIC_FOLDER)
    if files:
        selected_file = files[random.randint(0, len(files))]
        send_image_from_yadisk(m.chat.id, selected_file)
    else:
        print('No files found on Yandex.Disk.')

bot.polling(none_stop=True, interval=0)

