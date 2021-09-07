'''
TODO: add header here
'''
class Student:

    """ ========== TODO : START ========== """

    """TODO: Create a constructor."""
    def __init__(self, student_name, student_year, student_college):
        self.name = student_name
        self.year = student_year
        self.college = student_college
        self.classes = student_classes = []
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
        for i in range(len(self.classes)):
            if i == course:
                print("Already enrolled. You cannot add the same class twice.")
            else:
                self.classes.append(course)

    """TODO: Write the drop course method"""
    def drop_course(self, course):
        # check through the list of classes, if you find the class that matches
        # the parameter, remove the class. If not, tell the user they are not enrolled
        for i in range(len(self.classes)):
            if i == course:
                self.classes.remove(course)
            else:
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
    bob = Student("Bob",2024,"Haverford")
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

    print("Dictionary contents:")
    #print_dict(students) uncomment

    print("Trying to add a student with same key:")
    # TODO

    print("Dictionary contents afterwards:")
    #print_dict(students) uncomment

    print("Trying to add a student with new key and a repeated value/Student:")
    # TODO

    print("Dictionary contents afterwards:")
    #print_dict(students) uncomment

    specific_id = None # TODO
    print("Getting Student at key %i:" % (specific_id))
    # TODO

    print("Removing Student at key %i:" % (specific_id))
    print("Dictionary contents afterwards:")
    #print_dict(students) uncomment

    """ ========== TODO : END ========== """


def print_dict(dictionary):
    """Function that prints out the keys and values in a dictionary"""
    for key, val in dictionary.items():
        print(key, val)


if __name__ == "__main__":
    main()
