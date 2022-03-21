class Rectangle:
    length = 0
    width = 0

    def __init__(self):
        pass

    def area_of(self, length, width):
        area = length * width
        return area

    def perimeter_of(self, length, width):
        perimeter = 2 * (length + width)
        return perimeter


class Square(Rectangle):
    def __init__(self):
        pass


square1 = Square()
square_area = square1.area_of(2, 3)
print(f'The area of square1 is: {square_area}')

