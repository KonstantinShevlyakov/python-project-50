import json
from gendiff.scripts.generate_diff import generate_diff


file_json1 = 'tests/fixtures/test_primitive_file1.json'
file_json2 = 'tests/fixtures/test_primitive_file2.json'
file_yaml1 = 'tests/fixtures/test_primitive_file1.yaml'
file_yaml2 = 'tests/fixtures/test_primitive_file2.yaml'
file_nested_json1 = 'tests/fixtures/test_nested_file1.json'
file_nested_json2 = 'tests/fixtures/test_nested_file2.json'
file_nested_yaml1 = 'tests/fixtures/test_nested_file1.yaml'
file_nested_yaml2 = 'tests/fixtures/test_nested_file2.yaml'
primitive_result = open('tests/fixtures/primitive_result.txt', 'r').read()
nested_result = open('tests/fixtures/nested_result.txt', 'r').read()
plain_result = open('tests/fixtures/plain_result.txt', 'r').read()


def test_generate_diff_json():
    assert generate_diff(file_json1, file_json2) == primitive_result


def test_generate_diff_yaml():
    assert generate_diff(file_yaml1, file_yaml2) == primitive_result


def test_generate_diff_nested_json():
    assert generate_diff(file_nested_json1, file_nested_json2) == nested_result


def test_generate_diff_nested_yaml():
    assert generate_diff(file_nested_yaml1, file_nested_yaml2) == nested_result
    

def test_generate_diff_plain():
    assert generate_diff(file_nested_json1, file_nested_json2, 'plain') == plain_result
    assert generate_diff(file_nested_yaml1, file_nested_yaml2, 'plain') == plain_result
