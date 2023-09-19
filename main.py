# Program Name: Main Class
# Description: A program that control all processes
import os

from user_admin import UserAdmin
from user_teacher import UserTeacher
from user_student import UserStudent
from unit import Unit


def main_menu():
    # Function to display the main menu options
    print("\nMain Menu:")
    print("1. Login")
    print("2. Exit")


def generate_test_data():
    # Function to generate initial test data for users and units
    if os.path.exists("data/user.txt"):
        os.remove("data/user.txt")
    if os.path.exists("data/unit.txt"):
        os.remove("data/unit.txt")

    admin = UserAdmin(user_name="admin", user_password="password")
    with open("data/user.txt", "a", encoding='utf-8') as file:
        file.write(str(admin) + "\n")

    units = [
        Unit(unit_code="CSE101", unit_name="Introduction to Programming", unit_capacity=10),
        Unit(unit_code="CSE102", unit_name="Data Structures and Algorithms", unit_capacity=10),
        Unit(unit_code="CSE103", unit_name="Computer Organization", unit_capacity=10)
    ]
    for unit in units:
        with open("data/unit.txt", "a", encoding='utf-8') as file:
            file.write(str(unit) + "\n")

    teachers = [
        UserTeacher(user_name="teacher1", user_password="password", teach_units=["CSE101"]),
        UserTeacher(user_name="teacher2", user_password="password", teach_units=["CSE102"]),
        UserTeacher(user_name="teacher3", user_password="password", teach_units=["CSE103"])
    ]
    for teacher in teachers:
        with open("data/user.txt", "a", encoding='utf-8') as file:
            file.write(str(teacher) + "\n")

    students = [
        UserStudent(user_name=f"student{i}", user_password="password",
                    enrolled_units=[("CSE101", -1), ("CSE102", -1), ("CSE103", -1)]) for i in range(1, 11)
    ]
    for student in students:
        with open("data/user.txt", "a", encoding='utf-8') as file:
            file.write(str(student) + "\n")


def main():
    # Main function to run the program
    generate_test_data()
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            user_name = input("Enter your username: ")
            user_password = input("Enter your password: ")

            user_info = UserStudent.login(user_name, user_password)
            if user_info:
                user_info = user_info.split(", ")

                if user_info[3] == 'AD':
                    user = UserAdmin(user_id=int(user_info[0]), user_name=user_info[1], user_password=user_password)
                    admin_actions(user)
                elif user_info[3] == 'TA':
                    if len(user_info) < 6:
                        user = UserTeacher(user_id=int(user_info[0]), user_name=user_info[1],
                                           user_password=user_password,
                                           teach_units='')
                    else:
                        user = UserTeacher(user_id=int(user_info[0]), user_name=user_info[1],
                                           user_password=user_password, teach_units=user_info[5].split(", "))
                    teacher_actions(user)
                elif user_info[3] == 'ST':
                    if len(user_info) < 6:
                        enrolled_units = ''
                    else:
                        enrolled_units = [(unit_info.split(":")[0], int(unit_info.split(":")[1]))
                                          for unit_info in user_info[5].split("; ")]
                    user = UserStudent(user_id=int(user_info[0]), user_name=user_info[1], user_password=user_password,
                                       enrolled_units=enrolled_units)
                    student_actions(user)
            else:
                print("Invalid username or password. Try again.")
        elif choice == "2":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Try again.")


def admin_actions(user):
    while True:
        user.admin_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            user_name = input("Enter the username of the user to search: ")
            user.search_user(user_name)
        elif choice == "2":
            user.list_all_users()
        elif choice == "3":
            user.list_all_units()
        elif choice == "4":
            user_name = input("Enter the username of the user to enable/disable: ")
            user.enable_disable_user(user_name)
        elif choice == "5":
            user_name = input("Enter the username for the new user: ")
            user_password = input("Enter the password for the new user: ")
            user_role = input("Enter the role for the new user (AD/TA/ST): ")
            user_status = input("Enter the status for the new user (enabled/disabled): ")
            new_user = UserStudent(user_name=user_name, user_password=user_password, user_role=user_role,
                                   user_status=user_status)
            user.add_user(new_user)
        elif choice == "6":
            user_name = input("Enter the username of the user to delete: ")
            user.delete_user(user_name)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


def teacher_actions(user):
    while True:
        user.teacher_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            user.list_teach_units()
        elif choice == "2":
            unit_code = input("Enter the unit code for the new unit: ")
            unit_name = input("Enter the unit name for the new unit: ")
            unit_capacity = input("Enter the capacity for the new unit: ")
            new_unit = Unit(unit_code=unit_code, unit_name=unit_name, unit_capacity=unit_capacity)
            user.add_teach_unit(new_unit)
        elif choice == "3":
            unit_code = input("Enter the unit code of the unit to delete: ")
            user.delete_teach_unit(unit_code)
        elif choice == "4":
            unit_code = input("Enter the unit code of the unit to list enrolled students: ")
            user.list_enrol_students(unit_code)
        elif choice == "5":
            unit_code = input("Enter the unit code of the unit to show the avg/max/min score: ")
            user.show_unit_avg_max_min_score(unit_code)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


def student_actions(user):
    while True:
        user.student_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            user.list_available_units()
        elif choice == "2":
            user.list_enrolled_units()
        elif choice == "3":
            unit_code = input("Enter the unit code of the unit to enroll in: ")
            user.enrol_unit(unit_code)
        elif choice == "4":
            unit_code = input("Enter the unit code of the unit to drop: ")
            user.drop_unit(unit_code)
        elif choice == "5":
            unit_code = input("Enter the unit code of the unit to check the score (leave empty for all units): ")
            user.check_score(unit_code.strip() or None)
        elif choice == "6":
            unit_code = input("Enter the unit code of the unit to generate a score: ")
            user.generate_score(unit_code)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
