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