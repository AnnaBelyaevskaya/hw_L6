class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 1 <= grade <= 10:
                if course in lecturer.rating_dict:
                    lecturer.rating_dict[course] += [grade]
                else:
                    lecturer.rating_dict[course] = [grade]
                return lecturer.rating_dict
            return "Оцените по шкале от 1 до 10"
        return "Ошибка"

    def av_rating(self):
        rating = 0
        counter = 0
        for courses in self.grades.values():
            for rate in courses:
                rating += rate
                counter += 1
        av_rating = rating / counter
        return av_rating

    def __str__(self):
        return f'Имя: {self.name} \nФамилия:{self.surname} \nСредняя оценка за ДЗ: {self.av_rating()} \nКурсы в процессе изучения: {", ".join(map(str,self.courses_in_progress))} \nЗавершенные курсы: {", ".join(map(str,self.finished_courses))}\n'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.av_rating()< other.av_rating()
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]

            else:
                student.grades[course] = [grade]
            return student.grades
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия:{self.surname }\n'



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating_dict = {}

    def av_rating(self):
        rating = 0
        counter = 0
        for courses in self.rating_dict.values():
            for rate in courses:
                rating += rate
                counter += 1
        av_rating = rating / counter
        return av_rating

    def __str__(self):
        return f'Имя: {self.name} \nФамилия:{self.surname } \nСредняя оценка за лекции: {self.av_rating()}\n'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.av_rating() < other.av_rating()
        else:
            return "Ошибка"

def av_hw_all_students(student_list, course):
    students_hw = []
    total = 0
    counter = 0
    for student in student_list:
        for first, second in student:
            if first in student.name and second in student.surname:
                for courses, grades in student.grades:
                    if course in courses:
                        for grade in grades:
                            total += grade
                            counter += 1
                        students_hw.append(total / counter)
    return sum(i for i in students_hw)/len(students_hw)


list_1 = ["Петр Петров", "Иван Иванов"]


peter_student = Student('Петр', 'Петров', 'муж')
peter_student.courses_in_progress += ['Python']
peter_student.finished_courses += ['GIT']
ivan_student = Student('Иван', 'Иванов', 'муж')
ivan_student.courses_in_progress += ['Python']
ivan_student.finished_courses += ['GIT']
oleg_lec = Lecturer('Олег', 'Михайлов')
oleg_lec.courses_attached += ['Python']
bogdan_lec = Lecturer('Богдан', 'Богданов')
bogdan_lec.courses_attached += ['Python']
anna_rev = Reviewer('Анна', 'Васильева')
anna_rev.courses_attached += ['Python']
inna_rev = Reviewer('Инна', 'Сорокина')
inna_rev.courses_attached += ['Python']

print(peter_student.rate_lec(bogdan_lec, "Python", 10))
print(ivan_student.rate_lec(oleg_lec, "Python", 9))


print(anna_rev.rate_hw(peter_student, "Python", 10))
print(anna_rev.rate_hw(ivan_student, "Python", 9))

print(anna_rev.rate_hw(peter_student, "Python", 5))
print(anna_rev.rate_hw(ivan_student, "Python", 5))


print(peter_student < ivan_student)
print(oleg_lec < bogdan_lec)

print(peter_student)
print(ivan_student)

# print(peter_student.grades)

print(av_hw_all_students(list_1, "Python"))
