#!usr/bin/env python3
from itertools import chain


def plain(data):

    def iter_(data, iter):
        lines = []
        for k in data:
            current_path = iter
            if data[k][0] == 'added':
                if isinstance(data[k][1], dict):
                    lines.append(
                        f'Property \'{current_path}{k}\''
                        f' was added with value: '
                        f'[complex value]'
                    )
                else:
                    lines.append(
                        f'Property \'{current_path}{k}\''
                        f' was added with value: '
                        f'{data[k][1]}'
                    )
            elif data[k][0] == 'unchanged':
                lines.append(
                    f'Property \'{current_path}{k}\' was removed'
                )
            elif data[k][0] == 'two_values':
                if isinstance(data[k][1], dict) \
                        and not isinstance(data[k][2], dict):
                    lines.append(
                        f'Property \'{current_path}{k}\''
                        f' was updated. From [complex value] '
                        f'to {data[k][2]}'
                    )
                elif isinstance(data[k][2], dict) \
                        and not isinstance(data[k][1], dict):
                    lines.append(
                        f'Property \'{current_path}{k}\''
                        f' was updated. From {data[k][1]} '
                        f'to [complex value]'
                    )
                elif isinstance(data[k][1], dict) \
                        and isinstance(data[k][2], dict):
                    lines.append(
                        f'Property \'{current_path}{k}\''
                        f' was updated. From [complex value] '
                        f'to [complex value]'
                    )
                else:
                    lines.append(
                        f'Property \'{current_path}{k}\''
                        f' was updated. From {data[k][1]} '
                        f'to {data[k][2]}'
                    )
            elif data[k][0] == 'changed':
                lines.append(iter_(data[k][1], current_path + f'{k}.'))

            result = chain(lines)
        return '\n'.join(result)

    return iter_(data, '')
