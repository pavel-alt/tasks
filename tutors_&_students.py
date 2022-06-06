# 1.
# Есть класс преподавателей и класс студентов. Студентов пока оставим без изменения, а вот преподаватели бывают разные,
# поэтому теперь класс Mentor должен стать родительским классом, а от него нужно реализовать наследование классов
# Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия и список закрепленных
# курсов логично реализовать на уровне родительского класса.
# 2.
# Возможность выставлять студентам оценки за домашние задания могут делать только Reviewer (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов :) Реализуйте метод выставления оценок лекторам у
# класса Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия
# курсов, а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
# 3.
# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:
#
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy
#
# У лекторов:
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
#
# А у студентов так:
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование
#
# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и
# студентов по средней оценке за домашние задания.
#
# 4.
#
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
# -для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов
# принимаем список студентов и название курса);
# -для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов
# и название курса).

from abc import ABC
from random import randint


class Students:
    def __init__(self, name, surname, student_courses_list):
        self.name = name
        self.surname = surname
        self.student_courses_list = student_courses_list
        self.marks_list = []
        self.learning_courses = []
        self.learned_courses = []

    def __set_mark(self, student_course, lector):
        if student_course in self.student_courses_list and student_course in lector.mentor_courses_list:
            lector.lecture_marks.get(student_course).append(randint(1, 10))

    def study_the_course(self, course, lector, reviewer):
        if course not in self.student_courses_list:
            return "Курса нет в расписании"
        self.learning_courses.append(course)
        reviewer.marks(HomeWork(self, course))
        self.__set_mark(course, lector)
        self.learned_courses.append(course)
        self.learning_courses.remove(course)

    def __average_lectors_rate(self):
        rate_sum = sum(self.marks_list)
        return rate_sum / len(self.marks_list) if rate_sum > 0 else 'Нет оценок за домашнее задание'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.__average_lectors_rate()}\n' \
               f'Курсы в процессе изучения: ' \
               f'{" ".join(self.learning_courses) if self.learning_courses else "Нет курсов в процессе"}\n' \
               f'Завершенные курсы: ' \
               f'{" ".join(self.learned_courses) if self.learned_courses else "Нет завершенных курсов"}'


class HomeWork:
    def __init__(self, executor, course):
        self.executor = executor
        self.course = course

    def set_mark(self, mark):
        setattr(self, 'mark', mark)


class Mentor(ABC):
    def __init__(self, name, surname, mentor_courses_list):
        self.name = name
        self.surname = surname
        self.mentor_courses_list = mentor_courses_list


class Lecturer(Mentor):
    def __init__(self, name, surname, mentor_courses_list):
        super().__init__(name, surname, mentor_courses_list)
        self.lecture_marks = {key: [] for key in self.mentor_courses_list}

    def __calc_average_rate(self):
        rate_sum = sum([sum(el) / len(el) for el in self.lecture_marks.values() if len(el) > 0])
        return rate_sum / len(self.lecture_marks.values()) if rate_sum > 0 else 'Нет оценок за лекции'

    def __str__(self):
        # # return self.lecture_marks.values()
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции:' \
               f'{self.__calc_average_rate()}'


class Reviewer(Mentor):
    @staticmethod
    def marks(home_work):
        mark = randint(1, 10)
        home_work.set_mark(mark)
        home_work.executor.marks_list.append(mark)

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f' Фамилия: {self.surname}'


if __name__ == "__main__":
    student_1 = Students('Ivan', 'Ivanov', ['math', 'chemistry'])
    # student_1.marks_list = []
    # student_1.learning_courses = []
    # student_1.learned_courses = []

    student_2 = Students('Petr', 'Petrov', ['math', 'history'])
    # student_2.marks_list = []
    # student_2.learning_courses = []
    # student_2.learned_courses = []

    lecturer_1 = Lecturer('Sergey', 'Sergeev', ['math', 'phisic'])
    lecturer_2 = Lecturer('Denis', 'Denisov', ['history', 'phisic'])
    reviewer_1 = Reviewer('Vladimir', 'Vladimirov', ['math', 'phisic'])
    reviewer_2 = Reviewer('Igor', 'Igorev', ['history', 'phisic'])
    # home_work_1 = HomeWork(student_1, 'math')
    # home_work_2 = HomeWork(student_2, 'history')

    student_1.study_the_course('math', lecturer_1, reviewer_1)
    student_2.study_the_course('history', lecturer_2, reviewer_2)

    # student_1.set_mark('math', lecturer_1)
    # student_2.set_mark('history', lecturer_2)

    print(student_1)
    print(student_2)
    print()
    print(lecturer_1)
    print(lecturer_2)
    print()
    print(reviewer_1)
    print(reviewer_2)


def my_func(a, b):
    return sum(a, b) if sum(a, b) > 10 else a - b
