class Singleton:
    """
    E.g. a global configuration object
    that everyhing is supposed to share.
    - no matter how many times you try to create on,
      you are always supposed to get back the same instance;
      that prevents everyone from getting out of sync with one another.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def singleton_example():
    print('SINGLETON EXAMPLE')
    x = Singleton()
    y = Singleton()
    print(x is y)
    print(f'{x is y=}')


if __name__ == '__main__':
    singleton_example()
