# Program Name: UserStudent Class
# Description: A program that allows students to interact with a system to manage their courses.
import random

from user import User


class UserStudent(User):
    def __init__(self, user_id=None, user_name=None, user_password=None, user_role='ST', user_status='enabled',
                 enrolled_units=None):
        super().__init__(user_id=user_id, user_name=user_name, user_password=user_password, user_role=user_role,
                         user_status=user_status)
        self.enrolled_units = enrolled_units if enrolled_units else []

    def __str__(self):
        # convert the list of (unit_code, score) tuples into a string representation
        enrolled_units_str = "; ".join([f"{unit_code}:{score}" for unit_code, score in self.enrolled_units])
        if enrolled_units_str != '':
            return f"{super().__str__()}, {enrolled_units_str}"
        else:
            return f"{super().__str__()}"

    def student_menu(self):
        """
        Displays the student menu options
        """
        print("\nStudent Menu:")
        print("0. Log Out")
        print("1. List Available Units")
        print("2. List Enrolled Units")
        print("3. Enrol Unit")
        print("4. Drop Unit")
        print("5. Check Score")
        print("6. Generate Score")

    def list_available_units(self):
        """
        Lists all available units that the student can enroll in.
        """
        with open("data/unit.txt", "r", encoding='utf-8') as file:
            unit_data = file.readlines()
            enrolled_unit_codes = [unit_code for unit_code, _ in self.enrolled_units]

            available_units = []

            for line in unit_data:
                unit_info = line.strip().split(", ")
                unit_code = unit_info[1]
                unit_capacity = int(unit_info[3])

                if unit_code not in enrolled_unit_codes and unit_capacity > 0:
                    available_units.append(line.strip())

            if available_units:
                for unit in available_units:
                    print(unit)
            else:
                print("No available units to enroll.")

    def list_enrolled_units(self):
        """
        Lists all the units that the student has enrolled in along with their score.
        """
        if not self.enrolled_units:
            print("You have not enrolled in any units yet.")
        else:
            for unit_code, score in self.enrolled_units:
                print(f"Unit: {unit_code}, Score: {score}")

    def enrol_unit(self, unit_code):
        """
        Enrolls the student in a unit.
        """
        if len(self.enrolled_units) >= 3:
            print("You have reached the maximum number of enrollments.")
            return

        with open("data/unit.txt", "r", encoding='utf-8') as file:
            unit_data = file.readlines()
            for line in unit_data:
                unit_info = line.strip().split(", ")
                if unit_code == unit_info[1]:
                    if int(unit_info[3]) > 0:
                        self.enrolled_units.append((unit_code, -1))
                        print(f"Successfully enrolled in unit {unit_code}.")
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
                        return
                    else:
                        print("This unit has reached its maximum capacity.")
            print("Unit not found.")

    def drop_unit(self, unit_code):
        """
        Drops a unit that the student has enrolled in.
        """
        for i, (enrolled_unit_code, _) in enumerate(self.enrolled_units):
            if unit_code == enrolled_unit_code:
                self.enrolled_units.pop(i)
                print(f"Successfully dropped unit {unit_code}.")

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
                return
        print("Unit not found in your enrolled units.")

    def check_score(self, unit_code=None):
        """
        Checks the score of a unit that the student has enrolled in.
        If no unit is specified, it lists all the units that the student has enrolled in along with their score.
        """
        if unit_code:
            for enrolled_unit_code, score in self.enrolled_units:
                if unit_code == enrolled_unit_code:
                    print(f"Unit: {unit_code}, Score: {score}")
                    return
            print("Unit not found in your enrolled units.")
        else:
            self.list_enrolled_units()

    def generate_score(self, unit_code):
        """
        Generates a random score for the unit that the student has enrolled in.
        """
        for i, (enrolled_unit_code, _) in enumerate(self.enrolled_units):
            if unit_code == enrolled_unit_code:
                score = random.randint(0, 100)
                self.enrolled_units[i] = (unit_code, score)
                print(f"Generated score for unit {unit_code}: {score}")

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
                return
        print("Unit not found in your enrolled units.")
