#!usr/bin/env python3
import json

FIRST_FILE = json.load(open('tests/fixtures/file100.json'))
SECOND_FILE = json.load(open('tests/fixtures/file200.json'))


def diff_dicts(d1, d2, result=None):

    def get_key(elem):
        return elem

    if result is None:
        result = {}

    unique_keys = d1.keys() | d2.keys()
    sorted_keys = sorted(unique_keys, key=get_key)

    for k in sorted_keys:
        if k in d1.keys() and k not in d2.keys():
            result[k] = {'type': 'unchanged', 'value': d1[k]}
        if k not in d1.keys() and k in d2.keys():
            result[k] = {'type': 'added', 'value': d2[k]}
        if k in d1.keys() and k in d2.keys():
            if d1[k] != d2[k]:
                if isinstance(d1[k], dict) and isinstance(d2[k], dict):
                    result[k] = {'type': 'changed', 'value': diff_dicts(d1[k], d2[k])}
                else:
                    result[k] = {'type': 'two_values', 'value_first': d1[k], 'value_second': d2[k]}
            else:
                result[k] = {'type': 'saved', 'value': d1[k]}
    return result


print(diff_dicts(FIRST_FILE, SECOND_FILE))
