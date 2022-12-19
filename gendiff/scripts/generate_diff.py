#!usr/bin/env python3
# import argparse
import gendiff.cli as cli
import gendiff.parser as file_parser
import gendiff.builder as builder
import gendiff.formatters.stylish as stylish
import gendiff.formatters.plain as plain
import gendiff.formatters.json as json


def main():
    args = cli.get_args()
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format

    print(generate_diff(first_file, second_file, formatter))

# def main():
#     parser = argparse.ArgumentParser(
#         description='Compares two configuration
#         files and shows a difference.'
#     )
#     parser.add_argument('first_file', type=str)
#     parser.add_argument('second_file', type=str)
#     parser.add_argument(
#         '-f',
#         '--format',
#         type=str,
#         default='stylish',
#         help='set format of output'
#     )
#     args = parser.parse_args()
#     print(generate_diff(args.first_file, args.second_file, args.format))


def generate_diff(f1, f2, formatter='stylish'):

    f1 = file_parser.parse_file(f1)
    f2 = file_parser.parse_file(f2)
    representation = builder.build_representation(f1, f2)
    if formatter == 'json':
        return json.json_formatter(representation)
    elif formatter == 'plain':
        return plain.plain(representation)
    else:
        return stylish.stylish(representation)


if __name__ == '__main__':
    main()
