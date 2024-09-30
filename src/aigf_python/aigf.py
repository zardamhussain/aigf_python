from daily import *
import requests
from .daily_call import DailyCall
import os
import json

def create_web_call(api_url):
    url = f"{api_url}/new-meeting"
    headers = { 'Content-Type': 'application/json' }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code == 200:
            web_call_url = data.get('roomUrl')
            return web_call_url
        else:
            raise Exception(f"Error: {data.get('message', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")


def get_weatherunion_data(api_key: str, locality_id: str):
    url = f"https://www.weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id={locality_id}"
    headers = { 'X-Zomato-Api-Key': api_key }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Weather data not found")

class AIGF:
    def __init__(self, api_url="http://20.193.145.188:8000"):
        self.api_url = api_url

    def start(
        self,
    ):
        web_call_url = create_web_call(
            self.api_url
        )

        if not web_call_url:
            raise Exception("Error: Unable to create call.")

        os.environ['WEB_CALL_URL'] = web_call_url
        os.environ['API_URL'] = self.api_url

        self.__client = DailyCall()
        self.__client.join(web_call_url)
    
    def start_with_weatherunion(
        self,
        api_key: str,
        locality_id: str
    ):
        
        data = json.dumps(get_weatherunion_data(api_key, locality_id)['locality_weather_data'])

        web_call_url = create_web_call(
            self.api_url
        )

        if not web_call_url:
            raise Exception("Error: Unable to create call.")

        os.environ['WEB_CALL_URL'] = web_call_url
        os.environ['API_URL'] = self.api_url
        os.environ['DATA'] = data
        
        self.__client = DailyCall()
        self.__client.join(web_call_url)

    def stop(self):
        self.__client.leave()
        self.__client = None

    def send(self, message):
        """
        Send a generic message to the assistant.

        :param message: A dictionary containing the message type and content.
        """
        if not self.__client:
            raise Exception("Call not started. Please start the call first.")

        # Check message format here instead of serialization
        if not isinstance(message, dict) or 'type' not in message:
            raise ValueError("Invalid message format.")

        try:
            self.__client.send_app_message(message)  # Send dictionary directly
        except Exception as e:
            print(f"Failed to send message: {e}")

    def add_message(self, role, content):
        """
        method to send text messages with specific parameters.
        """
        message = {
            'type': 'add-message',
            'message': {
                'role': role,
                'content': content
            }
        }
        self.send(message)
