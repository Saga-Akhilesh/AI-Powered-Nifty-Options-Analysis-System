import requests
from config.api_keys import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_alert(message):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)