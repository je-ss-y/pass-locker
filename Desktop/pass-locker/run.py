#!/usr/bin/env python3.6
from user import User 
from credentials import Credentials


def create_contact(fname,lname,number,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,number,email)
    return new_contact