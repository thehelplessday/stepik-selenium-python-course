from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element_by_css_selector(".btn-primary").click()

input_data = browser.find_element_by_css_selector("#input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", input_data)
value = input_data.text

answer = calc(value)

textarea = browser.find_element_by_css_selector("#answer")
textarea.send_keys(answer)

button = browser.find_element_by_id("solve").click()
time.sleep(5)
# После выполнения всех действий мы не должны забыть закрыть окно браузера
browser.quit()