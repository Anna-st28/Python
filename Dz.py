from abc import ABC


class Human(ABC):
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def info(self):
        return f"Фамилия: {self.surname}, Имя: {self.name}, Возраст: {self.age}"


class Student(Human):
    def __init__(self, surname, name, age, department, group, grade):
        super().__init__(surname, name, age)
        self.department = department
        self.group = group
        self.grade = grade

    def info(self):
        return f"{super().info()}, Факультет: {self.department}, Группа: {self.group}, Курс: {self.grade}"


class Teacher(Human):
    def __init__(self, surname, name, age, department, experience):
        super().__init__(surname, name, age)
        self.department = department
        self.experience = experience

    def info(self):
        return f"{super().info()}, Кафедра: {self.department}, Стаж: {self.experience}"


class Graduate(Student):
    def __init__(self, surname, name, age, department, group, grade, thesis):
        super().__init__(surname, name, age, department, group, grade)
        self.thesis = thesis

    def info(self):
        return f"{super().info()}, Тема диплома: {self.thesis}"


people = [
    Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
    Student("Загидулин", "Линар", 32, "РПО", "PD_011", 5),
    Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
    Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
    Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
    Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
]

for person in people:
    print(person.info())
