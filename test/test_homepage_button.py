from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import warnings

class Test_web_app(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.option = Options()
        cls.option.headless = True
        cls.driver = webdriver.Chrome(options=cls.option)
        

    def setUp(self):
        self.driver.get('http://127.0.0.1:4999')
        warnings.simplefilter("ignore")

    # @unittest.skip
    def test_land_on_homepage(self):
        actual = "Gym"
        element = self.driver.find_element(By.CSS_SELECTOR, 'title')
        expected = element.get_attribute('textContent')
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_about_us_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/about_us"]')
        actual = element.get_attribute('textContent')
        expected = 'About us'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_Log_in_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        actual = element.get_attribute('textContent')
        expected = 'Log in'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_sign_up_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/signup"]')
        actual = element.get_attribute('textContent')
        expected = 'Sign up'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_About_classes_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        actual = element.get_attribute('textContent')
        expected = 'About classes'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_show_classes_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/show_classes"]')
        actual = element.get_attribute('textContent')
        expected = 'Show Classes'
        self.assertEqual(actual, expected)
    
    # @unittest.skip
    def test_time_table_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/aboutclasses/timetable"]')
        actual = element.get_attribute('textContent')
        expected = 'Timetable'
        self.assertEqual(actual, expected)

    # @unittest.skip
    def test_prices_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/aboutclasses/prices"]')
        actual = element.get_attribute('textContent')
        expected = 'Prices'
        self.assertEqual(actual, expected)

        # @unittest.skip
    def test_about_tutor_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/class/aboutclasses/tutor_info"]')
        actual = element.get_attribute('textContent')
        expected = 'About Tutor'
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()