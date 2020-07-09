import unittest
from selenium import webdriver
import time



class Testabs(unittest.TestCase):

    def test_reg1(self):
        browser = webdriver.Chrome()

        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input").send_keys("name")

        browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input").send_keys("lastname")

        browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input").send_keys("email")

        browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input").send_keys("phone")

        browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input").send_keys("Adres")

        browser.find_element_by_class_name('btn-default').click()

        time.sleep(2)

        cong = browser.find_element_by_tag_name("h1")


        congr = cong.text
        browser.quit()
        self.assertEqual(congr, "Congratulations! You have successfully registered!")


    def test_reg2(self):
        browser = webdriver.Chrome()

        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input").send_keys("name")

        browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input").send_keys("lastname")

        browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input").send_keys("email")

        browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input").send_keys("phone")

        browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input").send_keys("Adres")

        browser.find_element_by_class_name('btn-default').click()

        time.sleep(2)

        cong = browser.find_element_by_tag_name("h1")

        congr = cong.text
        browser.quit()
        self.assertEqual(congr, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()