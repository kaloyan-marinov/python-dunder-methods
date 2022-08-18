class A:
    def __new__(cls, *args, **kwargs):
        """It is supposed to return something - an object."""
        print('new', cls, args, kwargs)
        return super().__new__(cls)
    
    def __init__(self, *args, **kwargs):
        """It doesn't return anything - it just initializes values."""
        print('init', self, args, kwargs)


def how_object_construction_works():
    a = A(1, 2, 3, x=4)

    # This is what happens, approximately:
    '''
    x = A.__new__(A, *args, **kwargs)
    
    if isinstance(x, A):
        type(x).__init__(x, *args, **kwargs)
    '''


if __name__ == '__main__':
    how_object_construction_works()
