#!usr/bin/env python3
import gendiff.cli as cli
from gendiff.differ import generate_diff


def main():
    args = cli.get_args()
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format
    print(generate_diff(first_file, second_file, formatter))


if __name__ == '__main__':
    main()
