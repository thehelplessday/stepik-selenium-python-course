import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/selects1.html")



# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
num1 = driver.find_element_by_css_selector("#num1")

num2 = driver.find_element_by_css_selector("#num2")

sum= int(num1.text)+int(num2.text)


select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(str(sum)) # ищем элемент с текстом "Python"

driver.execute_script("alert('Hello!');")
button = driver.find_element_by_css_selector(".btn-default").click()

time.sleep(5)
# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()