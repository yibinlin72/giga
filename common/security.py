# -*- coding: utf-8 -*-
import base64
import sys


def encrypt(message):
    encrypted_message = base64.b64encode(message)
    return encrypted_message


def decrypt(encoded_encrypted_message):
    encrypted_message = base64.b64decode(encoded_encrypted_message)
    return encrypted_message


if __name__ == "__main__":
    encrypted = encrypt(sys.argv[1])
    print(encrypted)
    assert decrypt(encrypted) == sys.argv[1]
