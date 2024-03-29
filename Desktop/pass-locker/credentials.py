import pyperclip


class Credentials:
    """
    class that genenarates new instances for  user- credentials_inputs

    """
    credentials_inputs_list = [] #empty list tohold user's inputs

    def __init__(self,user_name,email,number):

        self.user_name = user_name
        self.email = email
        self.number = number

    def save_credentials(self):

        """
        save_inputs method saves save_credentials object into our user_inputs_list

        """

        Credentials.credentials_inputs_list.append(self)  

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_inputs_list
        '''

        Credentials.credentials_inputs_list.remove(self)

    def display_credentials(self):
        '''
        this method method that returns the credentials list
        '''
        self.credentials_inputs_list


    def find_credentials_by_number(cls,number):
        '''
        Method that takes in a number and returns credentials that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Credentials of person that matches the number.
        '''

        for credentials in cls. credentials_inputs_list:
            if credentials.number == number:
                return credentials
    @classmethod
    def credentials_exist(cls,number):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
       
        for credentials in cls. credentials_inputs_list:
            if credentials.number == number:
                return credentials

        return False

    

   

if __name__ ==  '__main__':
    unittest.main()
