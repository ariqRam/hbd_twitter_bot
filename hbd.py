from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pynput.keyboard import Key, Controller

from datetime import datetime

from threading import Timer

import keyboard

import time

key = Controller()

def login(e, p):
	email_xpath = '/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input'
	password_xpath = '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'
	login_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div'

	driver.find_element_by_xpath(email_xpath).send_keys(e)
	driver.find_element_by_xpath(password_xpath).send_keys(p)
	time.sleep(1)
	driver.find_element_by_xpath(login_button_xpath).click()

def open_user_page():
    
	try:
		user_login_xpath = '/html/body/div/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div[1]/div[1]/a/div/span/span'
		driver.find_element_by_xpath(user_login_xpath).click()
	except: 
		user_login_xpath = '/html/body/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/a/div/span/span'
		driver.find_element_by_xpath(user_login_xpath).click()

def find_message():
	try: 
		msg_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]'
		userName = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, msg_button_xpath)))
		driver.find_element_by_xpath(msg_button_xpath).click()
	except:
		msg_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]'
		userName = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, msg_button_xpath)))
		driver.find_element_by_xpath(msg_button_xpath).click()

def write_message(msg):
    #//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div/aside/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div
    # text_field_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div/div/div/aside/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span'
    # text_field_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div/aside/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
    text_field_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div/div/div/aside/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, text_field_xpath)))
    driver.find_element_by_xpath(text_field_xpath).click()
    keyboard.write(msg)

def hbd(email, password):
    msg = open('hbd.txt').read().replace('\n', ' ')

    user_login_x = '/html/body/div/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div[1]/div[1]/a/div/span/span'
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, user_login_x)))

    open_user_page()
    email_x = '/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input'
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, email_x)))

    login(email, password)
    
    find_message()
    
    write_message(msg)

    key.press(Key.enter)
    key.release(Key.enter)

browser = input('browser choice(f or c):')
jam = int(input('hour:'))
menit = int(input('minute:'))
target = input('target account:')
words = input('message fille(.txt):')
email = input('sender email:')
password = input('password:')

firefox_driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')
chrome_driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver = firefox_driver if browser == "f" else chrome_driver
# executable_path=r'C:\src\geckodriver.exe'
driver.get('https://twitter.com/{}'.format(target))

x=datetime.today()
y=x.replace(hour=jam, minute=menit, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1
func = hbd(email, password)
t = Timer(secs, func)
t.start()
