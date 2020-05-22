import os.path
#############################################################################################################################

dir_path = os.path.dirname(os.path.abspath(__file__))
private_key_file = 'vault_private_key'
path_to_private_key_file = dir_path + '/' + private_key_file
public_key_file = 'vault_public_key'
path_to_public_key_file = dir_path + '/' + public_key_file
encrypted_vault = 'vault.enc'
path_to_encrypted_vault = dir_path + '/' + encrypted_vault