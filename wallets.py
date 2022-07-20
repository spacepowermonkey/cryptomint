import base58
import binascii
import ecdsa
import hashlib
import secrets
from coincurve import PublicKey
from sha3 import keccak_256
from uuid import uuid4 as uuid



def make_eth_wallet():
    # Instructions from: https://www.arthurkoziel.com/generating-ethereum-addresses-in-python/
    priv_key = keccak_256(secrets.token_bytes(32)).digest()

    pub_key = PublicKey.from_valid_secret(priv_key).format(compressed=False)[1:]
    addr = keccak_256(pub_key).digest()[-20:]
    return (addr, priv_key)



class BitcoinWallet:
    CURRENCY_NAME = 'Bitcoin'
    LOGO_PATH = 'form/imgs/btc_logo.png'

    def __init__(self):
        self.name = str(uuid())

        address, secret = self.make_btc_wallet()
        self.address = address.decode('ascii')
        self.secret = secret.to_string().hex()
        return
    
    @staticmethod
    def make_btc_wallet():
        priv_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

        pub_key = '04' + priv_key.get_verifying_key().to_string().hex()
        pub_key_hash = hashlib.sha256(binascii.unhexlify(pub_key)).hexdigest()
        pub_key_net = '00' + hashlib.new('ripemd160', binascii.unhexlify(pub_key_hash)).hexdigest()

        pub_hash = pub_key_net
        for i in range(2):
            pub_hash = hashlib.sha256(binascii.unhexlify(pub_hash)).hexdigest()
        pub_key_with_checksum = pub_key_net + pub_hash[:8]

        addr = base58.b58encode(binascii.unhexlify(pub_key_with_checksum))
        return (addr, priv_key)



class DogecoinWallet:
    CURRENCY_NAME = 'Dogecoin'
    LOGO_PATH = 'form/imgs/doge_logo.png'

    def __init__(self):
        self.name = str(uuid())

        address, secret = self.make_doge_wallet()
        self.address = address.decode('ascii')
        self.secret = secret.to_string().hex()
        return
    
    @staticmethod
    def make_doge_wallet():
        priv_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

        pub_key = '04' + priv_key.get_verifying_key().to_string().hex()
        pub_key_hash = hashlib.sha256(binascii.unhexlify(pub_key)).hexdigest()
        pub_key_net = '1E' + hashlib.new('ripemd160', binascii.unhexlify(pub_key_hash)).hexdigest()

        pub_hash = pub_key_net
        for i in range(2):
            pub_hash = hashlib.sha256(binascii.unhexlify(pub_hash)).hexdigest()
        pub_key_with_checksum = pub_key_net + pub_hash[:8]

        addr = base58.b58encode(binascii.unhexlify(pub_key_with_checksum))
        return (addr, priv_key)



class EthereumWallet:
    CURRENCY_NAME = 'Ethereum'
    LOGO_PATH = 'form/imgs/eth_logo.png'

    def __init__(self):
        self.name = str(uuid())

        address, secret = self.make_eth_wallet()
        self.address = address.hex()
        self.secret = secret.hex()
        return
    
    @staticmethod
    def make_eth_wallet():
        # Instructions from: https://www.arthurkoziel.com/generating-ethereum-addresses-in-python/
        priv_key = keccak_256(secrets.token_bytes(32)).digest()

        pub_key = PublicKey.from_valid_secret(priv_key).format(compressed=False)[1:]
        addr = keccak_256(pub_key).digest()[-20:]
        return (addr, priv_key)



WALLET_TYPES = {
    'BTC' : BitcoinWallet,
    'DOGE' : DogecoinWallet,
    'ETH' : EthereumWallet
}

def wallet_from_symbol(symbol):
    return WALLET_TYPES[symbol]()
