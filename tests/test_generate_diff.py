import json
from gendiff.scripts.gendiff import generate_diff


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'
result = open('tests/fixtures/result.txt', 'r').read()


def test_generate_diff():
    assert generate_diff(file1, file2) == result

