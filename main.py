# main.py
from accounts import trove_accounts
import subprocess
from pystyle import *
import colorama
import pyautogui
import time
import schedule
import pygetwindow as gw

trove_accounts = trove_accounts

def launch_trove_launcher():
    subprocess.Popen(["python", "LauncherTroveAccount.py"])

def add_account():
    global trove_accounts
    username = input("Enter the user name:")
    password = input("Enter the password:")
    alias = input("Enter the alias:")

    # Nouveau compte au format de dictionnaire
    new_account = {"username": username, "password": password, "alias": alias}

    # Ajouter le nouveau compte à la liste trove_accounts dans la variable en mémoire
    trove_accounts.append(new_account)

    # Mettre à jour le fichier accounts.py avec la nouvelle liste trove_accounts
    with open("accounts.py", "w") as file:
        file.write("trove_accounts = [")
        for account in trove_accounts:
            file.write(f'\n    {account},')
        file.write("\n]")

    print("Account added")
    
def remove_account():
    global trove_accounts  # Déclarer trove_accounts comme global ici
    username_or_alias = input("Enter the username or alias of the account you wish to delete:")

    # Filtrer les comptes à supprimer
    removed_accounts = [account for account in trove_accounts if account["username"] == username_or_alias or account["alias"] == username_or_alias]
    
    # Mettre à jour la liste trove_accounts
    trove_accounts = [account for account in trove_accounts if account not in removed_accounts]
    
    # Mettre à jour le fichier accounts.py avec la nouvelle liste trove_accounts
    with open("accounts.py", "w") as file:
        file.write("trove_accounts = [")
        for account in trove_accounts:
            file.write(f'\n    {account},')
        file.write("\n]")
    
    # Afficher un message de confirmation pour chaque compte supprimé
    for account in removed_accounts:
        print(f"Account deleted: Username: {account['username']}, Alias: {account['alias']}")

def display_accounts():
    print()
    for account in trove_accounts:
        print(f"Username: {account['username']}, Alias: {account['alias']}")

def modify_num_accounts():
    global num_accounts_to_launch
    new_num_accounts = int(input("Enter the new number of accounts to launch: "))
    num_accounts_to_launch = new_num_accounts

    # Mettre à jour le fichier LauncherTroveAccount.py avec la nouvelle valeur num_accounts_to_launch
    file_path = "LauncherTroveAccount.py"  # Remplacez cela par le chemin correct
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for i, line in enumerate(lines):
            if i == 58:  # Modifier la ligne 59 (en commençant à partir de 0)
                file.write(f"    num_accounts_to_launch = {num_accounts_to_launch}  # Updated\n")
            else:
                file.write(line)


def anti_afk():
    global num_accounts_to_launch

    print("Anti AFK started...")

    while True:
        # Attendre 5 minutes
        time.sleep(30)  # 300 secondes équivalent à 5 minutes

        # Appuyer sur la touche Espace après chaque bascule de fenêtre
        switch_between_windows()

        print("Anti AFK completed")
def switch_between_windows():
    global num_accounts_to_launch

    print("Switching between windows...")

    # Obtenez toutes les fenêtres actives
    windows = gw.getAllTitles()

    # Sélectionnez les fenêtres en fonction de num_accounts_to_launch
    target_windows = windows[max(0, -num_accounts_to_launch):]

    # Rétablissez le focus sur chaque fenêtre
    for window in target_windows:
        try:
            windows_with_title = gw.getWindowsWithTitle(window)
            if windows_with_title:
               windows_with_title[0].activate()

            # Attendez quelques secondes entre chaque bascule
            time.sleep(2)

            # Appuyez sur la touche Espace
            pyautogui.press("space")
        except Exception as e:
           print(f"Error: {e}")

    print("Switching completed")

def move_account():
    global trove_accounts

    alias_to_move = input("Enter the alias of the account you want to move: ")
    new_position = int(input("Enter the new position for the account: "))

    # Recherche de l'index de l'alias spécifié dans la liste
    index_to_move = next((index for (index, account) in enumerate(trove_accounts) if account["alias"] == alias_to_move), None)

    if index_to_move is not None:
        # Supprimer l'élément de sa position actuelle
        moved_account = trove_accounts.pop(index_to_move)
        # Insérer l'élément à la nouvelle position
        trove_accounts.insert(new_position - 1, moved_account)

        # Mettre à jour le fichier accounts.py avec la nouvelle liste trove_accounts
        with open("accounts.py", "w") as file:
            file.write("trove_accounts = [")
            for account in trove_accounts:
                file.write(f'\n    {account},')
            file.write("\n]")

        print(f"Account '{alias_to_move}' moved to position {new_position}")
    else:
        print(f"Account with alias '{alias_to_move}' not found")


while True:
    banner1=('''
   _____                        _                             _   
  |_   _| __ _____   _____     / \   ___ ___ ___  _   _ _ __ | |_ 
    | || '__/ _ \ \ / / _ \   / _ \ / __/ __/ _ \| | | | '_ \| __|
    | || | | (_) \ V /  __/  / ___ \ (_| (_| (_) | |_| | | | | |_ 
    |_||_|  \___/ \_/ \___| /_/   \_\___\___\___/ \__,_|_| |_|\__|
                                                                 
                                                                                
    [1] Launch Account   [2] Compte launched     [3] View Account
    [4] Add Account      [5] Delete Account      [6] Move Account  
    [7] Anti AFK''')
    
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f'\n {banner1}')))
    
    choice = input(Colorate.Vertical(Colors.purple_to_blue,("\nChoose an option:")))

    if choice == "1":
        launch_trove_launcher()
    elif choice == "2":
        modify_num_accounts()
    elif choice == "3":
        display_accounts()
    elif choice == "4":
        add_account()
    elif choice == "5":
        remove_account()
    elif choice == "6":
        move_account()
    elif choice == "7":
        anti_afk()
    else:
        print("Please select an option")
