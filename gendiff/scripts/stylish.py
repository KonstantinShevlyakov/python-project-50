#!usr/bin/env python3
from itertools import chain


def stylish(data, space_count=2):
    def iter_(data, iter):
        lines = []
        deep_size = iter + space_count
        deep_tab = deep_size * ' '
        current_tab = iter * ' '
        for k in data:
            if data[k][0] == 'added':
                lines.append(f'{current_tab} + {k}: {data[k][1]}')
            elif data[k][0] == 'unchanged':
                lines.append(f'{current_tab} - {k}: {data[k][1]}')
            elif data[k][0] == 'saved':
                lines.append(f'{current_tab}   {k}: {data[k][1]}')
            elif data[k][0] == 'two_values':
                lines.append(f'{current_tab} - {k}: {data[k][1]}')
                lines.append(f'{current_tab} + {k}: {data[k][2]}')
            elif data[k][0] == 'changed':
                lines.append(f'{deep_tab} {k}: {iter_(data[k][1], deep_size)}')

        result = chain("{", lines, [current_tab + "}"])
        return '\n'.join(result)

    return iter_(data, 0)
