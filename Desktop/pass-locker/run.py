#!/usr/bin/env python3.6
from user import User 
from credentials import Credentials


def create_contact(fname,lname,number,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,number,email)
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

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()