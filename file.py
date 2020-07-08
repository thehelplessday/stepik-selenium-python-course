import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/file_input.html")



# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
name = driver.find_element_by_css_selector("[name='firstname']")
name.send_keys('lokh')
surname = driver.find_element_by_css_selector("[name='lastname']")
surname.send_keys('pidor')
email = driver.find_element_by_css_selector("[name='email']")
email.send_keys('ertertert')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')

upload = driver.find_element_by_css_selector("#file")

upload.send_keys(file_path)


button = driver.find_element_by_css_selector(".btn-primary").click()
time.sleep(5)
# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()