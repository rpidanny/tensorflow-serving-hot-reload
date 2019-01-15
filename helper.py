import json


def config_parser(ordered_pairs):
    models = []
    d = {}
    for k, v in ordered_pairs:
        if (k == 'config'):
            models.append({k: v})
        else:
            d[k] = v
    if (len(models) > 0):
        return models
    else:
        return d


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
