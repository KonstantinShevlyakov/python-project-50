import json
import yaml


def parse(data, ext):
    if ext == 'json':
        return json.load(data)
    elif ext in ('yaml', 'yml'):
        return yaml.safe_load(data)
    raise TypeError
