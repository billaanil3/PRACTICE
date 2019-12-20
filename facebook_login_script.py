#http://cn.moneyskillsacademy.com/video/nfT-6H3xyhPK3I
from selenium import webdriver
from getpass import getpass

usr = input("Enter your email or user-name:")
pwd = getpass("Enter your password:")

#chromedriver = '/home/anil/Downloads/google-chrome-stable_current_amd64.deb'
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

passwrd_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_2')
login_btn.submit()

