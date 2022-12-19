
def stringify(value, formatter='stylish'):
    if isinstance(value, dict) or type(value) is int:
        return value
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif value == '':
        if formatter == 'stylish':
            return ''
        return "''"
    else:
        if formatter == 'stylish':
            return str(value)
        return f"'{str(value)}'"
