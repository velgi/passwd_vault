import os.path
import global_variables
from getpass import getpass
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#############################################################################################################################

def generate_keys_pare():
    try:
        master_password = getpass("Enter new master password for new vault\n")
    except KeyboardInterrupt:
            print("Canceling from keyboard. Exiting")
            exit()
    else:
        pass

    key = RSA.generate(3072)
    public_key = key.publickey().exportKey('PEM')
    private_key = key.exportKey('PEM', master_password)
    new_file_public_key = open(global_variables.path_to_public_key_file, 'wb')
    new_file_public_key.write(public_key)
    new_file_public_key.close()

    new_file_private_key = open(global_variables.path_to_private_key_file, 'wb')
    new_file_private_key.write(private_key)
    new_file_private_key.close()


def decryption(data_for_decrypt):
    if os.path.isfile(global_variables.path_to_private_key_file):       
        print("Enter master password for encrypt vault:")
        attempts_count = 1
        while attempts_count <= 3:
            try:
                master_password = getpass('')
                used_file_private_key = open(global_variables.path_to_private_key_file, 'r')
                my_private_key = RSA.import_key(used_file_private_key.read(), master_password)
                used_file_private_key.close()
            except ValueError:
                print("Password incorrect, try again")
                attempts_count += 1
            else:
                break
        else:
            print("You enter wrong password 3 times. Exiting")
            exit()   
    else:
        print('Error! Private does not exists! Exiting.')
        exit()
    
    decryptor = PKCS1_OAEP.new(my_private_key)
    decrypted_data = str(decryptor.decrypt(data_for_decrypt).decode("utf-8"))
    print(decrypted_data)


def encryption(data_for_encrypt):
    if os.path.isfile(global_variables.path_to_public_key_file):
        used_file_public_key = open(global_variables.path_to_public_key_file, 'r')
        my_publickey = RSA.import_key(used_file_public_key.read())
        used_file_public_key.close()
        encryptor = PKCS1_OAEP.new(my_publickey)
        data_for_encrypt_bytes = bytes(data_for_encrypt, 'utf-8')
        encrypted_data = encryptor.encrypt(data_for_encrypt_bytes)
        print(encrypted_data)
    else:
        print('Error! Public key does not exist! Exiting.')
        exit()







