import json

def bot_config_access(value_to_choose):
    with open('config.json') as config_file:
        config = json.load(config_file)
    value = config[value_to_choose]
    return value