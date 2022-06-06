# Создать клетки (органические), которые бы себя соответствено вели - сливались.
# У клетки должна быть характеристика - обем.

class Cell:
    def __init__(self, volume):
        self.volume = volume

    def __add__(self, other: 'Cell'):
        new_cell = Cell(self.volume + other.volume)
        del self.volume, other.volume
        return new_cell

    def __truediv__(self):
        new_cell_volume = self.volume / 2
        del self.volume
        return Cell(new_cell_volume), Cell(new_cell_volume)



a = Cell(20)
b = Cell(10)

# print(a.volume)
# print(b.volume)
c = a + b
# print(c.volume)
# print(a.volume)
# print(b.volume)

# x, y = c.__truediv__()
# print(c)
# print(x.volume, y.volume)
# Сделать деление клеток


z = c.__truediv__()
print(z)

s, f, g = [4, 3]
