import test
import requests
from stellar_sdk import Asset
from stellar_sdk import Keypair


"""
Using Stellar SDK:
https://github.com/StellarCN/py-stellar-base
https://stellar-sdk.readthedocs.io/en/stable/install.html

Using Stellar to host assets, everything else (accounts, transactions, wallets) handled in wyre

Wyre doc: https://docs.sendwyre.com/reference/createtransfer

Tasks:
1. Figure out a way to get the invoice details from Wyre (assuming Wyre creates invoice and a way to record stakeholders' details)

2. Access public keys of the stakeholders and create a multisig transaction in Stellar

3. Release funds based on milestones

4. Dispute management

5. Finalization/ closure
"""
# Generate keypair (public and secret) https://stellar-sdk.readthedocs.io/en/stable/generate_keypair.html
# Required for interacting with Horizon node
# Can be generated from a given public or secret key, in this case we get a random one

def generateKeypair():
    keypair = Keypair.random()
    return keypair
    #print("Public Key: " + keypair.public_key)
    #print("Secret Seed: " + keypair.secret)

# Create account using Friendbot, only for use in the Stellar test network
# Live network account is more complex
def friendbotAccount(keypair):
    url = "https://friendbot.stellar.org"
    response = requests.get(url, params={"addr": keypair.public_key})
    return response




# Generate asset from Stellar SDK
def generateAsset(keypair):
    # Creates TEST asset issued by keypair.public_key
    test_asset = Asset("TEST", keypair.public_key)
    is_native = test_asset.is_native()  # False
    return test_asset

keypair = generateKeypair()
print(keypair.public_key)
print(friendbotAccount(keypair))