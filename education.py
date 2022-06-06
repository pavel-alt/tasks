from abc import ABC
from datetime import datetime
from time import sleep


class Human(ABC):
    pass


class Teacher(Human):
    def __init__(self):
        self.work = 0       # Определяем работу учителя изначально как нуль

    def teach(self, lesson, group):
        for student in group:
            student.studies(lesson)
        # Определяем работу учителя как длину списка суммарных знаний студентов
        self.work = sum([len(student.knowledge) for student in students_group])


class Student(Human):
    def __init__(self):
        self.knowledge = []

    def studies(self, new_knowledge):
        self.knowledge.append(new_knowledge)
        sleep(0.01)
        self.forger()

    def forger(self):
        if len(self.knowledge) > 10:
            self.knowledge.pop(0)
        if datetime.now().second % 2:
            self.knowledge.pop(0)


class KnowledgeData:
    lessons = ["les_1", "les_2", "les_3", "les_4", "les_5", "les_6", "les_7", "les_8", "les_9", "les_10"]


if __name__ == "__main__":
    vanya = Student()
    vasya = Student()
    petya = Student()
    tanya = Student()
    students_group = [vanya, vasya, petya, tanya]

    ivan = Teacher()
    # ivan.teach(KnowledgeData.lessons[0], students_group)
    for les in KnowledgeData.lessons:
        ivan.teach(les, students_group)

    print(vanya.knowledge)
    print(ivan.work)

    print([student.knowledge for student in students_group])
    print(1)
    for x in [student.knowledge for student in students_group]:
        print(x)

    # vanya.forger()
    print(vanya.knowledge)
    print(datetime.now().second)
