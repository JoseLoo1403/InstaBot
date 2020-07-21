import random

class XpathObjects:
    textBox = "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea"
    LoginButton = "/html/body/div[1]/section/main/div/div/article/div[3]/section[3]/div/span/a"
    PublishBtn = "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button"
    ErrorButton = "/html/body/div[2]/div/div/button"

class ListHelper:
    def __init__(self, user1, user2, user3, user4, user5):
        self.user1 = user1
        self.user2 = user2
        self.user3 = user3
        self.user4 = user4
        self.user5 = user5

    def GetRandom_User_Order(self):

        Number = random.randint(1,20)

        Result = ""

        if Number == 1:
            Result = self.user1 + " " + self.user2
        
        if Number == 2:
            Result = self.user1 + " " + self.user3

        if Number == 3:
            Result = self.user1 + " " + self.user4

        if Number == 4:
            Result = self.user1 + " " + self.user5

        '''USER 2 RESULT'''

        if Number == 5:
            Result = self.user2 + " " + self.user1
        
        if Number == 6:
            Result = self.user2 + " " + self.user3

        if Number == 7:
            Result = self.user2 + " " + self.user4

        if Number == 8:
            Result = self.user2 + " " + self.user5


        '''USER 3 RESULT'''

        if Number == 9:
            Result = self.user3 + " " + self.user2
        
        if Number == 10:
            Result = self.user3 + " " + self.user1

        if Number == 11:
            Result = self.user3 + " " + self.user4

        if Number == 12:
            Result = self.user3 + " " + self.user5
        
        '''USER 4 RESULT '''

        if Number == 13:
            Result = self.user4 + " " + self.user2
        
        if Number == 14:
            Result = self.user4 + " " + self.user1

        if Number == 15:
            Result = self.user4 + " " + self.user3

        if Number == 16:
            Result = self.user4 + " " + self.user5

        '''USER 5 RESULT '''

        if Number == 17:
            Result = self.user5 + " " + self.user2
        
        if Number == 18:
            Result = self.user5 + " " + self.user1

        if Number == 19:
            Result = self.user5 + " " + self.user3

        if Number == 20:
            Result = self.user5 + " " + self.user4
        
        return Result

    def GetRandom_User_Order_By3(self):

        Number = random.randint(1,20)

        Result = ""

        if Number == 1:
            Result = self.user1 + " " + self.user2 + " " + self.user3
        
        if Number == 2:
            Result = self.user1 + " " + self.user3 + " " + self.user2

        if Number == 3:
            Result = self.user1 + " " + self.user4 + " " + self.user3

        if Number == 4:
            Result = self.user1 + " " + self.user5 + " " + self.user3

        '''USER 2 RESULT'''

        if Number == 5:
            Result = self.user2 + " " + self.user1 + " " + self.user3
        
        if Number == 6:
            Result = self.user2 + " " + self.user3 + " " + self.user4

        if Number == 7:
            Result = self.user2 + " " + self.user4 + " " + self.user1

        if Number == 8:
            Result = self.user2 + " " + self.user5 + " " + self.user3


        '''USER 3 RESULT'''

        if Number == 9:
            Result = self.user3 + " " + self.user2 + " " + self.user5
        
        if Number == 10:
            Result = self.user3 + " " + self.user1 + " " + self.user4

        if Number == 11:
            Result = self.user3 + " " + self.user4 + " " + self.user5

        if Number == 12:
            Result = self.user3 + " " + self.user5 + " " + self.user1
        
        '''USER 4 RESULT '''

        if Number == 13:
            Result = self.user4 + " " + self.user2 + " " + self.user3
        
        if Number == 14:
            Result = self.user4 + " " + self.user1 + " " + self.user5

        if Number == 15:
            Result = self.user4 + " " + self.user3 + " " + self.user2

        if Number == 16:
            Result = self.user4 + " " + self.user5 + " " + self.user3

        '''USER 5 RESULT '''

        if Number == 17:
            Result = self.user5 + " " + self.user2 + " " + self.user3
        
        if Number == 18:
            Result = self.user5 + " " + self.user1 + " " + self.user4

        if Number == 19:
            Result = self.user5 + " " + self.user3 + " " + self.user1

        if Number == 20:
            Result = self.user5 + " " + self.user4 + " " + self.user2
        
        return Result
    