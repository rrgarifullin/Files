from datetime import datetime


def log(path):
    def write_log(old_function):
        def new_function(*args, **kwargs):
            start_time = datetime.now(tz=None)
            function_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'\nВремя вызова функции: {start_time}\n'
                         f'Имя функции: {function_name}\n'
                         f'Аргументы функции: {args}; {kwargs}\n'
                         f'Возвращаемое значение: {result}')

            return result
        return new_function
    return write_log

