from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import Utils
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/p/CCZzrs4jk5O/")


Helper = Utils.ListHelper('@sampineda18','@clementeramost ','@jair.abdul','@jaysonerazo','@francesca_bano')
XpathHelper = Utils.XpathObjects


UsersList = list()

#fill the list of comments with random order users
def FillUsers():
    UsersList.clear()

    for p in range(20):
        UsersList.append(Helper.GetRandom_User_Order())
    
    print("Combinaciones hechas")
    

#Make login click
sleep(6)
LogBtn = driver.find_element_by_xpath(XpathHelper.LoginButton)
LogBtn.click()

#verify if its block
def VerifyErrorButton():
    try:
        ErrorBtn = driver.find_element_by_xpath(XpathHelper.ErrorButton)
        ErrorBtn.click()
    except:
        return False
    
    print("Error detectado")
    return True


#Make publish with error button



#Make comment function
def MakeComments():
    for x in UsersList:
        TextBox = driver.find_element_by_xpath(XpathHelper.textBox)
        TextBox.send_keys(x)
        sleep(2)

        Publish = driver.find_element_by_xpath(XpathHelper.PublishBtn)
        Publish.click()

        sleep(1)

        if VerifyErrorButton():
            sleep(10)
            driver.refresh()
            sleep(10)
            driver.refresh()

        sleep(random.randint(5,10))

    print("Compltado!")


verificator = "1"
 
while(verificator == "1"):
    Selector = input("Que desea hacer?")

    for x in range(10):
        sleep(1)
        if Selector == "1":
            try:
                FillUsers()
                MakeComments()
            except:
                print("Error al publicar")
    
    verificator = input("Quiere seguir?")