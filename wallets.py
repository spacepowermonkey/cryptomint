import base58
import binascii
import ecdsa
import hashlib
import qrcode
import secrets
from coincurve import PublicKey
from sha3 import keccak_256



def make_eth_wallet():
    # Instructions from: https://www.arthurkoziel.com/generating-ethereum-addresses-in-python/
    priv_key = keccak_256(secrets.token_bytes(32)).digest()

    pub_key = PublicKey.from_valid_secret(priv_key).format(compressed=False)[1:]
    addr = keccak_256(pub_key).digest()[-20:]
    return (addr, priv_key)


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



def render_qr(data):
    qr_obj = qrcode.QRCode(version=1, box_size=10, border=2, error_correction=qrcode.ERROR_CORRECT_H)
    qr_obj.add_data(data)
    qr_obj.make()
    return qr_obj.make_image()



def main():
    addr, priv_key = make_btc_wallet()

    addr_qr = render_qr(addr)
    addr_qr.save("address.png")

    pk_qr = render_qr(priv_key)
    pk_qr.save("privkey.png")

    bank_qr = render_qr("www.spacepowermonkey.com")
    bank_qr.save("bankkey.png")
    return

if __name__ == '__main__':
    main()
