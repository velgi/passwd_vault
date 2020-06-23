"""Functions for generating keys pare, encrypt and decrypt data"""

import os.path
import global_variables
import static
from getpass import getpass
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_keys_pare():
    try:
        master_password = getpass("Enter new master password for new vault\n")
    except KeyboardInterrupt:
        print(static.KEYBOARD_INTERRUPT_MESSAGE)
        exit()
    else:
        pass

    print(static.NEW_KEYS)
    key = RSA.generate(3072)
    public_key = key.publickey().exportKey('PEM')
    private_key = key.exportKey('PEM', master_password)
    new_public_key_file = open(global_variables.public_key_file, 'wb')
    new_public_key_file.write(public_key)
    new_public_key_file.close()

    new_private_key_file = open(global_variables.private_key_file, 'wb')
    new_private_key_file.write(private_key)
    new_private_key_file.close()


def decryption(my_private_key, data_for_decrypt):
    decryptor = PKCS1_OAEP.new(my_private_key)
    decrypted_data = str(decryptor.decrypt(data_for_decrypt).decode("utf-8"))
    print(decrypted_data)


def encryption(data_for_encrypt):
    if os.path.isfile(global_variables.public_key_file):
        used_public_key_file = open(global_variables.public_key_file, 'r')
        my_publickey = RSA.import_key(used_public_key_file.read())
        used_public_key_file.close()
        encryptor = PKCS1_OAEP.new(my_publickey)
        data_for_encrypt_bytes = bytes(data_for_encrypt, 'utf-8')
        encrypted_data = encryptor.encrypt(data_for_encrypt_bytes)
        print(encrypted_data)
    else:
        print('Error! Public key does not exist! Exiting.')
        exit()
