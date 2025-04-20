class Student:

    def __init__(self, name, laptop_model, laptop_processor, laptop_memory):
        self.name = name
        self.laptop = self.Laptop(laptop_model, laptop_processor, laptop_memory)

    def print_student_info(self):
        print(f"Студент: {self.name}")
        self.laptop.print_laptop_info()

    class Laptop:

        def __init__(self, model, processor, memory):
            self.model = model
            self.processor = processor
            self.memory = memory

        def print_laptop_info(self):
            print(f"  Ноутбук: {self.model}, процессор: {self.processor}, память: {self.memory} ГБ")


Roman = Student("Roman", "HP", "i7", 16)
vladimir = Student("Vladimir", "HP", "i7", 16)

Roman.print_student_info()
vladimir.print_student_info()
