#!usr/bin/env python3
from itertools import chain


def stringify_dict(value, depth, space_count=2):
    if not isinstance(value, dict):
        return str(value)

    deep_size = depth + space_count
    deep_tab = deep_size * ' '
    # current_tab = depth * ' '
    lines = []
    for key, val in value.items():
        lines.append(f'{deep_tab}   {key}: '
                     f'{stringify_dict(val, deep_size + 2)}')
    result = chain("{", lines, [deep_tab + "}"])
    return '\n'.join(result)


def stylish(data, space_count=2):
    def iter_(data, iter):

        lines = []
        deep_size = iter + space_count
        # deep_tab = deep_size * ' '
        current_tab = iter * ' '
        for k in data:
            if data[k][0] == 'added':
                if isinstance(data[k][1], dict):
                    lines.append(
                        f'{current_tab} + {k}: '
                        f'{stringify_dict(data[k][1], deep_size)}'
                    )
                else:
                    lines.append(f'{current_tab} + '
                                 f'{k}: {data[k][1]}')
            elif data[k][0] == 'unchanged':
                if isinstance(data[k][1], dict):
                    lines.append(
                        f'{current_tab} - {k}: '
                        f'{stringify_dict(data[k][1], deep_size)}'
                    )
                else:
                    lines.append(f'{current_tab} - '
                                 f'{k}: {data[k][1]}')
            elif data[k][0] == 'saved':
                lines.append(f'{current_tab}   '
                             f'{k}: {data[k][1]}')
            elif data[k][0] == 'two_values':
                if isinstance(data[k][1], dict) \
                        and not isinstance(data[k][2], dict):
                    lines.append(
                        f'{current_tab} - '
                        f'{k}: {stringify_dict(data[k][1], deep_size)}')
                    lines.append(f'{current_tab} + '
                                 f'{k}: {data[k][2]}')
                elif not isinstance(data[k][1], dict) \
                        and isinstance(data[k][2], dict):
                    lines.append(f'{current_tab} - '
                                 f'{k}: {data[k][1]}')
                    lines.append(
                        f'{current_tab} + {k}: '
                        f'{stringify_dict(data[k][1], deep_size)}'
                    )
                elif isinstance(data[k][1], dict) \
                        and isinstance(data[k][2], dict):
                    lines.append(
                        f'{current_tab} - '
                        f'{k}: {stringify_dict(data[k][1], deep_size)}')
                    lines.append(
                        f'{current_tab} + '
                        f'{k}: {stringify_dict(data[k][1], deep_size)}'
                    )
                else:
                    lines.append(f'{current_tab} - {k}: {data[k][1]}')
                    lines.append(f'{current_tab} + {k}: {data[k][2]}')
            elif data[k][0] == 'changed':
                lines.append(f'{current_tab}   '
                             f'{k}: {iter_(data[k][1], deep_size + 2)}')

            result = chain("{", lines, [current_tab + "}"])
        return '\n'.join(result)

    return iter_(data, 0)
