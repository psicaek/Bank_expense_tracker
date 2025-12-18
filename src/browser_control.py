
import time

from selenium.common import NoSuchElementException, TimeoutException

from locators.webinterface_json_locator import get_locator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class browser_control:


    def __init__(self):
            self.driver = None
            self.wait = None


    def create_driver(self,url, headless=False):
        """
        Initialize Selenium WebDriver and open the given OAuth URL.
        Returns the driver instance.
        """

        chrome_options = Options()

        if headless:
            chrome_options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(url)
        return self.driver




    def find_element(self, locator_type, locator_value, timeout = 5, value=None):

            by_type = {
                'id' : By.ID,
                'xpath' : By.XPATH,
                'name' : By.NAME,
                'class:' : By.CLASS_NAME,
                'css' : By.CSS_SELECTOR,
                'attribute:' : By.CSS_SELECTOR,
            }

            if locator_type == "attribute":
                locator_value = f'[data -test-id="{locator_value}"]'

            element = self.wait.until(EC.visibility_of_element_located((by_type[locator_type],locator_value)))
            #element = self.wait.until(EC.presence_of_element_located((by_type[locator_type], locator_value)))
            print("element found in the locator founder")
            return element

    def check_element(self, page, locator_name, timeout = 5, value=None):
        locator_type, locator_value = get_locator(locator_name, page, value=value)
        end_time = time.time() + timeout
        element = None

        while time.time() < end_time:
            try:
                element = self.find_element(locator_type, locator_value, timeout)
                if element and element.is_displayed():
                    print("element found")
            except TimeoutException:
                #Element not present
                print("element not found")
                pass
            time.sleep(0.5)

    def click_element(self, page, locator_name, timeout=5,  value=None):

        locator_type, locator_value = get_locator(locator_name, page, value=value)
        print(locator_type)
        print(locator_value)
        end_time = time.time() + timeout
        element = None

        while time.time() < end_time:
            element = self.find_element(locator_type, locator_value, timeout)
            if element and element.is_displayed():
                element.click()
                print("Element clicked")
                return
            time.sleep(0.5)

    def give_input_on_element(self, page, locator_name, input, timeout=10, value=None):

        locator_type, locator_value = get_locator(locator_name, page, value=value)
        print(locator_type)
        print(locator_value)
        end_time = time.time() + timeout
        element = None

        while time.time() < end_time:
            element = self.find_element(locator_type, locator_value, timeout)
            if element and element.is_displayed():
                element
                print("Element input was successfully sent")
                return
            time.sleep(0.5)



