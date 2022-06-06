from abc import ABC, abstractmethod


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Engine2D:
    def __init__(self):
        self.canvas = []

    def add(self, figure):
        self.canvas.append(figure)

    def draw(self):
        for figure in self.canvas:
            figure.draw()
        self.canvas.clear()


"""Созднание родительского класса для обязаельного определения метода draw
для дочерних классов"""


class Figure(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass


class Circle(Figure):
    def __init__(self, centre: Point, rad: int) -> None:
        self.centre = centre
        self.rad = rad

    def draw(self) -> None:
        print(f'Drawing Circle: ({self.centre.x}, {self.centre.y}) with radius {self.rad}')


class Triangle(Figure):
    def __init__(self, coord_1: Point, coord_2: Point, coord_3: Point) -> None:
        self.coord_1 = coord_1
        self.coord_2 = coord_2
        self.coord_3 = coord_3

    def draw(self) -> None:
        print(f'Drawing a Triangle with corners at points ({self.coord_1.x}, {self.coord_1.y}), ({self.coord_2.x}, '
              f'{self.coord_2.y}), ({self.coord_3.x}, {self.coord_3.y})')


class Rectangle(Figure):
    def __init__(self, coord_1: Point, side_1: int, side_2: int) -> None:
        self.coord_1 = coord_1
        self.side_1 = side_1
        self.side_2 = side_2

    def draw(self) -> None:
        print(f'Drawing a Rectangle with corners at point ({self.coord_1.x}, {self.coord_1.y}) and sides '
              f'{self.side_1}, {self.side_2}')


if __name__ == "__main__":
    circle = Circle(Point(0, 1), 5)
    triangle = Triangle(Point(0, 0), Point(0, 1), Point(2, 5))
    rectangle = Rectangle(Point(0, 1), 5, 10)
    engine_2D = Engine2D()
    engine_2D.add(circle)
    engine_2D.add(triangle)
    engine_2D.add(rectangle)
    engine_2D.draw()


