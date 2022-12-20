import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class Test_pages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.option = Options()
        cls.option.headless = True
        cls.driver = webdriver.Chrome(options=cls.option)

    def setUp(self):
        self.driver.get('http://127.0.0.1:4999')
        warnings.simplefilter('ignore')

    # @unittest.skip
    def test_about_us_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/about_us"]')
        element.click()
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999/class/about_us'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_log_in_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        element.click()
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999/login'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_sign_up_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/signup"]')
        element.click()
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999/signup'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_About_classes_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        element.click()
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999/'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_show_classes_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        a = ActionChains(self.driver)
        a.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/show_classes"]')
        element.click()
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999/class/show_classes'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_timetable_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        a = ActionChains(self.driver)
        a.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/aboutclasses/timetable"]')
        element.click()
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999/class/aboutclasses/timetable'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_prices_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        a = ActionChains(self.driver)
        a.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/aboutclasses/prices"]')
        element.click()
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999/class/aboutclasses/prices'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_tutor_info_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        a = ActionChains(self.driver)
        a.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/aboutclasses/tutor_info"]')
        element.click()
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999/class/aboutclasses/tutor_info'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()