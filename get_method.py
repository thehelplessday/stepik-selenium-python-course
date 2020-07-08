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
driver.get("http://SunInJuly.github.io/execute_script.html")



# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
input_data = driver.find_element_by_css_selector("#input_value")
value = input_data.text

answer = calc(value)

textarea = driver.find_element_by_css_selector("#answer")

# Напишем текст ответа в найденное поле
textarea.send_keys(answer)


# Найдем кнопку, которая отправляет введенное решение
checkbox = driver.find_element_by_css_selector("#robotCheckbox").click()

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе

radiobutton = driver.find_element_by_css_selector("#robotsRule")
driver.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()
button = driver.find_element_by_css_selector(".btn-primary").click()
time.sleep(5)
# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()