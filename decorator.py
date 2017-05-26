
def log(func):
    '''

    :param func:
    :return:
    '''
    def wrapper(*args, **kvargs):
        print 'before calling', func.__name__
        print 'args', args, 'kvargs',kvargs
        func(*args, **kvargs)
        print 'end calling', func.__name__
    return wrapper


@log
def hello(name, age):
    print 'hello'

if __name__ == '__main__':
    hello("zjs", 2)