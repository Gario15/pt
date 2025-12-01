class Student:
    def __init__(self, last_name):
        self.__last_name = last_name
        self.__grades = []

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            raise TypeError(f"Оценка должна быть числом, получено: {type(grade).__name__}")

        if grade < 1 or grade > 5:
            raise ValueError(f"Оценка должна быть в диапазоне от 1 до 5, получено: {grade}")

        self.__grades.append(grade)

    def average_grade(self):
        if not self.__grades:
            return 0.0

        return sum(self.__grades) / len(self.__grades)

    def get_last_name(self):
        return self.__last_name

    def get_grades(self):
        return self.__grades.copy()

    def __str__(self):
        grades_str = ', '.join(str(grade) for grade in self.__grades) if self.__grades else "нет оценок"
        avg = self.average_grade()
        return f"Студент {self.__last_name}: оценки [{grades_str}], средний балл: {avg:.2f}"

    def __repr__(self):
        return f"Student('{self.__last_name}', grades={self.__grades})"
