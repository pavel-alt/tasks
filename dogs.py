class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def get_biggest_number(*args) -> int:
    return max(*args)


if __name__ == "__main__":
    dog_1 = Dog("Sharik", 5)
    dog_2 = Dog("Bobik", 8)
    dog_3 = Dog("Volchek", 9)
    dog_4 = Dog("Timka", 1)

    dog_list = [dog_1, dog_2, dog_3, dog_4]

    dog_age_list = [el.age for el in dog_list]

    d_a = get_biggest_number(dog_1.age, dog_2.age, dog_3.age, dog_4.age)

    for i in dog_list:
        if i.age == d_a:
            print(f"Самая старая собака - {i.name}")

