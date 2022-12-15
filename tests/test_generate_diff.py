import json
from gendiff.scripts.gendiff import generate_diff


file_json1 = 'tests/fixtures/test_primitive_file1.json'
file_json2 = 'tests/fixtures/test_primitive_file2.json'
file_yaml1 = 'tests/fixtures/test_primitive_file1.yaml'
file_yaml2 = 'tests/fixtures/test_primitive_file2.yaml'
file_yml1 = 'tests/fixtures/test_primitive_file1.yml'
file_yml2 = 'tests/fixtures/test_primitive_file2.yml'
file_nested_json1 = 'tests/fixtures/test_nested_file1.json'
file_nested_json2 = 'tests/fixtures/test_nested_file2.json'
result = open('tests/fixtures/result.txt', 'r').read()


def test_generate_diff_json():
    assert generate_diff(file_json1, file_json2) == result


def test_generate_diff_yaml():
    assert generate_diff(file_yaml1, file_yaml2) == result
    assert generate_diff(file_yml1, file_yml2) == result
