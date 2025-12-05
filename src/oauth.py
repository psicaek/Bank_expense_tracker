import requests
import webbrowser
import http.server
import socketserver
import threading
import urllib.parse
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL

auth_code = None


class CallbackHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/callback":
            auth_code = params.get("code", [None])[0]

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>You can close this tab.</h1>")


def start_callback_server():
    with socketserver.TCPServer(("", 5000), CallbackHandler) as httpd:
        httpd.handle_request()


def get_access_token():
    global auth_code

    thread = threading.Thread(target=start_callback_server, daemon=True)
    thread.start()

    oauth_url = (
        f"{AUTH_URL}?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=info%20accounts%20balance%20transactions"
        "&providers=sandbox"
    )

    webbrowser.open(oauth_url)

    while auth_code is None:
        pass

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": auth_code,
    }

    token_url = f"{AUTH_URL}/connect/token"
    response = requests.post(token_url, json=payload)
    tokens = response.json()

    if "access_token" not in tokens:
        raise Exception(f"Token error: {tokens}")

    return tokens["access_token"]
