import requests
import os

class DataManager:

    def __init__(self):
        self.sheety_endpoint = f"https://api.sheety.co/094464ab85b23bc8ee502c81ae9ba13e/flightDeals/prices/"
        self.sheety_header = {"Authorization": os.environ["SHEETY_HEADER"]}
        self.sheety_inputs = {"price": {"iataCode": ""}}

    def get_sheet_data(self):
        return requests.get(url=self.sheety_endpoint, headers=self.sheety_header).json()

    def add_row(self):
        add_row = requests.post(url=self.sheety_endpoint, json=self.sheety_inputs, headers=self.sheety_header)
        print(add_row)
        print(add_row.text)

    def edit_row(self, row_number, text):
        edit_inputs = {"price": {"iataCode": text}}
        edit_row = requests.put(url=f"{self.sheety_endpoint}/{row_number}",
                                json=edit_inputs, headers=self.sheety_header)
        print(edit_row)
        print(edit_row.text)

    # def user_reg(self, name, l_name, email):
    #     sheety_endpoint = "https://api.sheety.co/094464ab85b23bc8ee502c81ae9ba13e/flightDeals/users"
    #     sheety_inputs = {
    #         "user": {
    #                 "firstName": name,
    #                 "lastName": l_name,
    #                 "email": email
    #         }
    #     }
    #     requests.post(url=sheety_endpoint, json=sheety_inputs, headers=self.sheety_header)
    #
    # # New user registration
    # def new_user(self):
    #     name = input("What's your first Name?\n")
    #     l_name = input("What's your last name?\n")
    #     email = input("What's your email?\n")
    #     email_v = input(f"Type your email again.\n")
    #
    #     if email == email_v:
    #         self.user_reg(name, l_name, email)
    #         print("You are in the club.")
    #     else:
    #         print("The email is not the same.")
