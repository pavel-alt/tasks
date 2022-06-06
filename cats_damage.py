# Есть котик. У котика есть мама и папа. Мама передала котику свою красоту: шёрстку, глазки и плодовитость (инт).
# А папа характер: домаг, выносливость, живучесть (инт).
#
# У котика появится новая характеристика "генетика" которая равна плодовитости
# умноженной на живучесть. Эта характеристика должна вызываться через котик.генетика, не как функция .
# * Нужен super().init
# ** Читай про @property

class CatFather:
    def __init__(self, damage, stamina, vitality):
        self.damage = damage
        self.stamina = stamina
        self.vitality = vitality


class CatMother:
    def __init__(self, hair, eyes, fertility):
        self.hair = hair
        self.eyes = eyes
        self.fertility = fertility


class LittleCat(CatMother, CatFather):
    def __init__(self):
        super(LittleCat, self).__init__(vitality=int)