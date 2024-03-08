import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

class Student:
    def __init__(self, name, surname, index):
        self.name = name
        self.surname = surname
        self.index = index
        self.subjects = []
    def add_subjects(self, subject, grade):
        self.subjects.append((subject, grade))
        return self

    def __str__(self):
        txt1 = "Student: {} {}".format(self.name, self.surname)
        for subject in self.subjects:
            txt1 += "\n----{}: {}".format(subject[0],subject[1])
        return txt1

if __name__ == "__main__":
    students = {}
    while(True):
        string = input()
        if string == "end":
            break
        string = string.split(",")
        if students.get(int(string[2])) == None:
            students[int(string[2])] = Student(string[0], string[1], int(string[2]))

        grade = int(string[4]) + int(string[5]) + int(string[6])
        if grade <= 50:
            grade = 5;
        elif grade <= 60:
            grade = 6
        elif grade <= 70:
            grade = 7
        elif grade <= 80:
            grade = 8
        elif grade <= 90:
            grade = 9
        elif grade <= 100:
            grade = 10
        students.get(int(string[2])).add_subjects(string[3],grade)
    for student in students.values():
        print("{}\n".format(student))