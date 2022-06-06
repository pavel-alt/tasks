from abc import ABC, abstractmethod


class Cooker:
    def __init__(self):
        pass

    def get_the_dish(self, *args):
        print('I think...')
        if any([isinstance(food, Meet) for food in args]):
            self.roast(args)
        elif not all([isinstance(food, Goods) for food in args]):
            print('I have no goods')
        else:
            self.boil(args)

    @staticmethod
    def roast(goods):
        print(f'{", ".join([el.name for el in goods])} are roasted')

    @staticmethod
    def boil(goods):
        print(f'{", ".join([el.name for el in goods])} are boiled')

    @staticmethod
    def bake():
        print('it is baked')


class Goods(ABC):
    def __init__(self, name):
        self.name = name


class Meet(Goods):
    pass


class Vegetables(Goods):
    pass


class Fish(Goods):
    pass


if __name__ == '__main__':
    carrot = Vegetables('carrot')
    pork = Meet('pork')
    cooker_1 = Cooker()
    cooker_1.get_the_dish('carrot')
    print(isinstance(carrot, Goods))
