import random

class XpathObjects:
    textBox = "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea"
    LoginButton = "/html/body/div[1]/section/main/div/div/article/div[3]/section[2]/div/span/a"
    PublishBtn = "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button"


class ListHelper:
    def __init__(self, user1, user2, user3):
        self.user1 = user1
        self.user2 = user2
        self.user3 = user3

    def GetRandom_User_Order(self):

        Number = random.randint(1,3)

        Result = ""

        if Number == 1:
            Result = self.user1 + " " + self.user2 + " " + self.user3
        
        if Number == 2:
            Result = self.user2 + " " + self.user1 + " " + self.user3

        if Number == 3:
            Result = self.user3 + " " + self.user2 + " " + self.user1

        return Result
        
    