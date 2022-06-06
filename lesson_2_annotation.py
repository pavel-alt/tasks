from typing import Optional, Union, Any, List, FrozenSet, Set, Tuple, Dict


# a: Optional[int] - означает, что а должен быть интом, но може быть ни чем (дефолтно None)
# a: int=None - означает, что а должен быть интом или ничем (дефолтно None)
# b: Union[int, float] - означает, что b может быть или интом или флоатом
# c: Optional[Union[int, float]] - означает, что с может быть или интом, или флоатом, или ничем (дефолтно None)
# d: Any - означает, что d может быть чем угодно
# e: List[int] - означает, что е обязательно список, внутри которого будут только инты. внутри [] может быть что угодно,
#    в том числе можно писать e: List[Optional[Union[int, float]]]
# f: Set[int] - означает, что f обязательно set, внутри которого будут только инты. внутри [] может быть что угодно,
#    в том числе можно писать f: List[Optional[Union[int, float]]]
# g: FrozenSet[int] - означает, что g обязательно set, внутри которого будут только инты. внутри [] может быть что
#    угодно, в том числе можно писать g: FrozenSet[Optional[Union[int, float]]]
# h: Tuple[int, str, bool] - означает, что h всегда кортеж, включающий в себя только перечисленные типы данных и только
#    в указанном поядке
# i: Tuple[int, ...] - означает, что i тольк котртеж, включающий в себя только инты
# j: Dict[str, int] - озачает, что j обязательно словарь, где четко обозначены типы ключа/значения
# k: Optional[Union[int, Point]] - обзначает, что k может быть или интом, или экземпляром кастомного класса Point,
#    или None


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class MyClass:
    def __init__(self, a: Optional[int], b: Union[int, float], c: Optional[Union[int, float]], d: Any,
                 e: List[int], f: Set[int], g: FrozenSet[str], h: Tuple[int, str, bool], i: Tuple[int, ...],
                 j: Dict[str, int], k: Optional[Union[int, Point]]) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k


if __name__ == "__main__":
    my_set = {1, 2, 9}
    my_frozen_set = frozenset('gghg')
    ex = MyClass(5, 2.3, 1, 1, [1], my_set, my_frozen_set, (1, "a", True), (1, 5, 9), {"s1": 1}, Point(0, 1))

