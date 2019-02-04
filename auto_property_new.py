"""This script automatically wraps get, set, del methods in property."""


class Meta(type):
    """Metaclass that augments subclass instantiation."""

    def __new__(mcls, clsname, bases, classdict):
        """Override the __new__ method."""
        cls = type.__new__(mcls, clsname, bases, classdict)
        x_methods = [getattr(cls, attr) for attr in vars(cls)
                     for substr in ['get_x', 'set_x', 'del_x']
                     if substr in attr]
        y_methods = [getattr(cls, attr) for attr in vars(cls)
                     for substr in ['get_y', 'set_y', 'del_y']
                     if substr in attr]
        cls.x = property(*tuple(method for method in x_methods))
        cls.y = property(*tuple(method for method in y_methods))
        return cls


class Example(metaclass=Meta):
    """Class with methods to be automatically wrapped in property."""

    def __init__(self):
        """Initialize the object."""
        self._x = None

    def get_x(self):
        """Define getter."""
        return self._x

    def set_x(self, value):
        """Define setter."""
        self._x = value

    def get_y(self):
        """Define getter."""
        return 'y'


a = Example()
a.x = 255
print(a.x)
print(a.y)
