import time

from selenium.webdriver.support.wait import WebDriverWait
from config import *
from browser_control import browser_control
from oauth import get_code,get_access
from oauth import get_url
from transactions import get_transactions
from accounts import get_accounts



def main():
    print("Connecting to TrueLayer Sandbox...")
    print("Creating driver...")

    browser = browser_control()
    url = get_url()
    driver = browser.create_driver(url)
    time.sleep(1)
    browser.click_element(page, ing_option, timeout= 1,value=None)
    time.sleep(1)
    browser.click_element(page, allow_button, timeout= 1,value=None)
    time.sleep(30)
    get_code(driver)
    access_token = get_access()
    print("\n[OK] Access token received\n")
    print("Fetching Accounts...")
    accounts,account_id = get_accounts(access_token)
    print(accounts)

    print("\nFetching Transactions...")
    transactions = get_transactions(access_token, account_id)
    print(transactions)
    print(transactions)


if __name__ == "__main__":
    main()
