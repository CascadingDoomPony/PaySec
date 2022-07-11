import requests
import os
from dotenv import load_dotenv

load_dotenv()

wyreToken = os.getenv("WYRE_TOKEN")

"""
Get list of wallets
"""
def listWallets():
    limit = 20
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
"""
def createWallet():
    url = "https://api.testwyre.com/v2/wallets"

    payload = {
        "type": "DEFAULT",
        "name": "test",
        "notes": "test wallet"
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
def deleteWallet():

    wallet_id = "WA_8W28FR9FWHH"
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