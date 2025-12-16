import time

from selenium.webdriver.support.wait import WebDriverWait
from config import page,allow_button,ing_option
from browser_control import browser_control
from oauth import get_access_token
from oauth import get_url
from transactions_sandbox import get_transactions
from accounts_sandbox import get_accounts




def main():
    print("Connecting to TrueLayer Sandbox...")
    print("Creating driver...")

    browser = browser_control()
    url = get_url()
    driver = browser.create_driver(url)
    time.sleep(2.5)
    browser.click_element(page, ing_option, timeout= 10,value=None)
    time.sleep(2.5)
    browser.click_element(page, allow_button, timeout= 10,value=None)
    time.sleep(2.5)
    access_token = get_access_token(driver)
    print("\n[OK] Access token received\n")

    print("Fetching Accounts...")
    accounts = get_accounts(access_token)
    print(accounts)

    print("\nFetching Transactions...")
    transactions = get_transactions(access_token)
    print(transactions)


if __name__ == "__main__":
    main()
