class User:
    """
    class that genenarates new instances user-inputs

    """
    user_inputs_list = [] #empty list tohold user's inputs

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

    def save_inputs(self):

        """
        save_inputs method saves save_inputs object into our user_inputs_list

        """

        User.user_inputs_list.append(self)  


    

   