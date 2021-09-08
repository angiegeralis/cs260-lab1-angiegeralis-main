'''
Author      : Angie Geralis
Class       : CS260
Date        : 9/7/21
Description : This is the Student class in part 4 of lab 1 class that takes the
full name of the student, their graduating year, and their TriCo college. Each
student should also have a list of courses they are taking for the current semester.
We use this class to practice getter and __str__ methods, as well as write methods
for adding or dropping courses to the list of courses they are taking. Additionally,
a dictionary of students is created with assigned ID numbers (keys).

'''
class Student:

    """ ========== TODO : START ========== """

    """TODO: Create a constructor."""
    def __init__(self, student_name, student_year, student_college):
        self.name = student_name
        self.year = student_year
        self.college = student_college
        self.classes = []
    """TODO: Write getters. Although not necessary in python, it is good
    practice to have getter and setter methods (as needed) for the sake of
    encapsulazation."""
    def get_student_name(self):
        return self.name
    def get_student_year(self):
        return self.year
    def get_student_college(self):
        return self.college
    def get_student_classes(self):
        return self.classes
    """TODO: Write the add course method"""
    def add_course(self, course):
        # check through list of classes, if you already have that class,
        # tell the user that you are already enrolled. If not, add the class
        # to the list
        course_browser = True
        for i in range(len(self.classes)):
            if self.classes[i] == course:
                course_browser = False
                print("Already enrolled. You cannot add the same class twice.")
        if course_browser == True:
            self.classes.append(course)

    """TODO: Write the drop course method"""
    def drop_course(self, course):
        # check through the list of classes, if you find the class that matches
        # the parameter, remove the class. If not, tell the user they are not enrolled
        course_browser = True
        for i in range(len(self.classes)):
            if self.classes[i] == course:
                course_browser = False
                self.classes.remove(course)
        if course_browser == True:
            print("Not enrolled. You cannot remove a class you don't take.")

    """TODO: Write the __str__ method"""
    def __str__(self):
        s = "Student: %s , Year: %i , College: %s , Classes: %a" % (self.name, self.year, self.college, self.classes)
        return s

    """ ========== TODO : END ========== """

def main():

    """ ========== TODO : START ========== """
    """TODO: Create an instance of Student and test all the methods"""

    print("Student Class Testing\n")
    # TODO create instance
    bob = Student("Bob",2024,"Haverford College")
    print("Testing the getters:")
    # TODO test getters
    print(bob.get_student_name())
    print(bob.get_student_year())
    print(bob.get_student_college())

    print("\nTesting add_course and drop_course:")
    # TODO test add/drop
    bob.add_course("CMSC260")
    bob.add_course("CMSC260")
    print("\nTest __str__:")
    # TODO test __str__
    print(bob)


    student_lst = [["Fiona Xu", 2022, "Haverford College"],
                    ["Ivy Zhang", 2024, "Bryn Mawr College"],
                    ["Alton Wiggers", 2025, "Swarthmore College"],
                    ["Luis Contreras-Orendain", 2022, "Haverford College"],
                    ["Lizzie Spano", 2023, "Bryn Mawr College"]]

    print("Student Dictionary Exercises\n")
    # TODO create dictionary called students
    students = {}
    print("Dictionary contents:")
    #print_dict(students) uncomment
    students[123] = Student(student_lst[0][0],student_lst[0][1],student_lst[0][2]) #123 is student ID
    students[345] = Student(student_lst[1][0],student_lst[1][1],student_lst[1][2])
    students[678] = Student(student_lst[2][0],student_lst[2][1],student_lst[2][2])
    students[910] = Student(student_lst[3][0],student_lst[3][1],student_lst[3][2])
    students[112] = Student(student_lst[4][0],student_lst[4][1],student_lst[4][2])
    print("Trying to add a student with same key:")
    # TODO
    angie = Student("Angie Geralis",2024,"Haverford College")
    students[123] = angie #reassign 123 as angie's student ID
    print("Dictionary contents afterwards:")
    print_dict(students)

    print("Trying to add a student with new key and a repeated value/Student:")
    # TODO
    students[111] = angie #give angie a second student ID
    print("Dictionary contents afterwards:")
    print_dict(students)

    specific_id = 345 # TODO
    print("Getting Student at key %i:" % (specific_id))
    # prints info of student corresponding to ID 345
    print(students[345])
    print("Removing Student at key %i:" % (specific_id))
    students.pop(345) #pop removes a student from list
    print("Dictionary contents afterwards:")
    print_dict(students) #prints dictionary without student corresponding to ID345

    """ ========== TODO : END ========== """


def print_dict(dictionary):
    """Function that prints out the keys and values in a dictionary"""
    for key, val in dictionary.items():
        print(key, val)


if __name__ == "__main__":
    main()
