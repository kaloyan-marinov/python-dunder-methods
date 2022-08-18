class UppercaseTuple(tuple):
    def __new__(cls, iterable):
        uppercased_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, uppercased_iterable)


def inheriting_builtin_immutable_type():
    print('UPPERCASE TUPLE EXAMPLE')
    t = UppercaseTuple(('hi', 'there'))
    print(t)


if __name__ == '__main__':
    inheriting_builtin_immutable_type()


"""
Q:
Why inherit from `tuple` and have to know about `__new__`
instead of
creating a ["proxy"] class that simply contains a tuple?

A:
For this case, the reason is performance:
the `tuple` builtin is primarily written in C,
which makes it much faster than any Python code that you could write.
"""