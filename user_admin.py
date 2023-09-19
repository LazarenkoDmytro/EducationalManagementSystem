# Program Name: UserAdmin Class
# Description: This program defines a UserAdmin class that represents an admin user account,
#              which is a subclass of the User class. It includes methods to manage user accounts
#              and course units.

import os

from user import User


class UserAdmin(User):
    def __init__(self, user_id=None, user_name=None, user_password=None, user_role='AD', user_status='enabled'):
        """
        Initialize a new UserAdmin object with the given parameters. Set user_role to 'AD' by default.
        """
        super().__init__(user_id=user_id, user_name=user_name, user_password=user_password,
                         user_role=user_role, user_status=user_status)

    def __str__(self):
        """
        Return a string representation of the UserAdmin object.
        """
        return super().__str__()

    def admin_menu(self):
        """
        Display the admin menu options.
        """
        print("\nAdmin Menu:")
        print("0. Log Out")
        print("1. Search User")
        print("2. List All Users")
        print("3. List All Units")
        print("4. Enable/Disable User")
        print("5. Add User")
        print("6. Delete User")

    def search_user(self, user_name):
        """
        Search for a user with the given username in the "data/user.txt" file and display their information.
        """
        if self.check_username_exist(user_name):
            with open("data/user.txt", "r", encoding='utf-8') as file:
                for line in file.readlines():
                    if user_name == line.strip().split(", ")[1]:
                        print(line.strip())
                        return
        print("User not found.")

    def list_all_users(self):
        """
        Display the information of all users in the "data/user.txt" file.
        """
        if os.path.exists("data/user.txt"):
            with open("data/user.txt", "r", encoding='utf-8') as file:
                for line in file.readlines():
                    print(line.strip())

    def list_all_units(self):
        """
        Display the information of all course units in the "data/unit.txt" file.
        """
        if os.path.exists("data/unit.txt"):
            with open("data/unit.txt", "r", encoding='utf-8') as file:
                for line in file.readlines():
                    print(line.strip())

    def enable_disable_user(self, user_name):
        """
        Enable or disable a user with the given username in the "data/user.txt" file,
        depending on their current status.
        """
        if self.check_username_exist(user_name):
            with open("data/user.txt", "r", encoding='utf-8') as file:
                lines = file.readlines()

            with open("data/user.txt", "w", encoding='utf-8') as file:
                for line in lines:
                    user_info = line.strip().split(", ")
                    if user_name == user_info[1]:
                        if user_info[4] == 'disabled':
                            user_info[4] = 'enabled'
                            print("User successfully enabled")
                        else:
                            user_info[4] = 'disabled'
                            print("User successfully disabled")
                        file.write(', '.join(user_info) + '\n')
                    else:
                        file.write(line)
        else:
            print("User not found.")

    def add_user(self, user_obj):
        """
        Add a new user with the given User object to the "data/user.txt" file.
        """
        if not self.check_username_exist(user_obj.user_name):
            if user_obj.user_role in ['AD', 'TA', 'ST'] and user_obj.user_status in ['enabled', 'disabled']:
                with open("data/user.txt", "a", encoding='utf-8') as file:
                    file.write(str(user_obj) + '\n')
                print("User successfully added")
            else:
                print("Invalid data. Try again")
        else:
            print("User with this username already exists.")

    def delete_user(self, user_name):
        """
        Delete a user with the given username from the "data/user.txt" file.
        """
        if self.check_username_exist(user_name):
            with open("data/user.txt", "r", encoding='utf-8') as file:
                lines = file.readlines()

            with open("data/user.txt", "w", encoding='utf-8') as file:
                for line in lines:
                    if user_name != line.strip().split(", ")[1]:
                        file.write(line)
            print("User successfully deleted")
        else:
            print("User not found.")
