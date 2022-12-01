#!usr/bin/env python3
import argparse
import json


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
    print(generate_diff(args.first_file, args.second_file))


def generate_diff(f1, f2):
    def get_key(elem):
        return elem[0]

    f1 = json.load(open(f1))
    f2 = json.load(open(f2))
    result = ''
    union_dict = dict(f1, **f2)
    sorted_dict = sorted(union_dict, key=get_key)
    for k in sorted_dict:
        if k in f1 and k in f2:
            if f1[k] == f2[k]:
                result += f'\t  {k}: {f1[k]}\n'
            else:
                result += f'\t- {k}: {f1[k]}\n'
                result += f'\t+ {k}: {f2[k]}\n'
        elif k in f1 and k not in f2:
            result += f'\t- {k}: {f1[k]}\n'
        elif k not in f1 and k in f2:
            result += f'\t+ {k}: {f2[k]}\n'
    return '{\n' + result + '}'


if __name__ == '__main__':
    main()
