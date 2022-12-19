#!usr/bin/env python3
from itertools import chain
import gendiff.stringify as stringify


def plain(representation):

    def iter_(data, path):
        lines = []
        for k in data:
            current_path = path
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
                        f'{stringify.stringify(data[k][1], "plain")}'
                    )
            elif data[k][0] == 'removed':
                lines.append(
                    f'Property \'{current_path}{k}\' was removed'
                )
            elif data[k][0] == 'changed':
                if isinstance(data[k][1], dict) \
                        and not isinstance(data[k][2], dict):
                    lines.append(
                        f'Property \'{current_path}{k}\''
                        f' was updated. From [complex value] '
                        f'to {stringify.stringify(data[k][2], "plain")}'
                    )
                elif isinstance(data[k][2], dict) \
                        and not isinstance(data[k][1], dict):
                    lines.append(
                        f'Property \'{current_path}{k}\''
                        f' was updated. From '
                        f'{stringify.stringify(data[k][1], "plain")} '
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
                        f' was updated. From '
                        f'{stringify.stringify(data[k][1], "plain")} '
                        f'to {stringify.stringify(data[k][2], "plain")}'
                    )
            elif data[k][0] == 'nested':
                lines.append(iter_(data[k][1], current_path + f'{k}.'))

            result = chain(lines)
        return '\n'.join(result)

    return iter_(representation, '')
