import requests

class XrpFlexConnection:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def execute_get_request(self, param):
        url = f"{self.base_url}/{param}"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers)
        return response.text

    def execute_put_request(self, req, param):
        url = f"{self.base_url}/{req}"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.put(url, headers=headers, data=param)
        return response.text
