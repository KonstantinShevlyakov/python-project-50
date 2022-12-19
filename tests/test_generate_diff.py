import pytest
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


@pytest.mark.parametrize('first_file', [file_json1, file_yaml1])
@pytest.mark.parametrize('second_file', [file_json2, file_yaml2])
def test_generate_diff_primitive(first_file, second_file):
    assert generate_diff(first_file, second_file) == primitive_result


@pytest.mark.parametrize('first_nested_file', [file_nested_json1, file_nested_yaml1])
@pytest.mark.parametrize('second_nested_file', [file_nested_json2, file_nested_yaml2])
def test_generate_diff_nested(first_nested_file, second_nested_file):
    assert generate_diff(first_nested_file, second_nested_file) == nested_result
    assert generate_diff(first_nested_file, second_nested_file, 'plain') == plain_result
