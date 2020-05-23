import os.path

#############################################################################################################################

dir_path = os.path.dirname(os.path.abspath(__file__))
private_key_name = 'vault_private_key'
private_key_file = dir_path + '/' + private_key_name
public_key_name = 'vault_public_key'
public_key_file = dir_path + '/' + public_key_name
encrypted_vault_name = 'vault.enc'
encrypted_vault_file = dir_path + '/' + encrypted_vault_name
