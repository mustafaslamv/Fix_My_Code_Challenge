#!/usr/bin/python3
""" square class """


class square():
    """square class """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.height = self.width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
