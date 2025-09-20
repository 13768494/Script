import os
import struct
import argparse
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

MAGIC = b'SIMPLEENC'  # 8 bytes

RSA_PUBLIC_PEM = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiGW+V1CwAB7igFt/0klp
AHNEdc2ftjwSdKyYu3pE5GsG58s9t8q85ZjOuYdTF1IkZLWa2ydv4xZcAP+JQIWN
rCRIF6jAF1C62jcnz5h8aASTh/u4i+ubgrW4851HjaIlT8ZCol6P5qpfK75ms4aD
6JWuw9EW78Hb2r5SJ4BFZUeqmtNxdu1HTmw8WqZ2iymoane/3y+VY1qeyYJexZo1
B2eZctG09YHERrRcBIkiiiG/TY/4e3zE05acA5apU6my3+V29zHr7d2eI4NDsrL8
t72fwT27nj5cy7znEMeMP31aE7f8iNrJCsxXGRrI9tltE77tBZAxr1K2dRXjyvzf
UQIDAQAB
-----END PUBLIC KEY-----"""

RSA_PRIVATE_PEM = b"""-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCIZb5XULAAHuKA
W3/SSWkAc0R1zZ+2PBJ0rJi7ekTkawbnyz23yrzlmM65h1MXUiRktZrbJ2/jFlwA
/4lAhY2sJEgXqMAXULraNyfPmHxoBJOH+7iL65uCtbjznUeNoiVPxkKiXo/mql8r
vmazhoPola7D0RbvwdvavlIngEVlR6qa03F27UdObDxapnaLKahqd7/fL5VjWp7J
gl7FmjUHZ5ly0bT1gcRGtFwEiSKKIb9Nj/h7fMTTlpwDlqlTqbLf5Xb3Mevt3Z4j
g0Oysvy3vZ/BPbuePlzLvOcQx4w/fVoTt/yI2skKzFcZGsj22W0Tvu0FkDGvUrZ1
FePK/N9RAgMBAAECggEAMERM3IotlgVX4tM+QtR+h03C+qsGqw7L+yS+sY09htVG
7syxrPHd8aOm9+lm4nhLb6YCRC5K/kHB0gqbb80zCqkWJ+UsALQtQx5EhMZxs792
06akskLwV4tmBTNxiDHKYVYH63xqENbWcdzhbAMcd7hMTXgW1UY1Pk2eNeNC62ky
OHhVU4Ga4b7UuP7xG5l4DcCh6ZGI0H2mX4yF/DSRAT4kiVXpc10mmpV3WBSWvGei
xURGKgEP6NpqfUAAaaWRgu9LuB6RtRnuD0pj8i/S+lsFk4oBb+UCQu3hksC2dtIX
6RvhjZQ3loLYRXjTOCuYdAbdtB7DVAKIBwtx+w3LrwKBgQC8w9bjR6iXcysuG5OL
49qZwp/A5QtoRucZNMLu1Pz9Pxqpb9dF3oUK4LONXb4L3yMwKKu3k5wMsRUP2jdc
7VfBSkcXHzaXBXwzq0lUAHp8FeZidRsLbE/OD5PwYWrKlTztQcFno1oHVN6buX04
egtSFSR/NOrIwidljFgTQ4EKBwKBgQC4+t9IkmrIOcTn2zZIbOXJYYPlrLISfzlx
r/siHDikwFh8fPiamcJvhUCglOw0xo2wMzavO5dsphTp4Hq9CQGQndEfUDoN80CA
tE3WDu+TGmokEt3hPu+Tr7wNTS1PfkHJKSXV9UB/5BNxIsrJgdAoQYgliO9JKPo9
BFJPYOPV5wKBgG91T6gqAsFSbpeuDsQWCVirE7tJQyASZZh7j/KH7s31+d88O6d0
yafvn/WD+Zh27AcerK4byZOw6BfRKMmFF0D5g9qCQrCPu5OiuwyPr8MfB0bxkMOA
8+pfRmI0k2MFFdGd9v4j9R/JHBxlPSwg3BhehYtbCpr6EVsjsEnHnST3AoGAbbnK
lwbbNpgl+A6tfXqzN6iTj7rICnbTQV/NTSeGZhv+oSGUakiI8JQPiPGtx4R76agH
aRylLvq5bx4MUHO2LO2gbb2uIjZH7dCGV1KWxCCoE2vpl8I4ZNeaah18oinXpha1
bdxD/VjyO2sS9UL+kdKFixZWMoSPI4CbvqBPpcMCgYAbUPu6Zddb5mikZnAQlD7Q
2Xtn7liRs1Nn80gNBXo3ppk+aGz4bvALQKd344CYI7WysDM2bmSVJsJFk7NnzqAn
puvKs2z7qbEY9762XL0zs+bq8yLAAx1v4ADzYHVRL3SoD8Luguf4T+lWmSWIwTwk
WsolLVyveAjYkZUntQWpMw== 
-----END PRIVATE KEY-----"""

def load_rsa_public(pem_bytes):
    return RSA.import_key(pem_bytes)

def load_rsa_private(pem_bytes):
    return RSA.import_key(pem_bytes)

# ====== 加密 ======
def encrypt_file(filepath, rsa_pub_pem):
    with open(filepath, 'rb') as f:
        plaintext = f.read()
    session_key = get_random_bytes(32)
    nonce = get_random_bytes(12)
    cipher_aes = AES.new(session_key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)
    rsa_key = load_rsa_public(rsa_pub_pem)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    ek_len = len(enc_session_key)
    outpath = filepath + '.enc'
    with open(outpath, 'wb') as out:
        out.write(MAGIC)
        out.write(struct.pack('>H', ek_len))
        out.write(enc_session_key)
        out.write(nonce)
        out.write(tag)
        out.write(ciphertext)
    print(f"[+] Encrypted '{filepath}' -> '{outpath}'")
    os.remove(filepath)
    print(f"[+] Automatically deleted original file '{filepath}'")

# ====== 解密 ======
def decrypt_file(filepath, rsa_priv_pem):
    with open(filepath, 'rb') as f:
        magic = f.read(len(MAGIC))
        if magic != MAGIC:
            raise ValueError("Not a supported encrypted file")
        ek_len = struct.unpack('>H', f.read(2))[0]
        enc_session_key = f.read(ek_len)
        nonce = f.read(12)
        tag = f.read(16)
        ciphertext = f.read()
    rsa_key = load_rsa_private(rsa_priv_pem)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
    # 解密后文件名 = 去掉 .enc
    if filepath.endswith('.enc'):
        outpath = filepath[:-4]
    else:
        outpath = filepath
    with open(outpath, 'wb') as out:
        out.write(plaintext)
    print(f"[+] Decrypted '{filepath}' -> '{outpath}'")
    os.remove(filepath)
    print(f"[+] Automatically deleted encrypted file '{filepath}'")

def main():
    parser = argparse.ArgumentParser(description="RSA+AES 文件加密/解密")
    parser.add_argument('mode', choices=['enc', 'dec'])
    parser.add_argument('input')
    args = parser.parse_args()
    if args.mode == 'enc':
        encrypt_file(args.input, RSA_PUBLIC_PEM)
    else:
        decrypt_file(args.input, RSA_PRIVATE_PEM)

if __name__ == '__main__':
    main()
