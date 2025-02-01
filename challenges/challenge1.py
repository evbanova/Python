def type_check(*args_types):
    def put_type_decorator(put_type):
        def func_decorator(func):
            def arguments_decorator(*args, **kwargs):
                args_list = list(map(lambda x: ('', x), args)) + list(kwargs.items())
                if put_type is 'in':
                    for key, value in args_list:
                        if type(value) not in args_types:
                            print('Invalid input value, expected {}!'.format(', '.join(str(arg) for arg in args_types)))
                            break
                func_result = func(args, kwargs)
                if put_type is 'out':
                    if type(func_result) not in args_types:
                        print('Invalid output value, expected {}!'.format(', '.join(str(arg) for arg in args_types)))
                return func_result
            return arguments_decorator
        return func_decorator
    return put_type_decorator
