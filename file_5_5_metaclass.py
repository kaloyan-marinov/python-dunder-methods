"""
metaclasses are especially useful to do black magic, and therefore complicated stuff.

But by themselves, they are simple:
    - intercept a class creation
    - modify the class
    - return the modified class

"""

"""
remember that `type` is actually a class like `str` and `int`
so you can inherit from it

(
    classes are themselves instances. Of metaclasses.

    Except for `type`.

    `type` is actually its own metaclass.
)
"""

"""
metaclasses are complicated.
You may not want to use them for very simple class alterations.
You can change classes by using two different techniques:
    - monkey patching
    - class decorators

99% of the time you need class alteration, you are better off using these.

But 98% of the time, you don't need class alteration at all.
"""

class UpperAttrMetaclass(type):
    """
    `__new__` is the method called before `__init__`;
    it's the method that creates the object and returns it;
    it always receives the class it's defined in, as the first parameter
    - just like you have `self` for ordinary methods
      which receive the instance as the first parameter,
      or the defining class for class methods.

    while `__init__` just initializes the object passed as parameter

    you rarely use `__new__`, except when you want to control how the object
    is created.

    here the created object is the class, and we want to customize it
    so we override `__new__`

    (
    you can do some stuff in `__init__` too if you wish;
    some advanced use involves overriding __call__ as well, but we won't
    see this
    )
    """
    def __new__(cls, clsname, bases, attrs):
        print(cls)
        print(clsname)
        print(bases)
        print(attrs)

        uppercased_attrs = {
            key if key.startswith("__") else key.upper(): value
            for key, value in attrs.items()
        }
        # return type(clsname, bases, uppercased_attrs)
        # return type.__new__(cls, clsname, bases, uppercased_attrs)
        # return super(UpperAttrMetaclass, cls).__new__(
        #     cls, clsname, bases, uppercased_attrs
        # )
        return super().__new__(cls, clsname, bases, uppercased_attrs)


class Message(metaclass=UpperAttrMetaclass):
    id = 1
    text = 'hello'


if __name__ == '__main__':
    print()
    print(f"{hasattr(Message, 'id') = }")
    print(f"{hasattr(Message, 'text') = }")

    print()
    print(f"{hasattr(Message, 'ID') = }")
    print(f"{hasattr(Message, 'TEXT') = }")