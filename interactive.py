"""Block with interactive actions in command promt"""

import static
import global_variables
import vault
from os import system, name
from Crypto.PublicKey import RSA
from getpass import getpass


def general():

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux
        else:
            _ = system('clear')

    def exit_from_vault(private_key):
        del private_key
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
        clear()
        print(static.MENU)

        switcher = {
            1: vault.list_sites,
            2: vault.list_site_accounts,
            3: vault.add_account,
            4: vault.add_site,
            5: vault.show_passwd,
            6: vault.change_passwd,
            7: vault.del_account,
            8: vault.del_site,
            9: exit_from_vault
        }

        def start_swich_func(inputed_func):
            func = switcher.get(inputed_func, "error")
            try:
                func(my_private_key)
            except TypeError:
                print("Function that you enter does not exist. Try again.")
                return False
            else:
                return True

        def input_chosen_func():
            attempts_count = 1
            while attempts_count <= 3:
                try:
                    input_func = int(input("Choose needed function:  "))
                except KeyboardInterrupt:
                    print(static.KEYBOARD_INTERRUPT_MESSAGE)
                    exit()
                except ValueError:
                    print("Error! You enter not int argument. Try again")
                    attempts_count += 1
                else:
                    if start_swich_func(input_func):
                        break
                    else:
                        attempts_count += 1
                        continue
            else:
                print("You enter wrong argument 3 times. Exiting")
                exit()

        input_chosen_func()
