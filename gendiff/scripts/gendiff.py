#!usr/bin/env python3
import argparse
import gendiff.scripts.parser as file_parser
import gendiff.scripts.builder as builder
import gendiff.formatters.stylish as stylish


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='json',
        help='set format of output'
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


def generate_diff(f1, f2, format='stylish'):

    f1 = file_parser.parse_file(f1)
    f2 = file_parser.parse_file(f2)
    representation = builder.build_representation(f1, f2)
    return stylish.stylish(representation)

    # result = ''
    # union_dict = dict(f1, **f2)
    # sorted_dict = sorted(union_dict, key=get_key)
    # for k in sorted_dict:
    #     if k in f1 and k in f2:
    #         if f1[k] == f2[k]:
    #             result += f'  {k}: {f1[k]}\n'
    #         else:
    #             result += f'- {k}: {f1[k]}\n'
    #             result += f'+ {k}: {f2[k]}\n'
    #     elif k in f1 and k not in f2:
    #         result += f'- {k}: {f1[k]}\n'
    #     elif k not in f1 and k in f2:
    #         result += f'+ {k}: {f2[k]}\n'
    # return '{\n' + result + '}'


if __name__ == '__main__':
    main()
