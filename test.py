import requests
import os
from dotenv import load_dotenv

load_dotenv()

wyreToken = os.getenv("WYRE_TOKEN")

"""
Get list of wallets
Reference: https://docs.sendwyre.com/reference/listwalletspaginated
Limit field may be optional here
"""
def listWallets(limit):
    url = f"https://api.testwyre.com/v2/wallets?limit={limit}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {wyreToken}"
    }

    response = requests.get(url, headers=headers)

    print(response.text)

"""
Creating a wallet
Reference: https://docs.sendwyre.com/reference/createwallet

There is also an optional callback URL field but I don't how it works yet
Wallets are referenced by an ID provide by the response from Wyre
"""
def createWallet(type, name, notes):
    url = "https://api.testwyre.com/v2/wallets"

    payload = {
        "type": f"{type}",
        "name": f"{name}",
        "notes": f"{notes}"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {wyreToken}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

"""
Deleting a wallet
Reference: https://docs.sendwyre.com/reference/deletewallet
"""
def deleteWallet(wallet_id):

    url = f"https://api.testwyre.com/v2/wallet/{wallet_id}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {wyreToken}"
    }

    response = requests.delete(url, headers=headers)

    print(response.text)

def main():
    listWallets()

if __name__ == "__main__":
    main()