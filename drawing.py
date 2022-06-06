from abc import ABC, abstractmethod


class Engine2D:
    def __init__(self):
        self.canvas = []
        self.color = 'color'

    def add(self, shape):
        self.canvas.append(s    hape)

    def draw(self):
        for shape in self.canvas:
            shape.draw(self.color)
        self.canvas.clear()

    def set_color(self, color):
        self.color = color


class Shape(ABC):
    @abstractmethod
    def draw(self, color) -> None:
        pass


class Triangle(Shape):
    def __init__(self, coord_1: tuple, coord_2: tuple, coord_3: tuple):
        self.coord_1 = coord_1
        self.coord_2 = coord_2
        self.coord_3 = coord_3

    def draw(self, color):
        print(f'Drawing {color} {self.__class__.__name__} with '
              f'vertices at points {self.coord_1}, {self.coord_2}, {self.coord_3}')


class Rectangle(Shape):
    def __init__(self, corner_coord: tuple, side_1: int, side_2: int):
        self.corner_coord = corner_coord
        self.side_1 = side_1
        self.side_2 = side_2

    def draw(self, color):
        print(f'Drawing {color} {self.__class__.__name__} with sides {self.side_1} and {self.side_2} '
              f'intersecting at a point {self.corner_coord}')


class Circle(Shape):
    def __init__(self, centre_coord: tuple, radius: int):
        self.centre_coord = centre_coord
        self.radius = radius

    def draw(self, color):
            print(f'Drawing {color} {self.__class__.__name__}: {self.centre_coord} with radius {self.radius}')


if __name__ == "__main__":
    circle = Circle((2, 3), 5)
    triangle = Triangle((0, 0), (4, 1), (2, 2))
    rectangle = Rectangle((0, 1), 5, 10)
    engine_2D = Engine2D()
    engine_2D.set_color('red')
    engine_2D.add(circle)
    engine_2D.add(triangle)
    engine_2D.add(rectangle)
    engine_2D.draw()
