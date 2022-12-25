from itertools import chain
import gendiff.formatters.stringify as stringify


def plain(representation):

    def iter_(data, path):
        lines = []
        for key in data:
            current_path = path
            common_part = f'Property \'{current_path}{key}\' was'
            if data[key][0] == 'added':
                if isinstance(data[key][1], dict):
                    lines.append(
                        f'{common_part} added with value: [complex value]'
                    )
                else:
                    lines.append(
                        f'{common_part} added with value: '
                        f'{stringify.stringify(data[key][1], "plain")}'
                    )
            elif data[key][0] == 'removed':
                lines.append(f'{common_part} removed')
            elif data[key][0] == 'changed':
                if isinstance(data[key][1], dict) \
                        and not isinstance(data[key][2], dict):
                    lines.append(
                        f'{common_part} updated. From [complex value] '
                        f'to {stringify.stringify(data[key][2], "plain")}'
                    )
                elif isinstance(data[key][2], dict) \
                        and not isinstance(data[key][1], dict):
                    lines.append(
                        f'{common_part} updated. From '
                        f'{stringify.stringify(data[key][1], "plain")} '
                        f'to [complex value]'
                    )
                elif isinstance(data[key][1], dict) \
                        and isinstance(data[key][2], dict):
                    lines.append(
                        f'{common_part} updated. From [complex value] '
                        f'to [complex value]'
                    )
                else:
                    lines.append(
                        f'{common_part} updated. From '
                        f'{stringify.stringify(data[key][1], "plain")} '
                        f'to {stringify.stringify(data[key][2], "plain")}'
                    )
            elif data[key][0] == 'nested':
                lines.append(iter_(data[key][1], current_path + f'{key}.'))

            result = chain(lines)
        return '\n'.join(result)

    return iter_(representation, '')
