#!/usr/bin/env python3.6
from user import User 
from credentials import Credentials


def create_contact(fname,lname,phone_number,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone_number,email)
    return new_contact

def save_credentials(credentials):
    '''
    Function to save  user's credentials
    '''
    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    Function to delete user's credentials
    '''
    credentials.delete_credentials()


def find_credentials_by_number(number):
    '''
    Function that finds credentials by number and returns the credentials
    '''
    return Credentials.find_by_number(number)

def check_existing_credentials(number):
    '''
    Function that check if user's credentials exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(number)

def display_credentials(self):
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

  ####calling the functions to be implemented above####


def main():
        print("Hello Welcome to your credentials list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the credentials list ")

                short_code = input().lower()

                if short_code == 'cc':
                        print("New Contact")
                        print("-"*10)

                        print ("User_name ....")
                        User_name = input()

                        print("Phone number ...")
                        p_number = input()

                        print("Email address ...")
                        e_address = input()

                        print("password ...")
                        password= input()


                        save_contacts(create_contact(User_name,password,p_number,e_address)) # create and save new credentials.
                        print ('\n')
                        print(f"New Contact {User_name} created")
                        print ('\n')

                elif short_code == 'dc':

                        if display_credentials():
                                print("Here is a list of all your credentials")
                                print('\n')

                                for credentials in display_credentials():
                                        print(f"Username:{credentials.first_name}/n Password:{credentials.last_name} /n Phone_number{credentials.phone_number}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any credentials saved yet")
                                print('\n')

                elif short_code == 'fc':

                        print("Enter the number you want to search for")

                        search_number = input()
                        if check_existing_credentials(search_number):
                                search_credentials = find_credentials_by_number(search_number)
                                print(f"{search_credentials.first_name} {search_credentials.last_name}")
                                print('-' * 20)

                                print(f"Phone number.......{search_credentials.phone_number}")
                                print(f"Email address.......{search_credentials.email}")
                        else:
                                print("That credential does not exist")

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
        main()