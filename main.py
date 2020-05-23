#!/usr/bin/python3

import os
import global_variables
import static
from encryption import generate_keys_pare


# Check keys exist
if (os.path.isfile(global_variables.private_key_file)
        and os.path.isfile(global_variables.public_key_file)):
    pass
elif (os.path.isfile(global_variables.encrypted_vault_file)
      and (not os.path.isfile(global_variables.private_key_file
                              or not os.path.isfile(global_variables.private_key_file)))):
    print('Error! Vault exist but public or private key not exist!')
else:
    generate_keys_pare()

# Check that command-line param exist
# If exist - go to the "automated.py" (there are we call functions from vault.py with arguments that we enter in command promt)
# If not - "go to the interactive.py" (there are we call functions from vault.py after program ask as neeaded functions, desired variable values, etc)
