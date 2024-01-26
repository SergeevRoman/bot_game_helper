import random

from config_executor import bot_config_access
from meta import get_files_from_yadisk, send_image_from_yadisk, meta

YANDEX_DISK_PUBLIC_FOLDER = bot_config_access('disk_public_folder')
def bonus():
    bonus_dict = {
        'Спой': ['Шансон песню', 'фонк песню', 'металкор песню', 'фолк песню', 'русский рок', 'песню короля и шута', 'что-нибудь популярное'],
        'Расскажи': ['анекдот', 'новость', 'рецепт', 'загадку', 'секрет', 'как прошел день', 'теорию заговора', 'историю из жизни'],
        'Изобрази': ['страх', 'удивление', 'кринж', 'удовольствие', 'сытость', 'веселье', 'грусть', 'ужас', 'живот пучит', 'омерзение'],
        'Поругай': ['еду', 'работу', 'заведение', 'правительство', 'молодежь', 'другую страну', 'политическое направление', 'тип людей'],
        'Похвали': ['пиво', 'кошек', 'болото', 'игрока рядом', 'шрека', 'погоду', 'персонажа', 'эту игру'],
        'Опиши': ['любимый мем', 'любимую игру', 'место', 'картину', 'человека', 'музыку', 'родной город', 'работу']
                  }
    random_key = random.choice(list(bonus_dict.keys()))
    random_value = random.choice(bonus_dict[random_key])
    action_for_bonus = f'Привет, скучно мне тут. {random_key} {random_value}, а я тебе подарю что-нибудь'
    return action_for_bonus


def descriptor_of_situation(type_of_situation):
    description_of_situation = ''
    skills = ['Сила', 'Ловкость', 'Меткость', 'Выносливость', 'Интеллект', 'Харизма']
    if type_of_situation == 'trixter':
        description_of_situation = 'Так так, кто тут у нас? Разгадай загадку, отгадай вопрос! Выбрать загадку ' #может быть сюда самому впихивать загадку из файла
    if type_of_situation == 'bonus':
        description_of_situation = bonus()
    if type_of_situation == 'danger':
        description_of_situation = f'проверка навыков по очереди ({random.choice(skills)} : {random.randint(1, 6)}), ({random.choice(skills)} : {random.randint(1, 6)}), ({random.choice(skills)} : {random.randint(1, 6)})',
    if type_of_situation == 'trade':
        description_of_situation = 'Это торговец. Решай - будешь с ним торговать или пойдешь мимо'
    if type_of_situation == 'help':
        description_of_situation = f'Мне нужна помощь, для этого тебе понадобится {random.choice(skills)} : {random.randint(1, 6)}'
    return description_of_situation

def descriptor_of_bonus(name_of_bonus):
    bonus_name = name_of_bonus.split('_')
    item = bonus_name[0]
    description_of_bonus = ''
    if item == 'weapon':
        description_of_bonus = f'Это оружие прибавит к твоему урону {random.randint(1, 6)} очков'
    if item == 'armor':
        description_of_bonus = f'Это прибавит к твоей защите {random.randint(1, 6)} очков'
    if item == 'amulet':
        list_of_abilities = ['силе', 'ловкости', 'меткости', 'выносливости', 'интеллекту', 'харизме']
        description_of_bonus = f'Этот амулет прибавит к твоей {list_of_abilities[random.randint(0, 5)]} {random.randint(1, 3)} очков'
    if item == 'chest':
        description_of_bonus = f'Это сундук. Открываем? /open_chest'
    if item == 'mimik':
        description_of_bonus = f'Сундук оказался опасным мимиком! Придется драться. Здоровья  у него {random.randint(1,6)*10}'
    if item == 'gold':
        description_of_bonus = f'Ты нашел {random.randint(1, 6)*100} золота'
    return description_of_bonus


def choose_place(callbak_data, chatid):
    location = f'{YANDEX_DISK_PUBLIC_FOLDER}{callbak_data}'
    items = meta(location)  # словарь из названия и ссылки изображения
    files = get_files_from_yadisk(location)  # список названий изображений из указанной папки
    selected_file = files[random.randint(0, len(files) - 1)]  # выбор случайного названия из списка
    type_of_situation = selected_file.split('_')
    description = descriptor_of_situation(type_of_situation[0])
    send_image_from_yadisk(chatid, items[selected_file], description)