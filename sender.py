import requests

def send_notification_via_IFTTT(event, value1, value2, value3):
    IFTTT_KEY = "b6QW8twUdtbV-ZpYbSsrIc"
    payload = { "value1" : value1, "value2" : value2, "value3" : value3 }
    headers = { "Content-Type": "application/json" }

    resp = requests.post(f"https://maker.ifttt.com/trigger/{event}/with/key/{IFTTT_KEY}", json=payload, headers=headers)

    if resp.status_code != 200:
        raise ValueError("Unable to send notification")
    #else:
        #print("Notification sent successfully!")

def send(x):
    send_notification_via_IFTTT("send_notification", x, "", "")
