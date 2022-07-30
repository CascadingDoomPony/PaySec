'''
This is a Python 3.7 Module that Submits an Auth Token
and returns an API key for authentication
'''
import json
import secrets
import requests
import urllib.parse


class WyreApi:

    API_URL = "https://api.testwyre.com"
    API_VER2 = "/v2"
    API_SESSIONS_PATH = "/sessions/auth/key"

    def generate_token(self, tok_length=30):
        '''
            This method generates a secret token using secrets
            in Python3
        '''
        return secrets.token_hex(tok_length)

    def submitAuthToken(self, token):
        '''
            This method submits the secret key / token generated above
            and to https://api.sendwyre.com/v2/sessions/auth/key
            and sets API_KEY to the API key returned
        '''
        if not token:
            print("Please generate a 25-35 length token")
            return

        params = {
            "secretKey": token
        }
        url = WyreApi.API_URL + WyreApi.API_VER2 + WyreApi.API_SESSIONS_PATH + "?" + \
            urllib.parse.urlencode(params, encoding='utf-8')

        response = requests.post(url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(response.text)


if __name__ == "__main__":
    # create a wyre class object
    wyre = WyreApi()

    # generate a wyre token
    token = wyre.generate_token()
    print("Token", token)
    # get a secret key
    response = wyre.submitAuthToken(token)
    if response:
        print("API KEYS", response.get('apiKey'))