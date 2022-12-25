from itertools import chain
import gendiff.formatters.stringify as stringify


def stringify_dict(value, depth, space_count=2):
    if not isinstance(value, dict):
        return stringify.stringify(value)

    deep_size = depth + space_count
    deep_tab = deep_size * ' '
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
        current_tab = counter * ' '
        for key in data:
            templates = {
                'added': f'{current_tab}  + {key}: ',
                'removed': f'{current_tab}  - {key}: ',
                'unchanged': f'{current_tab}    {key}: '
            }
            if data[key][0] == 'added':
                if isinstance(data[key][1], dict):
                    lines.append(
                        f'{templates["added"]}'
                        f'{stringify_dict(data[key][1], deep_size)}'
                    )
                else:
                    lines.append(f'{templates["added"]}'
                                 f'{stringify.stringify(data[key][1])}')
            elif data[key][0] == 'removed':
                if isinstance(data[key][1], dict):
                    lines.append(
                        f'{templates["removed"]}'
                        f'{stringify_dict(data[key][1], deep_size)}'
                    )
                else:
                    lines.append(f'{templates["removed"]}'
                                 f'{stringify.stringify(data[key][1])}')
            elif data[key][0] == 'unchanged':
                lines.append(f'{templates["unchanged"]}'
                             f'{stringify.stringify(data[key][1])}')
            elif data[key][0] == 'changed':
                if isinstance(data[key][1], dict) \
                        and not isinstance(data[key][2], dict):
                    lines.append(
                        f'{templates["removed"]}'
                        f'{stringify_dict(data[key][1], deep_size)}')
                    lines.append(f'{templates["added"]}'
                                 f'{stringify.stringify(data[key][2])}')
                elif not isinstance(data[key][1], dict) \
                        and isinstance(data[key][2], dict):
                    lines.append(f'{templates["removed"]}'
                                 f'{stringify.stringify(data[key][1])}')
                    lines.append(
                        f'{templates["added"]}'
                        f'{stringify_dict(data[key][2], deep_size)}'
                    )
                elif isinstance(data[key][1], dict) \
                        and isinstance(data[key][2], dict):
                    lines.append(
                        f'{templates["removed"]}'
                        f'{stringify_dict(data[key][1], deep_size)}')
                    lines.append(
                        f'{templates["added"]}'
                        f'{stringify_dict(data[key][1], deep_size)}'
                    )
                else:
                    lines.append(f'{templates["removed"]}'
                                 f'{stringify.stringify(data[key][1])}')
                    lines.append(f'{templates["added"]}'
                                 f'{stringify.stringify(data[key][2])}')
            elif data[key][0] == 'nested':
                lines.append(f'{templates["unchanged"]}'
                             f'{iter_(data[key][1], deep_size + 2)}')

            result = chain("{", lines, [current_tab + "}"])
        return '\n'.join(result)

    return iter_(representation, 0)
