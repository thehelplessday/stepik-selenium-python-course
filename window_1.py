import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/redirect_accept.html")

redirect_button = driver.find_element_by_css_selector(".btn-primary").click()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

input_data = driver.find_element_by_css_selector("#input_value")
value = input_data.text

answer = calc(value)

textarea = driver.find_element_by_css_selector("#answer")

# Напишем текст ответа в найденное поле
textarea.send_keys(answer)


# Найдем кнопку, которая отправляет введенное решение


# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе

button = driver.find_element_by_css_selector(".btn-primary").click()
time.sleep(5)
# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()