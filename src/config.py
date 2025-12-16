import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID_SANDBOX = os.getenv("CLIENT_ID_SANDBOX")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI_SANDBOX = "http://localhost:3000/callback"
REDIRECT_URI="https://console.truelayer.com/redirect-page"


AUTH_URL_SANDBOX = "https://auth.truelayer-sandbox.com/"
TOKEN_URL_SANDBOX = "https://auth.truelayer-sandbox.com/connect/token"
DATA_URL_SANDBOX = "https://api.truelayer-sandbox.com/data/v1/me"

AUTH_URL = "https://auth.truelayer.com/"
TOKEN_URL = "https://auth.truelayer.com/connect/token"
DATA_URL = "https://api.truelayer.com/data/v1/me"


REVOLUT= "%20de-ob-revolut"
ING = "%20de-xs2a-ing"

page="choose_Bank.json"
ing_option="bank_option_ing"
allow_button="click_allow"