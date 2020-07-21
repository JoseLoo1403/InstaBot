from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import Utils

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/p/CC2r0WzlCap/")


Helper = Utils.ListHelper('hola','2','hola34')
XpathHelper = Utils.XpathObjects


UsersList = list()

for p in range(10):
    UsersList.append(Helper.GetRandom_User_Order())

sleep(6)

LogBtn = driver.find_element_by_xpath(XpathHelper.LoginButton)
LogBtn.click()


def MakeComments():
    for x in UsersList:
        TextBox = driver.find_element_by_xpath(XpathHelper.textBox)
        TextBox.send_keys(x)
        sleep(3)
        Publish = driver.find_element_by_xpath(XpathHelper.PublishBtn)
        Publish.click()
        sleep(3)


verificator = "1"

while(verificator == "1"):
    Selector = input()

    if Selector == "1":
        MakeComments()
    
    verificator = input("Quiere seguir?")