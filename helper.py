import json


def config_parser(ordered_pairs):
    models = []
    dic = {}
    for key, val in ordered_pairs:
        if key == 'config':
            models.append({key: val})
        else:
            dic[key] = val
    if models:
        return models
    else:
        return dic


def format_config_string(config_string):
    formatted_string = config_string.replace('model_config_list: ', '')
    formatted_string = formatted_string.replace('config', '"config"')
    formatted_string = formatted_string.replace('name', '"name"')
    formatted_string = formatted_string.replace('base_path', '"base_path"')
    formatted_string = formatted_string.replace('model_platform',
                                                '"model_platform"')
    return formatted_string


def load_config(config_path):
    config_string = open(config_path).read()
    config_string = format_config_string(config_string)
    return json.loads(config_string, object_pairs_hook=config_parser)
