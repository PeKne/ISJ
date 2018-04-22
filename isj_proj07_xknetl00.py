#!/usr/bin/env python3
import math

class TooManyCallsError(Exception):
    """
    Special exception for limit_calls decorator
    """
    pass

def limit_calls(max_calls=2, error_message_tail='called too often'):
    """
    Decorator which raises exception if count of function calls is greater than max_calls parameter
    """

    def func_call_counter(func):
        func.max = max_calls + 1
        def call(a,b):
            func.max -=1
            if func.max != 0:
                return func(a,b)
            else:
                exception_message =  'function \"' + func.__name__ + '\" - ' + error_message_tail
                raise TooManyCallsError(exception_message)
        return call
    return func_call_counter

    return call_counter


def ordered_merge(*args, selector=None):
    """
    Function which generate new list containing items from itterable items (args) in specific order (by selector)
    """
    args = list(args)
    output = []
    if selector == None:
        print ("ERROR: undefined 'selector' argument")
        exit(1)

    elif args is None:
        print ("ERROR: undefined itterable arguments")
        exit(1)

    else:
        for index in selector:
            try:
                iterator = iter(args[index])
            except TypeError:
                    print ("ERROR: args are not itterable")
                    exit(2)
            else:
                if len(args[index]) == 0:
                    print("ERROR: itterable argument is empty")
                    exit(3)
                output.append(args[index][0])
                args[index] = args[index][1:]

    return (output)

class Log():
    """ Zapis informace do souboru """
    def __init__(self, log_file):
        self.filename = log_file

    def __enter__(self):
        self.opened_file = open(self.filename, 'w+')
        self.opened_file.write("Begin\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.opened_file.write("End\n")
        self.opened_file.close()
        return True # handle error

    def logging(self, text):
        self.opened_file.write(text + "\n")
