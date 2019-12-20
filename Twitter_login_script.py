#https://www.youtube.com/watch?v=g_p70uVN1XA
from selenium import webdriver
from getpass import getpass


#chromedriver = '/home/anil/Downloads/google-chrome-stable_current_amd64.deb'
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")
usr = input("Enter your email or user-name:")
pwd = getpass("Enter your password:")

username_box = driver.find_element_by_class_name('js_username_field')
username_box.send_keys(usr)

passwrd_box = driver.find_element_by_class_name('js_password_field')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_css_selector('button.submit.Edgebutton.Edgebutton--primary.EdgeButton--medium')
login_btn.submit()

