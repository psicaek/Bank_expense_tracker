import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:3000/callback"


AUTH_URL = "https://auth.truelayer-sandbox.com/"
TOKEN_URL = "https://auth.truelayer-sandbox.com/connect/token"
DATA_URL = "https://api.truelayer-sandbox.com/data/v1/me"