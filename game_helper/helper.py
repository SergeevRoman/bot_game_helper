import random
import time

import telebot
from telebot import types
from yadisk import YaDisk
from config_executor import bot_config_access
from character_properties import name_of_character
from functions import descriptor_of_bonus, choose_place
from meta import get_files_from_yadisk, send_image_from_yadisk, meta, characteristics

TELEGRAM_TOKEN = bot_config_access('telegram_bot_token')
YANDEX_DISK_TOKEN = bot_config_access('ya_disk_token')
YANDEX_DISK_PUBLIC_FOLDER = bot_config_access('disk_public_folder')
YANDEX_DISK_AVATARS = bot_config_access('disk_avatars')
YANDEX_DISK_BONUSES = bot_config_access('disk_bonuses')
YANDEX_DISK_CONTENT_OF_CHESTS = bot_config_access('disk_chest')


bot = telebot.TeleBot(TELEGRAM_TOKEN)
y = YaDisk(token=YANDEX_DISK_TOKEN)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я бот помощник для ролевой игры. Начинай')

@bot.message_handler(commands=['get_situation'])
def get_situation(m):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton("Мост", callback_data='bridge')
    item2 = types.InlineKeyboardButton("Замок", callback_data='castle')
    item3 = types.InlineKeyboardButton("Катакомбы", callback_data='catacombs')
    item4 = types.InlineKeyboardButton("Пещера", callback_data='cave')
    item5 = types.InlineKeyboardButton("Пустыня", callback_data='desert')
    item6 = types.InlineKeyboardButton("Лес", callback_data='forest')
    item7 = types.InlineKeyboardButton("Лесной дом", callback_data='forest_house')
    item8 = types.InlineKeyboardButton("Ледяная пещера", callback_data='iced_lake')
    item9 = types.InlineKeyboardButton("Горы", callback_data='mountains')
    item10 = types.InlineKeyboardButton("Порт", callback_data='port')
    item11 = types.InlineKeyboardButton("Руины", callback_data='ruins')
    item12 = types.InlineKeyboardButton("Берег", callback_data='shore')
    item13 = types.InlineKeyboardButton("Болото", callback_data='swamp')
    item14 = types.InlineKeyboardButton("Лабиринт", callback_data='maze')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14)
    bot.send_message(m.chat.id, "Выбери куда пойти:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    choose_place(call.data, call.message.chat.id)

# @bot.message_handler(commands=["get_situation_old"])
# def menu_of_locations(message, res=False):
#     bot.register_next_step_handler(message, get_situation)
#     answer = 'Отправь ответом на это сообщение одну из локаций: \nbridge\ncastle\ncatacombs\ncave\ndesert\nforest\nforest_house\n' \
#              'ice_cave\niced_lake\nmountains\nport\nruins\nshore\nswamp\nmaze'
#     bot.send_message(message.chat.id, answer)
#
#
# def get_situation(m):
#     chosen_location = m.text
#     location = f'{YANDEX_DISK_PUBLIC_FOLDER}{chosen_location}'
#     items = meta(location) # словарь из названия и ссылки изображения
#     files = get_files_from_yadisk(location) # список названий изображений из указанной папки
#     selected_file = files[random.randint(0, len(files)-1)] # выбор случайного названия из списка
#     type_of_situation = selected_file.split('_')
#     description = descriptor_of_situation(type_of_situation[0])
#     send_image_from_yadisk(m.chat.id, items[selected_file], description)

@bot.message_handler(commands=["choose_pers"])
def menu_of_avatars(message, res=False):
    bot.register_next_step_handler(message, choose_avatar)
    answer = 'Отправь ответом на это сообщение один из вариантов и имя персонажа: man_archer\nman_bard\nman_hunter\nman_mage\nman_thief\n' \
             'man_warrior\nwoman_archer\nwoman_bard\nwoman_hunter\nwoman_mage\nwoman_thief\nwoman_warrior  '
    bot.send_message(message.chat.id, answer)
def choose_avatar(m):
    choosen_avatar = m.text
    if len(choosen_avatar.split()) == 1:
        choosen_avatar = choosen_avatar + ' 1'
    numbers = ['01', '02']
    name_of_file = name_of_character(choosen_avatar, 0) # Имя аватара
    avatar_for_gamer = f'{name_of_file}_{random.choice(numbers)}.jpg' # Выбор одного из двух аватаров
    avatars = meta(YANDEX_DISK_AVATARS) # словарь доступных аватаров
    description_of_character = characteristics(choosen_avatar) # создание описания персонажа
    send_image_from_yadisk(m.chat.id, avatars[avatar_for_gamer], description_of_character)

@bot.message_handler(commands=["get_bonus"])
def get_bonus(m):
    menu_of_bonuses = get_files_from_yadisk(YANDEX_DISK_BONUSES)
    bonuses = meta(YANDEX_DISK_BONUSES)
    random_bonus = random.choice(menu_of_bonuses)
    description_of_bonus = descriptor_of_bonus(random_bonus)
    send_image_from_yadisk(m.chat.id, bonuses[random_bonus], description_of_bonus)

@bot.message_handler(commands=["open_chest"])
def open_chest(m):
    menu_of_content = get_files_from_yadisk(YANDEX_DISK_CONTENT_OF_CHESTS)
    contents = meta(YANDEX_DISK_CONTENT_OF_CHESTS)
    random_content = random.choice(menu_of_content)
    description_of_content = descriptor_of_bonus(random_content)
    send_image_from_yadisk(m.chat.id, contents[random_content], description_of_content)


# @bot.message_handler(commands=["get_picture"])
# def get_picture(m, res=False):
#     items = meta.meta(YANDEX_DISK_PUBLIC_FOLDER)
#     files = meta.get_files_from_yadisk(YANDEX_DISK_PUBLIC_FOLDER)
#     selected_file = files[random.randint(0, len(files))]
#     send_image_from_yadisk(m.chat.id, items[selected_file])


# bot.polling(none_stop=True, timeout=123)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, timeout=123)
        except Exception as e:
            time.sleep(3)
            print(e)
