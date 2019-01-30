class Meta(type):
    def __call__(cls, *args, **kwargs):
        new = cls.__new__(cls, *args, **kwargs)
        if isinstance(new, cls):
            new.__init__(*args, **kwargs)
        x_methods = [getattr(cls,i) for i in cls.__dict__ if 'x' in i]
        cls.x = property(*tuple(method for method in x_methods))
        return new

class Example(metaclass=Meta):
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self,value):
        self._x = value
    def get_y(self):
        return 'y'
