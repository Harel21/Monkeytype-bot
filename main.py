from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import random

MY_CHROME_DRIVER_PATH = 'C:\Program Files\chromedriver.exe'
driverPath = input(
    'Enter your Chrome driver PATH. Leave empty if its: C:\Program Files\chromedriver.exe')

if driverPath == '':
    path = MY_CHROME_DRIVER_PATH
else:
    path = driverPath

driver = webdriver.Chrome(path)
driver.get('https://monkeytype.com/')

words = driver.find_elements_by_class_name("word")

print(f'length of words: {len(words)}')
print('starting!')


for word in words:

    for i in range(len(word.text)):
        startTime = time.time()
        letter = word.text[i]
        # waiting for random secs so that it dosent know that its a BOT ;)
        # time.sleep(random.randint(1, 2) / 100)
        # pyautogui.press(letter)
        pyautogui.write(letter)
        endTime = time.time()
        print(f'Loop took {endTime - startTime}')

    pyautogui.press('space')


print('done!')


time.sleep(5)
driver.quit()