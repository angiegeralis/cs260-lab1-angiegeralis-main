'''
TODO: add header here
'''

class Student:

    """ ========== TODO : START ========== """

    """TODO: Create a constructor."""


    """TODO: Write getters. Although not necessary in python, it is good
    practice to have getter and setter methods (as needed) for the sake of
    encapsulazation."""


    """TODO: Write the add course method"""


    """TODO: Write the drop course method"""


    """TODO: Write the __str__ method"""

    """ ========== TODO : END ========== """

def main():

    """ ========== TODO : START ========== """
    """TODO: Create an instance of Student and test all the methods"""

    print("Student Class Testing\n")
    # TODO create instance

    print("Testing the getters:")
    # TODO test getters

    print("\nTesting add_course and drop_course:")
    # TODO test add/drop

    print("\nTest __str__:")
    # TODO test __str__


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
