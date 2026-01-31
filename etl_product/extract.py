import requests
import os
from dotenv import load_dotenv

load_dotenv()

def extract_data():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

    payload = {
        "username": os.getenv("API_USERNAME"),
        "password": os.getenv("API_PASSWORD")
    }

    raw_data = requests.post(url, data=payload)

    json_data = raw_data.json()

    if json_data["error"] != 0:
        raise Exception("API Error")
    
    return json_data["data"]
    

extract_data()