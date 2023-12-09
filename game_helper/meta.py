from yadisk import YaDisk
import telebot
from game_helper.config_executor import bot_config_access


TELEGRAM_TOKEN = bot_config_access('telegram_bot_token')
YANDEX_DISK_TOKEN = bot_config_access('ya_disk_token')
YANDEX_DISK_PUBLIC_FOLDER = bot_config_access('disk_public_folder')

y = YaDisk(token=YANDEX_DISK_TOKEN)
bot = telebot.TeleBot(TELEGRAM_TOKEN)


class Card:
    def __init__(self, name, link):
        self.name = name
        self.link = link

def get_files_from_yadisk(folder_path):
    files = y.listdir(folder_path)
    return [file['name'] for file in files]

def send_image_from_yadisk(chat_id, image_name):
    bot.send_photo(chat_id, image_name)

def meta(folder_path):
    meta = (y.get_meta(folder_path))
    fields = meta.FIELDS
    embedded = fields['embedded'].FIELDS
    items = embedded['items']
    dict_items = {}
    for i in range(len(items)):
        g = items[i].FIELDS
        dict_items[g['name']] = g['file']
    return dict_items

meta("/gamecards")