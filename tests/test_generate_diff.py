import json
from gendiff.scripts.gendiff import generate_diff


file1 = json.load(open('/test_files/file1.json'))
file2 = json.load(open('/test_files/file2.json'))
result = open('/test_files/result.txt', 'r')


def test_generate_diff():
    assert generate_diff(file1, file2) == result

