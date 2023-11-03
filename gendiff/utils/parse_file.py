import json


def parse_file(path):
    with open(path) as file:
        content = file.read()
    last_dot_index = path.rfind('.')
    file_extension = path[last_dot_index + 1:]
    match file_extension:
        case 'json':
            return json.loads(content)
        case _:
            raise NameError(f'file extension {file_extension} not supported')
