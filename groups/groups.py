from numbers import Integral
import numpy as np


class GroupsValueError(ValueError):
    pass


class Element:
    def __init__(self, group, value):
        group._validate(value)
        self.group = group
        self.value = value

    def __mul__(self, other):
        return Element(
            self.group,
            self.group.operation(self.value, other.value)
        )

    def __str__(self):
        return f"{self.value}_{self.group}"

    def __repr__(self):
        return f"{type(self).__name__}({self.group}, {self.value})"
    # rather than "return f'Element({self.group}, {self.value}')"


class Group:
    def __init__(self, n):
        self.n = n

    def __call__(self, value):
        return Element(self, value)

    def __repr__(self):
        return f"{self.symbol}{self.n})"


class CyclicGroup(Group):
    symbol = "C"  # class attribute

    def _validate(self, value):
        if not (isinstance(value, Integral) and
                0 <= value < self.n):
            raise GroupsValueError("Element value must be an integer "
                                   f"in the range [0, {self.n}).")

    def operation(self, a, b):
        """Perform the group operation on two values."""
        return (a + b) % self.n

    def __str__(self):
        return f"C{self.n}"


class GeneralLinearGroup(Group):
    symbol = "G"
    # Just like the method name is accessed to self._validate(value),
    # class attribute name is accessed to self.symbol

    def _validate(self, value):
        if not (isinstance(value, np.ndarray) and
                value.shape == (self.n, self.n)):
            raise GroupsValueError("Element value must be an array "
                                   f"with shape ({self.n}, {self.n}).]")

    def operation(self, a, b):
        """Perform the group operation on two values."""
        return a @ b

    def __str__(self):
        return f"G{self.n}"
