import random

class XpathObjects:
    textBox = "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea"
    LoginButton = "/html/body/div[1]/section/main/div/div/article/div[3]/section[3]/div/span/a"
    PublishBtn = "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button"


class ListHelper:
    def __init__(self, user1, user2, user3, user4):
        self.user1 = user1
        self.user2 = user2
        self.user3 = user3
        self.user4 = user4

    def GetRandom_User_Order(self):

        Number = random.randint(1,9)

        Result = ""

        if Number == 1:
            Result = self.user1 + " " + self.user2
        
        if Number == 2:
            Result = self.user1 + " " + self.user3

        if Number == 3:
            Result = self.user1 + " " + self.user4

        '''USER 2 RESULT'''

        if Number == 4:
            Result = self.user2 + " " + self.user1
        
        if Number == 5:
            Result = self.user2 + " " + self.user3

        if Number == 6:
            Result = self.user2 + " " + self.user4


        '''USER 3 RESULT'''

        if Number == 7:
            Result = self.user3 + " " + self.user2
        
        if Number == 8:
            Result = self.user3 + " " + self.user1

        if Number == 9:
            Result = self.user3 + " " + self.user4

        
        return Result
    