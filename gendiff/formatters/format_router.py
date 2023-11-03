def formatter(diffs, format):
    result = ['{']
    for item in diffs:
        key, action_type = item.get('key'), item.get('action_type')
        value, new_value = item.get('value'), item.get('new_value')
        added = f'  + {key}: {str(value).lower()}'
        removed = f'  - {key}: {str(value).lower()}'
        not_changed = f'    {key}: {str(value).lower()}'
        changed = f'  + {key}: {str(new_value).lower()}'
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
            case _:
                raise NameError(f"action's type {action_type} not supported")
    result.append('}')
    return '\n'.join(result)
