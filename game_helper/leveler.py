import random


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