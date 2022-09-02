import datetime

def logger(filename):

    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(filename, 'a+', encoding='UTF-8') as f:
                f.write(f'{datetime.datetime.now()} вызвана функция {old_function.__name__} с аргументами {args} и {kwargs}, результат {result}\n')
            # print(f'{datetime.datetime.now()} вызвана функция {old_function.__name__} с аргументами {args} и {kwargs}, результат {result}')
            return result

        return new_function
    return _logger

