import ast


def data_conversion(val, type):
    if type == 'String':
        return str(val)
    if type == 'Number':
        return int(val)
    if type == 'Dictionary':
        return ast.literal_eval(val)
    if type == 'List':
        # "1,2,3,4,5"
        return val.split(",")
    if type == 'Tuple':
        # tuple(eval("(1,2,3)"))
        return tuple(eval(val))
    if type == 'Set':
        # hello  => {'h','e','l','o'}
        return set(val)
    if type == 'Float':
        return float(val)

    return val

