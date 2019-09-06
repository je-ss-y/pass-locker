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


   
   
  
    

   

if __name__ ==  '__main__':
    unittest.main()
