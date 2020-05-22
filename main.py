#!/usr/bin/python3

import os
import global_variables
import static
from encryption import generate_keys_pare
#############################################################################################################################

#Check keys exist
if os.path.isfile(global_variables.path_to_private_key_file) and os.path.isfile(global_variables.path_to_public_key_file) and os.path.isfile(global_variables.path_to_encrypted_vault):
    pass
else: 
    print(static.NEW_VAULT)
    generate_keys_pare()  


