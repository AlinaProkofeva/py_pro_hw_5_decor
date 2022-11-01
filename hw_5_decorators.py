import datetime

'''пишем простой логгер'''
def logger(somefunc):
    def new_func(*args, **kwargs):
        datetime_mark = datetime.datetime.now() # отметка времени запуска функции
        result = somefunc(*args, **kwargs)
        log = f'{datetime_mark} | {somefunc.__name__} | args: {args, kwargs} | result: {result}\n' # строка лога
        with open('log.txt', 'at', encoding='utf-8') as file:
            file.write(log) # запись в файл
        return result
    return new_func

@logger
def summator(a,b):
    return a + b

'''проверяем'''
summator(1,2)
summator(7,8)
summator(4,2)

'''пишем логгер c путем'''

def path_logger(path):
    def logger(somefunc):
        def new_func(*args, **kwargs):
            datetime_mark = datetime.datetime.now() # отметка времени запуска функции
            result = somefunc(*args, **kwargs)
            log = f'{datetime_mark} | {somefunc.__name__} | args: {args, kwargs} | result: {result}\n' # строка лога
            with open(path, 'at', encoding='utf-8') as file:
                file.write(log) # запись в файл
            return result
        return new_func
    return logger

'''проверяем'''

@path_logger('C:\\Users\\Алина\\Desktop\\log.txt')
def summator(a,b):
    return a + b

summator(1,2)
summator(7,8)
summator(6,6)