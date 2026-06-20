import requests

BASE_URL = "https://api.frankfurter.app"

def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict: #type hinting

    url = f"{BASE_URL}/latest"

    params = {
        "amount": amount,
        "from": from_currency,
        "to": to_currency
    }

    response = requests.get(url, params)
    response.raise_for_status() 

    return response.json()    