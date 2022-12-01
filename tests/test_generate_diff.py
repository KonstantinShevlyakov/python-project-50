import json
from gendiff.scripts.gendiff import generate_diff


file1 = 'test_files/file1.json'
file2 = 'test_files/file2.json'
result = open('test_files/result.txt', 'r').read()


def test_generate_diff():
    assert generate_diff(file1, file2) == result

