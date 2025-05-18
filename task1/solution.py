def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__
        anno_keys = list(annotations.keys())

        for i, arg in enumerate(args):
            print(f"{i} {arg}")
            if i >= len(anno_keys):
                break 
            param_name = anno_keys[i]
            expected_type = annotations[param_name]
            if not isinstance(arg, expected_type):
                raise TypeError()
        return func(*args)
    return wrapper

    
@strict
def sum_two(a: int, b: int) -> int:
    return a + b

test_data = [[1,2],[1,2.4],[1,"a"],[1,True]]
for data in test_data:
    print(sum_two(data[0], data[1]))

