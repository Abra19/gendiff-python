from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def formatter(diffs, format):
    match format:
        case 'stylish':
            return format_stylish(diffs)
        case 'plain':
            return format_plain(diffs)
        case _:
            raise NameError(f'format {format} not supported')
