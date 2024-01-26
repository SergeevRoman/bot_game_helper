import random

from yadisk import YaDisk
import telebot
from config_executor import bot_config_access
from character_properties import points_of_dexterity, points_of_accuracy, points_of_endurance, \
    points_of_intelligence, points_of_charisma, points_of_strenght, name_of_character, class_of_hero

TELEGRAM_TOKEN = bot_config_access('telegram_bot_token')
YANDEX_DISK_TOKEN = bot_config_access('ya_disk_token')
YANDEX_DISK_PUBLIC_FOLDER = bot_config_access('disk_public_folder')
CHAT_ID = bot_config_access('chat_id')

y = YaDisk(token=YANDEX_DISK_TOKEN)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_files_from_yadisk(folder_path):
    files = y.listdir(folder_path)
    return [file['name'] for file in files]

def send_image_from_yadisk(chat_id, image_name, text):
    if chat_id == int(CHAT_ID):
        bot.send_photo(chat_id, image_name, caption=text)
    else:
        bot.send_message(chat_id, 'Вам нельзя получать картинки!')

def characteristics(class_and_name):
    '''
    Функция создает текстовое описание характеристик персонажа
    '''
    name = name_of_character(class_and_name, 1)
    if name == '1':
        name = 'Имя не выбрано'

    class_of_chatracter = class_of_hero(class_and_name)
    health = random.randint(3, 6) * '❤'
    armor = random.randint(3, 6) * '🛡'
    strenght = points_of_strenght(class_and_name) # сила
    dexterity = points_of_dexterity(class_and_name) # ловкость
    accuracy = points_of_accuracy(class_and_name) # меткость
    endurance = points_of_endurance(class_and_name) # выносливость
    intelligence = points_of_intelligence(class_and_name) # интеллект
    charisma = points_of_charisma(class_and_name) # харизма
    description = f'{class_of_chatracter} {name}\n'\
                  f'Здоровье : {health}\n'\
                  f'Защита : {armor}\n' \
                  f'Сила : {strenght}\n' \
                  f'Ловкость : {dexterity}\n' \
                  f'Меткость : {accuracy}\n' \
                  f'Выносливость : {endurance}\n' \
                  f'Интеллект : {intelligence}\n' \
                  f'Харизма : {charisma}\n'
    return description


def meta(folder_path):
    meta = (y.get_meta(folder_path, limit = 200))
    fields = meta.FIELDS
    embedded = fields['embedded'].FIELDS
    items = embedded['items']
    dict_items = {}
    for i in range(len(items)):
        g = items[i].FIELDS
        dict_items[g['name']] = g['file']
    return dict_items

