class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __repr__(self):
        return f"{self.__class__.__name__}{self.length, self.width!r}"
