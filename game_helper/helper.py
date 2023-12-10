import random

import telebot
from yadisk import YaDisk
from config_executor import bot_config_access
from game_helper import meta
from game_helper.meta import get_files_from_yadisk, send_image_from_yadisk

TELEGRAM_TOKEN = bot_config_access('telegram_bot_token')
YANDEX_DISK_TOKEN = bot_config_access('ya_disk_token')
YANDEX_DISK_PUBLIC_FOLDER = bot_config_access('disk_public_folder')
YANDEX_DISK_AVATARS = bot_config_access('disk_avatars')

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
    description = 'твоя ситуация'
    send_image_from_yadisk(m.chat.id, items[selected_file], description)

@bot.message_handler(commands=["choose_pers"])
def menu_of_avatars(message, res=False):
    bot.register_next_step_handler(message, choose_avatar)
    answer = 'Отправь ответом на это сообщение один из вариантов: man_archer\nman_bard\nman_hunter\nman_mage\nman_thief\n' \
             'man_warrior\nwoman_archer\nwoman_bard\nwoman_hunter\nwoman_mage\nwoman_thief\nwoman_warrior  '
    bot.send_message(message.chat.id, answer)
def choose_avatar(m):
    choosen_avatar = m.text
    numbers =['01','02']
    avatar_for_gamer = f'{choosen_avatar}_{random.choice(numbers)}.jpg'
    avatars = meta.meta(YANDEX_DISK_AVATARS)
    names_of_avatars = meta.get_files_from_yadisk(YANDEX_DISK_AVATARS)
    # avatar = names_of_avatars[random.randint(0, len(avatars))]
    characteristics = meta.characteristics(choosen_avatar)
    send_image_from_yadisk(m.chat.id, avatars[avatar_for_gamer], characteristics)


# @bot.message_handler(commands=["get_picture"])
# def get_picture(m, res=False):
#     items = meta.meta(YANDEX_DISK_PUBLIC_FOLDER)
#     files = meta.get_files_from_yadisk(YANDEX_DISK_PUBLIC_FOLDER)
#     selected_file = files[random.randint(0, len(files))]
#     send_image_from_yadisk(m.chat.id, items[selected_file])

bot.polling(none_stop=True, interval=0)

