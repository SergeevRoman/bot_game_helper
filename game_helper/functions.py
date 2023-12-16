import random

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
    if type_of_situation == 'trixter':
        description_of_situation = 'Так так, кто тут у нас? Разгадай загадку, отгадай вопрос! Выбрать загадку ' #может быть сюда самому впихивать загадку из файла
    if type_of_situation == 'bonus':
        description_of_situation = bonus()
    if type_of_situation == 'danger':
        description_of_situation = 'Ты замечаешь опасность. Бросай кубик узнаем, что тебя ждет\n' \
                       '1. Проверка профильного навыка\n' \
                       '2. Использование одного из навыков\n' \
                       '3. Сразу начинается драка, враг наносит удар первым\n' \
                       '4. Сбежать\n' \
                       '5. Нанести удар первым.\n' \
                       '6. Решить самому выбрав одно из решений выше'
    if type_of_situation == 'trade':
        description_of_situation = 'Это торговец. Решай - будешь с ним торговать или пойдешь мимо'
    if type_of_situation == 'help':
        description_of_situation = 'придумать'
    return description_of_situation

def descriptor_of_bonus(name_of_bonus):
    bonus = name_of_bonus.split('_')
    item = bonus[0]
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
    return description_of_bonus


