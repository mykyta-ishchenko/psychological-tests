def connect_to_upper_group(upper_group, func, params):
    result = {}
    for group_key, group_value in upper_group.items():
        sub = {el: params[el] for el in group_value}
        result[group_key] = (func([v[0] for k, v in sub.items()]), sub)
    return result
