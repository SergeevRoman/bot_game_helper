import random



def class_of_hero(class_and_name):
    underscore_index = class_and_name.find('_')
    space_index = class_and_name.find(' ')
    class_of = class_and_name[underscore_index+1 : space_index]
    if class_of == 'warrior':
        return 'Воин'
    if class_of == 'archer':
        return 'Лучник'
    if class_of == 'bard':
        return 'Бард'
    if class_of == 'hunter':
        return 'Охотник'
    if class_of == 'mage':
        return 'Маг'
    if class_of == 'thief':
        return 'Вор'
def name_of_character(class_of_charachter, part_of_string):
    words = class_of_charachter.split()
    name = words[part_of_string]
    return name

def points_of_strenght(class_of_charachter):
    if 'warrior' in class_of_charachter:
        return 6
    else:
        return random.randint(1, 5)

def points_of_dexterity(class_of_charachter):
    if 'thief' in class_of_charachter:
        return 6
    else:
        return random.randint(1, 5)

def points_of_accuracy(class_of_charachter):
    if 'archer' in class_of_charachter:
        return 6
    else:
        return random.randint(1, 5)

def points_of_endurance(class_of_charachter):
    if 'hunter' in class_of_charachter:
        return 6
    else:
        return random.randint(1, 5)

def points_of_intelligence(class_of_charachter):
    if 'mage' in class_of_charachter:
        return 6
    else:
        return random.randint(1, 5)

def points_of_charisma(class_of_charachter):
    if 'bard' in class_of_charachter:
        return 6
    else:
        return random.randint(1, 5)