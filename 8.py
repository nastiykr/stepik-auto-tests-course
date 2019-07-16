from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_id('input_value')
x = x_element.text


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


y = calc(x)


input3 = browser.find_element_by_id('answer')
input3.send_keys(y) 

option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("[for='robotsRule']")
option2.click()


button = browser.find_element_by_css_selector("button.btn")
button.click()