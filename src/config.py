import os
from dotenv import load_dotenv


load_dotenv()


# Truelayer username-passwords
CLIENT_ID_SANDBOX = os.getenv("CLIENT_ID_SANDBOX")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
CLIENT_SECRET_SANDBOX = os.getenv("CLIENT_SECRET_SANDBOX")
REDIRECT_URI_SANDBOX = "http://localhost:3000/callback"
REDIRECT_URI="https://console.truelayer.com/redirect-page"

# Truelayer Apis
AUTH_URL_SANDBOX = "https://auth.truelayer-sandbox.com/"
TOKEN_URL_SANDBOX = "https://auth.truelayer-sandbox.com/connect/token"
DATA_URL_SANDBOX = "https://api.truelayer-sandbox.com/data/v1/me"
AUTH_URL = "https://auth.truelayer.com/"
TOKEN_URL = "https://auth.truelayer.com/connect/token"
LIST_ACCOUNTS_URL = "https://api.truelayer.com/data/v1/accounts"



# Truelayer specific setting regarding the Bank
REVOLUT= "%20de-ob-revolut"
ING = "%20de-xs2a-ing"


# Loacators
page="choose_Bank.json"
ing_option="bank_option_ing"
allow_button="click_allow"
ing_password="ing_password"
ing_username="ing_username"
login_button="login_button"


# Username and password for Users Bank

username=os.getenv("ING_USERNAME")
password=os.getenv("ING_PASSWORD")