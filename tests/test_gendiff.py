import pytest
from gendiff.generate_diff import generate_diff

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
expected_json = 'tests/fixtures/expected1.txt'


@pytest.mark.parametrize(
    'path1, path2, expected',
    [(file1_json, file2_json, expected_json)]     
)


def test_gendiff(path1, path2, expected):
    with open(expected) as result:
        assert generate_diff(path1, path2) == result.read()


def test_not_supproted_extensions():
        wrong = 'tests/fixtures/file1.txt'
        path = 'tests/fixtures/file1.json'
        with pytest.raises(NameError):
            generate_diff(wrong, path)