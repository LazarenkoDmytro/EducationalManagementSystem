# Program Name: User Class
# Description: This program defines a User class that represents a user account.
#              It includes methods to generate a unique user ID, check if a user ID or username exists,
#              encrypt a password, and allow users to log in.

import random
import os


class User:
    def __init__(self, user_id=None, user_name=None, user_password=None, user_role=None, user_status='enabled'):
        """
        Initialize a new User object with the given parameters. If no user_id is provided,
        generate a unique user ID using the generate_user_id method.
        Encrypt the user_password using the encrypt method before storing it.
        """
        if user_id is None:
            self.user_id = self.generate_user_id()
        else:
            self.user_id = user_id
        self.user_name = user_name
        self.user_password = self.encrypt(user_password)
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        """
        Return a string representation of the User object.
        """
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}"

    def generate_user_id(self):
        """
        Generate a unique user ID by randomly selecting a 5-digit number between 10000 and 99999,
        and checking if it already exists in the "data/user.txt" file using the check_user_id_exists method.
        If the user ID is unique, return it.
        """
        while True:
            user_id = random.randint(10000, 99999)
            if not self.check_user_id_exists(user_id):
                return user_id

    @staticmethod
    def check_user_id_exists(user_id):
        """
        Check if the given user ID already exists in the "data/user.txt" file.
        If it does, return True. Otherwise, return False.
        """
        if os.path.exists("data/user.txt"):
            with open("data/user.txt", "r", encoding='utf-8') as file:
                for line in file.readlines():
                    if str(user_id) == line.strip().split(", ")[0]:
                        return True
        return False

    @staticmethod
    def check_username_exist(user_name):
        """
        Check if the given username already exists in the "data/user.txt" file.
        If it does, return True. Otherwise, return False.
        """
        if os.path.exists("data/user.txt"):
            with open("data/user.txt", "r", encoding='utf-8') as file:
                for line in file.readlines():
                    if user_name == line.strip().split(", ")[1]:
                        return True
        return False

    def encrypt(self, user_password):
        """
        Encrypt the given user password using two strings str_1 and str_2,
        then return the encrypted password.
        """
        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@^_`{|}~"

        encrypted_password = '^^^'
        for index, char in enumerate(user_password):
            ascii_num = ord(char)
            encrypted_password += str_1[ascii_num % len(str_1)] + str_2[index % len(str_2)]
        encrypted_password += '$$$'

        return encrypted_password

    @classmethod
    def login(cls, user_name, user_password):
        """
        Check if the given username and password match a user
        in the "data/user.txt" file and the user's status is "enabled".
        If they do, return the user information string from the file.
        Otherwise, return None.
        """
        if cls.check_username_exist(user_name):
            with open("data/user.txt", "r", encoding='utf-8') as file:
                for line in file.readlines():
                    user_info = line.strip().split(", ")
                    user = User(user_password=user_password)
                    if user_name == user_info[1] and user.encrypt(user_password) == user_info[2] \
                            and user_info[4] == 'enabled':
                        return line.strip()
        return None
