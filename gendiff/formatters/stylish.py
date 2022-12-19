#!usr/bin/env python3
from itertools import chain
import gendiff.stringify as stringify


def stringify_dict(value, depth, space_count=2):
    if not isinstance(value, dict):
        return stringify.stringify(value)

    deep_size = depth + space_count
    deep_tab = deep_size * ' '
    # current_tab = depth * ' '
    lines = []
    for key, val in value.items():
        lines.append(f'{deep_tab}    {key}: '
                     f'{stringify_dict(val, deep_size + 2)}')
    result = chain("{", lines, [deep_tab + "}"])
    return '\n'.join(result)


def stylish(representation, space_count=2):
    def iter_(data, counter):

        lines = []
        deep_size = counter + space_count
        # deep_tab = deep_size * ' '
        current_tab = counter * ' '
        for k in data:
            if data[k][0] == 'added':
                if isinstance(data[k][1], dict):
                    lines.append(
                        f'{current_tab}  + {k}: '
                        f'{stringify_dict(data[k][1], deep_size)}'
                    )
                else:
                    lines.append(f'{current_tab}  + '
                                 f'{k}: {stringify.stringify(data[k][1])}')
            elif data[k][0] == 'removed':
                if isinstance(data[k][1], dict):
                    lines.append(
                        f'{current_tab}  - {k}: '
                        f'{stringify_dict(data[k][1], deep_size)}'
                    )
                else:
                    lines.append(f'{current_tab}  - '
                                 f'{k}: {stringify.stringify(data[k][1])}')
            elif data[k][0] == 'unchanged':
                lines.append(f'{current_tab}    '
                             f'{k}: {stringify.stringify(data[k][1])}')
            elif data[k][0] == 'changed':
                if isinstance(data[k][1], dict) \
                        and not isinstance(data[k][2], dict):
                    lines.append(
                        f'{current_tab}  - '
                        f'{k}: {stringify_dict(data[k][1], deep_size)}')
                    lines.append(f'{current_tab}  + '
                                 f'{k}: {stringify.stringify(data[k][2])}')
                elif not isinstance(data[k][1], dict) \
                        and isinstance(data[k][2], dict):
                    lines.append(f'{current_tab}  - '
                                 f'{k}: {stringify.stringify(data[k][1])}')
                    lines.append(
                        f'{current_tab}  + {k}: '
                        f'{stringify_dict(data[k][2], deep_size)}'
                    )
                elif isinstance(data[k][1], dict) \
                        and isinstance(data[k][2], dict):
                    lines.append(
                        f'{current_tab}  - '
                        f'{k}: {stringify_dict(data[k][1], deep_size)}')
                    lines.append(
                        f'{current_tab}  + '
                        f'{k}: {stringify_dict(data[k][1], deep_size)}'
                    )
                else:
                    lines.append(f'{current_tab}  - {k}: '
                                 f'{stringify.stringify(data[k][1])}')
                    lines.append(f'{current_tab}  + {k}: '
                                 f'{stringify.stringify(data[k][2])}')
            elif data[k][0] == 'nested':
                lines.append(f'{current_tab}    '
                             f'{k}: {iter_(data[k][1], deep_size + 2)}')

            result = chain("{", lines, [current_tab + "}"])
        return '\n'.join(result)

    return iter_(representation, 0)
