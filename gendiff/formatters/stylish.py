REPLACER = ' '


def stringify(value, depth, spaces_count=4):
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        return str(value).lower() if isinstance(value, bool) else str(value)
    lines = ['{']
    for key in value.keys():
        current = value[key]
        format_key = f'{REPLACER * (depth + spaces_count * 2)}{key}: '
        if isinstance(current, dict):
            lines.append(format_key
                         + stringify(current, depth + spaces_count))
        else:
            result_str = str(current).lower() if isinstance(current, bool) \
                else "null" if current is None else str(current)
            lines.append(format_key + result_str)
    lines.append(f'{REPLACER * (depth + spaces_count) + "}"}')
    return '\n'.join(lines)


def stylish(diffs):
    def iter(tree, depth):
        result = ['{']
        for node in tree:
            key, action_type = node.get('key'), node.get('action_type')
            value, new_value = node.get('value'), node.get('new_value')
            value_str = stringify(value, depth)
            new_value_str = stringify(new_value, depth)
            spaces = REPLACER * (depth + 2)
            added = f'{spaces}+ {key}: {value_str}'
            removed = f'{spaces}- {key}: {value_str}'
            not_changed = f'{spaces}  {key}: {value_str}'
            changed = f'{spaces}+ {key}: {new_value_str}'
            match action_type:
                case 'added':
                    result.append(added)
                case 'removed':
                    result.append(removed)
                case 'not_changed':
                    result.append(not_changed)
                case 'changed':
                    result.append(removed)
                    result.append(changed)
                case 'children':
                    result.append(f'{REPLACER * (depth + 4)}{key}: '
                                  + f'{iter(value, depth + 4)}')
        result.append(f'{REPLACER * depth + "}"}')
        return '\n'.join(result)
    return iter(diffs, 0)
