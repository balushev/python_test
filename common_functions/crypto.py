# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:40:56 2021

@author: bbalushev
"""

from cryptography.fernet import Fernet


class Crypto:
    """ Crypto class provide methods for encryption and decryption """

    # ================================ Initialization method ================================
    def __init__(self, crypto_key: bytes = b'Rmgf_uSQ_XHsaxKsd-knFTjgzykRWojzc9sbmo5656w=') -> None:
        """ Constructor method

            Method parameters:
               crypto_key -> contains cryptography key bytes literal which will be used
                             for our encrypting and decrypting algorithm

            Return value -> None

        """

        self.fernet = Fernet(crypto_key)

    # ================================ Encryption method ================================
    def encrypt(self, text: str) -> bytes:
        """ encrypt method return encrypted text in byte format

            Method parameters:
                text -> text witch must be encrypted

            Return value -> encrypted text

        """

        return self.fernet.encrypt(text.encode())

    # ================================ Decryption method ================================
    def decrypt(self, encrypted_text: bytes) -> str:
        """ decrypt method return decrypted bytes

            Method parameters
                encrypted_text -> bytes witch must be decrypted

            Return value -> decrypted text
        """

        return self.fernet.decrypt(encrypted_text).decode()

    # ================================ Cryptography key generator ================================
    @staticmethod
    def generate_key() -> bytes:
        """ generate_key static method generates a crypto key

            Method parameters -> None

            Return value -> generated crypto key

        """

        return Fernet.generate_key()
