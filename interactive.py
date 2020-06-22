"""Block with interactive actions in command promt"""

import static
import vault

def start_list_site_accounts():
    """input site name"""
    site = ""
    """check site exist"""
    vault.list_site_accounts(site)


def start_add_new_site():
    """input site name"""
    site = ""
    vault.add_site(site)


def start_add_new_account():
    """input account"""
    account = ""
    vault.add_account(account)


def start_show_passwd_for_account():
    pass


def start_change_passwd_for_account():
    pass


def start_del_acc():
    pass


def start_del_site():
    pass


def general():
    print(static.MENU)

    """choose function"""

    chosed_function = {
        1: vault.list_sites(),
        2: start_list_site_accounts(),
        3: start_add_new_account(),
        4: start_add_new_site(),
        5: start_show_passwd_for_account(),
        6: start_change_passwd_for_account(),
        7: start_del_acc(),
        8: start_del_site()
    }
