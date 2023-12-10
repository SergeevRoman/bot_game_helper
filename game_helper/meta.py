import random

from yadisk import YaDisk
import telebot
from game_helper.config_executor import bot_config_access
from game_helper.leveler import points_of_dexterity, points_of_accuracy, points_of_endurance, \
    points_of_intelligence, points_of_charisma, points_of_strenght

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

def characteristics(class_of_character):
    health = random.randint(1, 6) * 100
    armor = random.randint(1, 6) * 10
    strenght = points_of_strenght(class_of_character) # сила
    dexterity = points_of_dexterity(class_of_character) # ловкость
    accuracy = points_of_accuracy(class_of_character) # меткость
    endurance = points_of_endurance(class_of_character) # выносливость
    intelligence = points_of_intelligence(class_of_character) # интеллект
    charisma = points_of_charisma(class_of_character) # харизма
    description = f'Здоровье персонажа: {health}\n'\
                  f'Защита персонажа: {armor}\n' \
                  f'Сила персонажа: {strenght}\n' \
                  f'Ловкость персонажа: {dexterity}\n' \
                  f'Меткость персонажа: {accuracy}\n' \
                  f'Выносливость персонажа: {endurance}\n' \
                  f'Интеллект персонажа: {intelligence}\n' \
                  f'Харизма персонажа: {charisma}\n'
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

