from gendiff.parser import parse, read_file, get_extensions
import gendiff.builder as builder
import gendiff.formatters.stylish as stylish
import gendiff.formatters.plain as plain
import gendiff.formatters.json as json


def generate_diff(first_file, second_file, formatter='stylish'):

    first_data = parse(read_file(first_file), get_extensions(first_file))
    second_data = parse(read_file(second_file), get_extensions(second_file))
    representation = builder.build_representation(first_data, second_data)
    if formatter == 'json':
        return json.json_formatter(representation)
    elif formatter == 'plain':
        return plain.plain(representation)
    else:
        return stylish.stylish(representation)
