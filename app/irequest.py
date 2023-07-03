import requests
from typing import Dict, Union


class APIRequest:
    API_URL = 'https://api.midjourneyapi.io/v2/'

    def __init__(self, api_key: str, callback_uri: str = None):
        self.api_key = api_key
        self.callback_uri = callback_uri

    @staticmethod
    def send_request(endpoint: str, data: dict, headers: dict) -> Union[Dict, str]:
        url = APIRequest.API_URL + endpoint
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def describe_image(self, image_file: str) -> Dict:
        endpoint = 'describe'
        data = {
            'callbackURL': self.callback_uri,
            'image': image_file
        }
        headers = {'Authorization': self.api_key}
        return APIRequest.send_request(endpoint, data, headers)

    def get_result(self, task_id: str) -> Dict:
        endpoint = 'result'
        data = {'taskId': task_id}
        headers = {'Authorization': self.api_key,
                   'Content-Type': 'application/json'}
        return APIRequest.send_request(endpoint, data, headers)

    def upscale_image(self, task_id: str, position: int) -> Dict:
        endpoint = 'upscale'
        data = {'taskId': task_id, 'position': position}
        headers = {'Authorization': self.api_key,
                   'Content-Type': 'application/json'}
        return APIRequest.send_request(endpoint, data, headers)

    def imagine(self, prompt: str) -> Dict:
        endpoint = 'imagine'
        data = {'callback_uri': self.callback_uri, 'prompt': prompt}
        headers = {'Authorization': self.api_key}
        return APIRequest.send_request(endpoint, data, headers)
