from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

site = webdriver.ChromeOptions()
# site

browser = webdriver.Chrome(options=site)

url = 'https://popcat.click'
browser.get(url)
browser.maximize_window()
sleep(2)

while 1:
    browser.find_element_by_xpath('//*[@id="app"]/img').click()
    browser.find_element_by_xpath('//*[@id="app"]/img').click()
    sleep(0.01)
