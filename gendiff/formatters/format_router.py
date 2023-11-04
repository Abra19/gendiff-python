from gendiff.formatters.stylish import stylish


def formatter(diffs, format):
    match format:
        case 'stylish':
            return stylish(diffs)
