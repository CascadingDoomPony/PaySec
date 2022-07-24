import test
import requests
from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder



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
# Required for creating account
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


# Issuing an asset. Inherently creates a trustline
# Assets are only created when they are first transacted
def issueAsset(issuing_asset, issuing_secret_key, distributing_secret_key):

    # Configure Stellar SDK to talk to the horizon instance hosted by Stellar.org
    # To use the live network, set the hostname to 'https://horizon.stellar.org'
    server = Server(horizon_url="https://horizon-testnet.stellar.org")
    # Use test network, if you need to use public network, please set it to `Network.PUBLIC_NETWORK_PASSPHRASE`
    network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE

    # Keys for accounts to issue and receive the new asset
    issuing_keypair = Keypair.from_secret(
        issuing_secret_key
    )
    issuing_public = issuing_keypair.public_key

    distributor_keypair = Keypair.from_secret(
        distributing_secret_key
    )
    distributor_public = distributor_keypair.public_key

    # Transactions require a valid sequence number that is specific to this account.
    # We can fetch the current sequence number for the source account from Horizon.
    distributor_account = server.load_account(distributor_public)

    # First, the receiving account must trust the asset
    trust_transaction = (
        TransactionBuilder(
            source_account=distributor_account,
            network_passphrase=network_passphrase,
            base_fee=100,
        )
        #  The `changeTrust` operation creates (or alters) a trustline
        #  The `limit` parameter below is optional
        .append_change_trust_op(asset=issuing_asset, limit="1000")
        .set_timeout(100)
        .build()
    )

    trust_transaction.sign(distributor_keypair)
    trust_transaction_resp = server.submit_transaction(trust_transaction)
    print(f"Change Trust Transaction Resp:\n{trust_transaction_resp}")

    issuing_account = server.load_account(issuing_public)
    # Second, the issuing account actually sends a payment using the asset.
    payment_transaction = (
        TransactionBuilder(
            source_account=issuing_account,
            network_passphrase=network_passphrase,
            base_fee=100,
        )
        .append_payment_op(
            destination=distributor_public,
            asset=issuing_asset,
            amount="1",
        )
        .build()
    )
    payment_transaction.sign(issuing_keypair)
    payment_transaction_resp = server.submit_transaction(payment_transaction)
    print(f"Payment Transaction Resp:\n{payment_transaction_resp}")

keypair = generateKeypair()
print(keypair.public_key)
print(friendbotAccount(keypair).json)