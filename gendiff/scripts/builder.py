#!usr/bin/env python3


def primitive_stringify(value, format):
    if format == 'stylish':
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
    elif format == 'plain':
        if isinstance(value, dict):
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


def build_representation(d1, d2, format):
    result = {}
    unique_keys = d1.keys() | d2.keys()
    sorted_keys = sorted(unique_keys, key=lambda x: x)
    for k in sorted_keys:
        if k in d1.keys() and k not in d2.keys():
            result[k] = ('unchanged', primitive_stringify(d1[k], format))
        if k not in d1.keys() and k in d2.keys():
            result[k] = ('added', primitive_stringify(d2[k], format))
        if k in d1.keys() and k in d2.keys():
            if d1[k] != d2[k]:
                if isinstance(d1[k], dict) and isinstance(d2[k], dict):
                    result[k] = (
                        'changed', build_representation(d1[k], d2[k], format)
                    )
                else:
                    result[k] = ('two_values',
                                 primitive_stringify(d1[k], format),
                                 primitive_stringify(d2[k], format))
            else:
                result[k] = ('saved', primitive_stringify(d1[k], format))
    return result
