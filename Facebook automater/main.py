from selenium import webdriver
from time import sleep
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui


def login():
    user_ID = input("Enter your email id: ")
    user_PWD = input("Enter the password: ")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com/")

    username_box = driver.find_element_by_name('email')  # matching email id
    username_box.send_keys(user_ID)
    print('Sending email id...')

    sleep(1)

    userPass = driver.find_element_by_name('pass')  # matching password
    userPass.send_keys(user_PWD)
    print('Sending email password...')

    sleep(1)
    # loggin button through inspect element
    loginnow = driver.find_element_by_id('u_0_b')
    loginnow.submit()

    print('Looged in')
    sleep(1)
    # exit()


def comment(userinput):
    # userinput = "Comenting jsut for fun!"
    pyautogui.typewrite(userinput)
    pyautogui.typewrite("/n")
    print("Done")


login()
user = input("Press Y to comment on random post or N to exit.")
if user is "y":
    user = input("Type your comment: ")
    comment(user)
else:
    exit()
