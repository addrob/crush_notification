import requests
from src import config

headers = {'Authorization': f'Key {config.DEVINO_API_KEY}'}


def send(to, message):
    messages = {
        "messages": [
            {
                "from": "ArtLife",
                "to": f"{to}",
                "text": f"{message}",
            }
        ]
    }

    requests.post(
        'https://api.devino.online/sms/messages',
        json=messages,
        headers=headers
    )
