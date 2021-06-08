def func_executor(*funcs_with_args):
    res = []

    for func, fargs in funcs_with_args:
        func_res = func(*fargs)
        res.append(func_res)

    return res