"""Block with interactive actions in command promt"""

import static
import global_variables
import vault
from Crypto.PublicKey import RSA
from getpass import getpass


def general():
    """choose function"""

    def start_list_site_accounts():
        """input site name"""
        # site = ""
        """check site exist"""
        # vault.list_site_accounts(site)
        print("List site's accounts")

    def start_add_new_site():
        """input site name"""
        # site = ""
        # vault.add_site(site)
        print("adding site")

    def start_add_new_account():
        """input account"""
        # account = ""
        # vault.add_account(account)
        print("Adding account")

    def start_show_passwd_for_account():
        print("show passwd")

    def start_change_passwd_for_account():
        print("change passwd")

    def start_del_acc():
        print("dell acc")

    def start_del_site():
        print("del site")

    def exit_from_vault():
        print("Bye bye!")
        exit()

    print(static.START_MESSAGE)

    print("Enter master password for encrypt vault:")
    attempts_count = 1
    while attempts_count <= 3:
        try:
            master_password = getpass('')
            used_private_key_file = open(global_variables.private_key_file, 'r')
            my_private_key = RSA.import_key(used_private_key_file.read(), master_password)
            used_private_key_file.close()
        except KeyboardInterrupt:
            print(static.KEYBOARD_INTERRUPT_MESSAGE)
            exit()
        except ValueError:
            print("Password incorrect, try again")
            attempts_count += 1
        else:
            break
    else:
        print("You enter wrong password 3 times. Exiting")
        exit()

    while True:
        print(static.MENU)

        switcher = {
            1: vault.list_sites,
            2: start_list_site_accounts,
            3: start_add_new_account,
            4: start_add_new_site,
            5: start_show_passwd_for_account,
            6: start_change_passwd_for_account,
            7: start_del_acc,
            8: start_del_site,
            9: exit_from_vault
        }

        def start_swich_func(inputed_func):
            func = switcher.get(inputed_func, "error")
            func()

        try:
            input_func = int(input("Choose needed function:  "))
        except KeyboardInterrupt:
            print(static.KEYBOARD_INTERRUPT_MESSAGE)
            exit()
        else:
            start_swich_func(input_func)


