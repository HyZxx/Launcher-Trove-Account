import subprocess
import time
import pyautogui
import pyperclip
import pygetwindow as gw
from accounts import trove_accounts

def launch_trove_accounts(num_accounts):
    # Remplacez ces chemins par ceux vers le lanceur Glyph et Trove sur votre système
    glyph_path = "C:\Program Files (x86)\Glyph\GlyphClient.exe"
    trove_path = "C:\Program Files (x86)\Glyph\Games\Trove\Live\Trove.exe"
    
    # Vérification que le nombre de comptes est correct
    num_accounts = min(num_accounts, len(trove_accounts))

    # Lancement de Glyph
    subprocess.Popen(glyph_path)
    time.sleep(15)  # Attendre que le lanceur Glyph s'ouvre
    
    for i in range(num_accounts):
        account = trove_accounts[i]
        username = account["username"]
        password = account["password"]
        
        # Clic pour accéder à l'écran de connexion
        pyautogui.click(x=1724, y=324)
        time.sleep(1)
        pyautogui.click(x=1729, y=376)

        # Automatisation des clics et saisies clavier pour se connecter
        pyautogui.click(x=1201, y=575)  # Clic sur le champ "Email"
        pyautogui.hotkey("ctrl", "a")  # Sélectionner tout le texte actuel
        pyperclip.copy(username)  # Copier le nom d'utilisateur
        pyautogui.hotkey("ctrl", "v")  # Coller le nom d'utilisateur
        pyautogui.press("tab")  # Passer au champ de mot de passe
        pyautogui.hotkey("ctrl", "a")  # Sélectionner tout le texte actuel
        pyperclip.copy(password)  # Copier le mot de passe
        pyautogui.hotkey("ctrl", "v")  # Coller le mot de passe
        pyautogui.press("enter")  # Appuyer sur Entrée pour se connecter

        # Attendre un court instant pour que le jeu se lance (ajustez le délai si nécessaire)
        time.sleep(3)
        
        # Si le jeu ne s'est pas lancé après le délai, cliquer sur "Jouer" pour essayer de le lancer
        pyautogui.click(x=1734, y=401)
        time.sleep(3)
        pyautogui.hotkey("alt", "tab")
        time.sleep(3)
        
        # Une fois le jeu lancé, cliquer sur l'écran de connexion 
        pyautogui.click(x=1724, y=324)
        time.sleep(1)
        pyautogui.click(x=1715, y=454)
        time.sleep(1)
        pyautogui.click(x=1653, y=449)

if __name__ == "__main__":
    
    num_accounts_to_launch = 8  # Updated

    launch_trove_accounts(num_accounts_to_launch)
