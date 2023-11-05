from gendiff.formatters import stylish, plain, to_json


def formatter(diffs, format):
    print(diffs)
    match format:
        case 'stylish':
            return stylish.format_stylish(diffs)
        case 'plain':
            return plain.format_plain(diffs)
        case 'json':
            return to_json.format_json(diffs)
        case _:
            raise NameError(f'format {format} not supported')
