import pytest
from gendiff.generate_diff import generate_diff

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yaml = 'tests/fixtures/file1.yaml'
file2_yaml = 'tests/fixtures/file2.yml'
expected = 'tests/fixtures/expected.txt'
file1_nested_json = 'tests/fixtures/file_nested1.json'
file2_nested_json = 'tests/fixtures/file_nested2.json'
file1_nested_yaml = 'tests/fixtures/file_nested1.yaml'
file2_nested_yaml = 'tests/fixtures/file_nested2.yml'
expected_stylish = 'tests/fixtures/expected_stylish.txt'


@pytest.mark.parametrize(
    'path1, path2, format, expected',
    [
        (file1_json, file2_json, 'stylish', expected),
        (file1_yaml, file2_yaml, 'stylish', expected),
        (file1_nested_json, file2_nested_json, 'stylish', expected_stylish),
        (file1_nested_yaml, file2_nested_yaml, 'stylish', expected_stylish)
     ]     
)


def test_gendiff(path1, path2, format, expected):
    with open(expected) as result:
        assert generate_diff(path1, path2, format) == result.read()


def test_not_supproted_extensions():
        wrong = 'tests/fixtures/file1.txt'
        path = 'tests/fixtures/file1.json'
        with pytest.raises(NameError):
            generate_diff(wrong, path)