import requests
import time
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

def fake_signal():
    return "📊 BINGX SİNYAL\n\nBTC/USDT\nYÖN: LONG\nGÜÇ: %72\n\n⚠️ Bu test sinyalidir."

while True:
    try:
        message = fake_signal()
        send_message(message)
        time.sleep(3600)  # 1 saatte 1 mesaj
    except Exception as e:
        print("Hata:", e)
        time.sleep(60)
