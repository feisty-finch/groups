class ShapesValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise ShapesValueError("dimensions cannot be negative")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __repr__(self):
        return f"{self.__class__.__name__}{self.length, self.width!r}"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        # Calls the __init__ function of the parent class

    def __repr__(self):
        return f"{type(self).__name__}({self.length!r})"
