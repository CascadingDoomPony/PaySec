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
Sample response:
{
  "pusherChannel": "45dda32c62df19963075eee5394583dc",
  "balances": {},
  "srn": "wallet:WA_WLDA6DTVCU9",
  "callbackUrl": null,
  "totalBalances": {},
  "availableBalances": {},
  "savingsReferralSRN": null,
  "depositAddresses": {
    "BTC": "miLgniFyYFD7viYWfMaYL9APoRbRvVR3cq",
    "MATIC": "0x43ded07ffb2c8b8d107c179671bc002be366d9ee",
    "AVAX": "X-fuji1sq38nqt95l635fs5an2x7wqvd2x6l3d6c3xcw2",
    "ETH": "0x0ea24c9cc9a3c55837d7bebdf25f21019fdd95c8",
    "XLM": "GD7WXI7AOAK2CIPZVBEFYLS2NQZI2J4WN4HFYQQ4A2OMFVWGWAL3IW7K:EGG6DG6XRZZ",
    "AVAXC": "0x33d1a326a082ee97aa76735d71aaa3fc0be0cbfe"
  },
  "notes": null,
  "name": "test",
  "id": "WA_WLDA6DTVCU9",
  "type": "DEFAULT",
  "status": null
}
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

"""
Creating a transaction
Reference:https://docs.sendwyre.com/reference/createtransfer
Check documentation for full list of fields and options
This transacts real currency; I haven't found a way to simulate making transactions
"""
def createTransaction():
    
    url = "https://api.testwyre.com/v3/transfers"

    payload = {
        "autoConfirm": True,
        "destCurrency": "USD",
        "sourceCurrency": "USD",
        "source": "account:AC_YNWFWXDW3AG",
        "destAmount": "200"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer TEST-SK-BNAG6XPU-V82BGUCQ-63TLCPXQ-D7MQ8C2V"
    }

response = requests.post(url, json=payload, headers=headers)

print(response.text)


def main():
    listWallets()

if __name__ == "__main__":
    main()