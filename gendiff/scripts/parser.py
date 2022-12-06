import json
import yaml


def parse_file(filepath):
    if filepath.endswith('.json'):
        return json_parse(filepath)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return yaml_parse(filepath)


def json_parse(filepath):
    return json.load(open(filepath))


def yaml_parse(filepath):
    with open(filepath, 'r') as stream:
        data = yaml.safe_load(stream)
    return data
