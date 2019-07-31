from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
name = browser.find_element_by_name("firstname")
name.send_keys("Dima")
lastname = browser.find_element_by_name("lastname")
lastname.send_keys("Solonichenko")
email = browser.find_element_by_name("email")
email.send_keys("dsolonichenko@gmail.com")
file = browser.find_element_by_id("file")
file.send_keys("c:/chromedriver/1.txt")
button = browser.find_element_by_class_name("btn")
button.click()


