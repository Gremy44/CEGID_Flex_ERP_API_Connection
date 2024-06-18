import requests

def get_oauth_token(username, password, scope, client_id, client_secret, auth_url):
    headers = {
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'scope': scope,
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(auth_url, headers=headers, data=payload)
    response_data = response.json()
    token = response_data.get("access_token")
    return token
