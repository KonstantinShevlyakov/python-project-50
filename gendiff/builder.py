
def build_representation(old_data, new_data):
    diff = {}
    unique_keys = old_data.keys() | new_data.keys()
    sorted_keys = sorted(unique_keys, key=lambda x: x)
    for key in sorted_keys:
        if key in old_data.keys() and key not in new_data.keys():
            diff[key] = ('removed', old_data[key])
        elif key not in old_data.keys() and key in new_data.keys():
            diff[key] = ('added', new_data[key])
        elif key in old_data.keys() and key in new_data.keys():
            if old_data[key] != new_data[key]:
                if isinstance(old_data[key], dict) \
                        and isinstance(new_data[key], dict):
                    diff[key] = (
                        'nested',
                        build_representation(old_data[key], new_data[key])
                    )
                else:
                    diff[key] = ('changed',
                                 old_data[key],
                                 new_data[key])
            else:
                diff[key] = ('unchanged', old_data[key])
    return diff
