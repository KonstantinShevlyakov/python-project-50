#!usr/bin/env python3

def build_representation(old_data, new_data):
    result = {}
    unique_keys = old_data.keys() | new_data.keys()
    sorted_keys = sorted(unique_keys, key=lambda x: x)
    for k in sorted_keys:
        if k in old_data.keys() and k not in new_data.keys():
            result[k] = ('removed', old_data[k])
        if k not in old_data.keys() and k in new_data.keys():
            result[k] = ('added', new_data[k])
        if k in old_data.keys() and k in new_data.keys():
            if old_data[k] != new_data[k]:
                if isinstance(old_data[k], dict) \
                        and isinstance(new_data[k], dict):
                    result[k] = (
                        'nested',
                        build_representation(old_data[k], new_data[k])
                    )
                else:
                    result[k] = ('changed',
                                 old_data[k],
                                 new_data[k])
            else:
                result[k] = ('unchanged', old_data[k])
    return result
