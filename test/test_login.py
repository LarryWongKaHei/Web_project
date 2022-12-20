import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.option = Options()
        # cls.option.headless = True
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get('http://127.0.0.1:4999/login')
        warnings.simplefilter('ignore')

    @unittest.expectedFailure
    # @unittest.skip
    def test_input_name_only(self):
        element = self.driver.find_element(By.NAME, 'name')
        element.send_keys('Larry')
        Keys.RETURN
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999'
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    # @unittest.skip
    def test_input_username_only(self):
        element = self.driver.find_element(By.NAME, 'username')
        element.send_keys('Larry')
        Keys.RETURN
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999'
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    # @unittest.skip
    def test_input_password_only(self):
        element = self.driver.find_element(By.NAME, 'password')
        element.send_keys('Larry')
        Keys.RETURN
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999'
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    # @unittest.skip
    def test_input_name_and_username(self):
        element = self.driver.find_element(By.NAME, 'name')
        element.send_keys('Larry')
        element = self.driver.find_element(By.NAME, 'username')
        element.send_keys('Larry')
        Keys.RETURN
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999'
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    # @unittest.skip
    def test_input_username_and_password(self):
        element = self.driver.find_element(By.NAME, 'username')
        element.send_keys('Larry')
        element = self.driver.find_element(By.NAME, 'password')
        element.send_keys('Larry')
        Keys.RETURN
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999'
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    # @unittest.skip
    def test_input_name_and_password(self):
        element = self.driver.find_element(By.NAME, 'name')
        element.send_keys('Larry')
        element = self.driver.find_element(By.NAME, 'password')
        element.send_keys('Larry')
        Keys.RETURN
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999'
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    # @unittest.skip
    def test_do_not_have_account(self):
        element = self.driver.find_element(By.NAME, 'name')
        element.send_keys("Larry")
        element = self.driver.find_element(By.NAME, 'username')
        element.send_keys("Larry")
        element = self.driver.find_element(By.NAME, 'password')
        element.send_keys("Larry")
        Keys.RETURN
        actual = self.driver.current_url
        expected = 'http://127.0.0.1:4999'
        self.assertEqual(actual, expected)

    # @unittest.expectedFailure
    def test_do_not_have_account(self):
        element = self.driver.find_element(By.NAME, 'name')
        element.send_keys("Larry")
        element = self.driver.find_element(By.NAME, 'username')
        element.send_keys("larry")
        element = self.driver.find_element(By.NAME, 'password')
        element.send_keys("larry")
        self.driver.find_element(By.CLASS_NAME, 'submit').click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.url_changes('http://127.0.0.1:4999/login'))
        actual = self.driver.current_url
        expected = 'http://localhost:4999/'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()