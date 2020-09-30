import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
print("bilal")

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/BILAL/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe")
        #chrome_options = Options()
        #chrome_options.add_experimental_option("detach", True)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        driver.implicitly_wait("6000")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()