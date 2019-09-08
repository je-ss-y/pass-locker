import unittest #importing the unittest module
from user import User 
from credentials import Credentials


class TestUserInputs(unittest.TestCase):
    def setUp(self):
        """
        set up method to run before each test cases

        """
        self.new_user_inputs = User("username","userpassword")

    def test_init(self):
        """
        test_init to test if the object is initialized properly

        """

        self.assertEqual(self.new_user_inputs.user_name,"username")
        self.assertEqual(self.new_user_inputs.password,"userpassword")

    def test_save_inputs (self):
        
        """
        test_save_inputs to test if the new_user_inputs object is saved into the  user_inputs_list
        """

        self.new_user_inputs.save_inputs() # saving the new inputs
        self.assertEqual(len(User.user_inputs_list),1)

    


    

if __name__ ==  '__main__':
    unittest.main()
   


