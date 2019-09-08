import unittest #importing the unittest module
from credentials import Credentials


class TestUserCredentials(unittest.TestCase):

     def setUp(self):
        """
        set up method to run before each test cases

        """
        self.new_user_credentials = Credentials("username","useremail","usernumber")

     def test_init(self):
        """
        test_init to test if the object is initialized properly

        """

        self.assertEqual(self.new_user_credentials.user_name,"username")
        self.assertEqual(self.new_user_credentials.email,"useremail")
        self.assertEqual(self.new_user_credentials.number,"usernumber")

    
    
     def test_save_multiple_credentials(self):
        """
        test_save_multiple_inputs to check if we can save multiple user_inputs into our object new_user_inputs

        """
        self.new_user_credentials.save_credentials()
        new_user_credentials = Credentials("user","test@user.com","0788456789")#new inputs
        new_user_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_inputs_list),2)

     def tearDown(self):

        """
        teardown method to clean up after each test case has run
        """
        Credentials.credentials_inputs_list= []

     def test_delete_credentials(self):

         """
         testdelete to test if we can remove credentials

         """
         self.new_user_credentials.save_credentials()
         new_user_credentials = Credentials("user","test@user.com","0788456789")#new inputs
         new_user_credentials.save_credentials()

         self.new_user_credentials.delete_credentials()# Deleting a credential object
         self.assertEqual(len( Credentials.credentials_inputs_list),1)

        
     def test_display_credentials(self):
        '''
        this method will return a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(self),Credentials.credentials_inputs_list)


    
     def test_find_credentials_by_number(self):
         
         """
         this will check if we can find credentials by phone number and display information

         """
         self.new_user_credentials.save_credentials()
         test_crendentials = Credentials("user","test@user.com","0788456789")
         test_crendentials.save_credentials()

         found_credentials = Credentials.number("0788456789")

         self.assertEqual(found_credentials.email,test_crendentials.email)

     def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_user_credentials.save_credentials()
        test_crendentials = Credentials("user","test@user.com","0788456789") 
        test_crendentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("0788456789")

        self.assertTrue(credentials_exists)
  
        
        



    

if __name__ ==  '__main__':
    unittest.main()
