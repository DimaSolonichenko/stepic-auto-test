from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

a = browser.find_element_by_id("num1").text
b = browser.find_element_by_id("num2").text
print(a)
print(b)
c = int(a) + int(b)
select = Select(browser.find_element_by_tag_name("select"))

select.select_by_value(str(c))
button = browser.find_element_by_class_name("btn")
button.click()
