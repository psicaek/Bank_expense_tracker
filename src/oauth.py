
import requests
import http.server
import socketserver
import threading
from urllib.parse import urlparse, parse_qs
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, REVOLUT,AUTH_URL_SANDBOX , ING
import time
auth_code = None


class CallbackHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        auth_code = query.get("code", [None])[0]

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>You can close this window now.</h1>")


def start_callback_server():
    with socketserver.TCPServer(("", 3000), CallbackHandler) as httpd:
        httpd.handle_request()



def get_url():
    print("Client ID:", CLIENT_ID)
    print("Client secret:", CLIENT_SECRET)
    oauth_url = (
        f"{AUTH_URL}?response_type=code"
        f"&client_id={CLIENT_ID}"
        "&scope=info%20accounts%20balance%20cards%20transactions%20direct_debits%20standing_orders%20offline_access"
        f"&redirect_uri={REDIRECT_URI}"
        "&providers=de-ob-all%20de-oauth-all"
        f"{ING}"
    )
    print("OAuth URL:", oauth_url)
    return oauth_url

def get_code(driver):
    global auth_code
    time.sleep(5)
    current_url = driver.current_url
    print("Current URL:", current_url)
    parsed_url = urlparse(current_url)
    auth_code = parse_qs(parsed_url.query).get("code", [None])[0]
    print("Code:", auth_code)
    driver.quit()
    return auth_code

def get_access():
    global auth_code

    thread = threading.Thread(target=start_callback_server, daemon=True)
    thread.start()


    print("Waiting for authorization code...")
    print(auth_code)
    while auth_code is None:
        time.sleep(5)
    print("code:", auth_code)

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": auth_code,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    print("Requesting access token...")
    token_url = f"{TOKEN_URL}?response_type=code"

    response = requests.post(token_url, json=payload, headers=headers)
    tokens = response.json()

    if "access_token" not in tokens:
        raise Exception(f"Token error: {tokens}")

    return tokens["access_token"]
