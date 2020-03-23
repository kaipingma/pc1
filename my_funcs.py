"""
This module provides a collection of echo functions.
>>> func1()
'func1'
>>> func2()
'func2'
>>> func3()
'func3'
"""


def func1():
    """
    >>> func1()
    'func1'
    """
    # print('in func1...')
    return 'func1'


def func2():
    """
    >>> func2()
    'func2'
    """
    # print('in func2...')
    return 'func2'


def func3():
    """
    >>> func3()
    'func3'
    """
    # print('in func3...')
    return 'func3'


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    print('In main, calling', func1())
    print('In main, calling', func2())
    print('In main, calling', func3())

# print(func1(), func2(), func3())
