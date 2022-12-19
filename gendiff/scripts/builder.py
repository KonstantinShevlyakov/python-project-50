#!usr/bin/env python3


def primitive_stringify(value, formatter):
    if formatter == 'stylish':
        if isinstance(value, dict):
            return value
        elif value is True:
            return 'true'
        elif value is False:
            return 'false'
        elif value is None:
            return 'null'
        elif value == '':
            return ''
        else:
            return str(value)
    elif formatter == 'plain':
        if isinstance(value, dict) or type(value) is int:
            return value
        elif value is True:
            return 'true'
        elif value is False:
            return 'false'
        elif value is None:
            return 'null'
        elif value == "''":
            return ''
        else:
            return f"'{str(value)}'"


def build_representation(d1, d2, formatter):
    result = {}
    unique_keys = d1.keys() | d2.keys()
    sorted_keys = sorted(unique_keys, key=lambda x: x)
    for k in sorted_keys:
        if k in d1.keys() and k not in d2.keys():
            result[k] = ('removed', primitive_stringify(d1[k], formatter))
        if k not in d1.keys() and k in d2.keys():
            result[k] = ('added', primitive_stringify(d2[k], formatter))
        if k in d1.keys() and k in d2.keys():
            if d1[k] != d2[k]:
                if isinstance(d1[k], dict) and isinstance(d2[k], dict):
                    result[k] = (
                        'nested', build_representation(d1[k], d2[k], formatter)
                    )
                else:
                    result[k] = ('changed',
                                 primitive_stringify(d1[k], formatter),
                                 primitive_stringify(d2[k], formatter))
            else:
                result[k] = ('unchanged', primitive_stringify(d1[k], formatter))
    return result
