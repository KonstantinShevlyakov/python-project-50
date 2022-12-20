import json
import yaml


def read_file(filepath):
    return open(filepath, 'r')


def get_extensions(filepath):
    return filepath.split('.')[-1]


def parse(data, ext):
    if ext == 'json':
        return json.load(data)
    elif ext in ('yaml', 'yml'):
        return yaml.safe_load(data)
    raise TypeError
