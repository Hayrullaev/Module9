def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        result[i.__name__] = i(int_list)
    return result


print(apply_all_func([8, 90, 43, 24, 57, 1], max, min))
print(apply_all_func([6, 20, 15, 9, 89, 7], len, sum, sorted))
