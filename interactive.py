"""Block with interactive actions in command promt"""

import static
import global_variables
import vault
from Crypto.PublicKey import RSA
from getpass import getpass


def general():

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
