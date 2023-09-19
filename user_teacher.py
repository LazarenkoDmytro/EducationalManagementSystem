# Program Name: UserTeacher Class
# Description: This program defines the class UserTeacher which is a subclass of User, used for teacher user role. It
#              provides various methods to perform operations like listing teach units, adding teach unit, deleting
#              teach unit, listing enrolled students and showing unit average, maximum and minimum scores. The program
#              reads and writes user and unit data from and to text files in data directory using utf-8 encoding.

import re

from user import User


class UserTeacher(User):
    def __init__(self, user_id=None, user_name=None, user_password=None, user_role='TA', user_status='enabled',
                 teach_units=None):
        # Constructor to initialize UserTeacher object
        super().__init__(user_id=user_id, user_name=user_name, user_password=user_password, user_role=user_role,
                         user_status=user_status)
        self.teach_units = teach_units if teach_units else []

    def __str__(self):
        # String representation of UserTeacher object
        if not self.teach_units:
            return f"{super().__str__()}"
        else:
            return f"{super().__str__()}, {', '.join(self.teach_units)}"

    def teacher_menu(self):
        # Method to display teacher menu
        print("\nTeacher Menu:")
        print("0. Log Out")
        print("1. List Teach Units")
        print("2. Add Teach Unit")
        print("3. Delete Teach Unit")
        print("4. List Enrol Students")
        print("5. Show Unit Avg, Max, Min Score")

    def list_teach_units(self):
        # Method to list teach units
        if self.teach_units:
            with open("data/unit.txt", "r", encoding='utf-8') as file:
                unit_data = file.readlines()
                unit_data = [line.strip() for line in unit_data]
                for unit_code in self.teach_units:
                    for unit_info in unit_data:
                        if unit_code == unit_info.split(", ")[1]:
                            print(unit_info)
                            break
        else:
            print("No units taught by this teacher are found in the system.")

    def add_teach_unit(self, unit_obj):
        # Method to add teach unit
        if unit_obj.unit_code not in self.teach_units:
            if unit_obj.unit_capacity.isnumeric() and int(unit_obj.unit_capacity) > 0:
                with open("data/unit.txt", "r", encoding='utf-8') as file:
                    for line in file:
                        existing_unit = line.strip().split(", ")
                        if existing_unit[1] == unit_obj.unit_code:
                            print("This unit already exists in dataset.")
                            return

                self.teach_units.append(unit_obj.unit_code)
                with open("data/unit.txt", "a", encoding='utf-8') as file:
                    file.write(str(unit_obj) + '\n')
                users = []
                with open("data/user.txt", "r", encoding='utf-8') as file:
                    users = file.readlines()
                with open("data/user.txt", "w", encoding='utf-8') as file:
                    for user in users:
                        user_info = user.strip().split(", ")
                        if user_info[0] == str(self.user_id):
                            updated_user_info = self.__str__()
                            file.write(updated_user_info + "\n")
                        else:
                            file.write(user)
                print("Unit successfully added")
            else:
                print("Invalid data. Try again")
        else:
            print("This unit is already in the teacher's teach_units list.")

    def delete_teach_unit(self, unit_code):
        # Method to delete teach unit
        if unit_code in self.teach_units:
            self.teach_units.remove(unit_code)
            with open("data/unit.txt", "r", encoding='utf-8') as file:
                lines = file.readlines()
            with open("data/unit.txt", "w", encoding='utf-8') as file:
                for line in lines:
                    if unit_code != line.strip().split(", ")[1]:
                        file.write(line)
            with open("data/user.txt", "r", encoding='utf-8') as file:
                users = file.readlines()
            with open("data/user.txt", "w", encoding='utf-8') as file:
                for user in users:
                    user_info = user.strip().split(", ")
                    if user_info[0] == str(self.user_id):
                        updated_teacher_info = self.__str__()
                        file.write(updated_teacher_info + "\n")
                    else:
                        if user_info[3] == 'ST':
                            enrolled_units = [unit for unit in user_info[5].split("; ") if
                                              unit.split(":")[0] != unit_code]
                            updated_enrolled_units = "; ".join(enrolled_units)
                            user_info[5] = updated_enrolled_units

                        updated_user_info = ", ".join(user_info)
                        file.write(updated_user_info + "\n")

            print("Unit successfully deleted")
        else:
            print("Unit not found in the teacher's teach_units list.")

    def list_enrol_students(self, unit_code):
        # Method to list enrolled students for a teach unit
        if unit_code in self.teach_units:
            student_list = []
            with open("data/user.txt", "r", encoding='utf-8') as file:
                user_data = file.readlines()
                for line in user_data:
                    user_info = line.strip().split(", ")
                    if user_info[3] == 'ST' and re.search(fr'\b{unit_code}\b', user_info[5]):
                        student_list.append(user_info[1])
            if student_list:

                print("Students enrolled in the unit:")
                for student in student_list:
                    print(student)
            else:
                print("No students found enrolled in the unit.")
        else:
            print("This unit is not in teacher's units list. Try again")

    def show_unit_avg_max_min_score(self, unit_code):
        # Method to show unit average, maximum and minimum scores
        if unit_code in self.teach_units:
            scores = []
            with open("data/user.txt", "r", encoding='utf-8') as file:
                user_data = file.readlines()
                for line in user_data:
                    user_info = line.strip().split(", ")
                    if user_info[3] == 'ST' and re.search(fr'\b{unit_code}\b', user_info[5]):
                        score_match = re.search(fr'{unit_code}:(-?\d+)', user_info[5])
                        if score_match:
                            score = int(score_match.group(1))
                            if score != -1:
                                scores.append(score)
            if scores:
                print(
                    f"Unit {unit_code} - Avg: {sum(scores) / len(scores):.2f}, Max: {max(scores)}, Min: {min(scores)}")
            else:
                print("No scores found for the unit.")
        else:
            print("This unit is not in teacher's units list. Try again")
