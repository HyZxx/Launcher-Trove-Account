import subprocess
import time
import pyautogui
import pyperclip
from accounts import trove_accounts

def click_on_image(image_path):
    while True:
        # Recherchez l'emplacement de l'image spécifique à l'écran
        location = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if location:
            # Cliquez sur l'emplacement de l'image trouvée
            pyautogui.click(location)
            break

def launch_trove_accounts(num_accounts):
    # Remplacez ces chemins par ceux vers le lanceur Glyph et Trove sur votre système
    glyph_path = "C:\\Program Files (x86)\\Glyph\\GlyphClient.exe"
    trove_path = "C:\\Program Files (x86)\\Glyph\\Games\\Trove\\Live\\Trove.exe"
    
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
        click_on_image("path/to/login_screen.png")  # Remplacez cela par le chemin de l'image de l'écran de connexion
        
        # Automatisation des clics et saisies clavier pour se connecter
        click_on_image("path/to/email_field.png")  # Remplacez cela par le chemin de l'image du champ d'e-mail
        pyautogui.hotkey("ctrl", "a")  # Sélectionner tout le texte actuel
        pyperclip.copy(username)  # Copier le nom d'utilisateur
        pyautogui.hotkey("ctrl", "v")  # Coller le nom d'utilisateur
        
        click_on_image("path/to/password_field.png")  # Remplacez cela par le chemin de l'image du champ de mot de passe
        pyautogui.hotkey("ctrl", "a")  # Sélectionner tout le texte actuel
        pyperclip.copy(password)  # Copier le mot de passe
        pyautogui.hotkey("ctrl", "v")  # Coller le mot de passe
        
        pyautogui.press("enter")  # Appuyer sur Entrée pour se connecter

        # Attendre un court instant pour que le jeu se lance (ajustez le délai si nécessaire)
        time.sleep(3)
        
        # Si le jeu ne s'est pas lancé après le délai, cliquer sur "Jouer" pour essayer de le lancer
        click_on_image("path/to/play_button.png")  # Remplacez cela par le chemin de l'image du bouton "Jouer"
        
        # Attendre un court instant pour que le jeu se lance (ajustez le délai si nécessaire)
        time.sleep(3)
        
        # Une fois le jeu lancé, cliquer sur l'écran de connexion 
        click_on_image("path/to/game_screen.png")  # Remplacez cela par le chemin de l'image de l'écran de jeu

if __name__ == "__main__":
    # Nombre de comptes à lancer (vous pouvez le modifier selon vos besoins)
    num_accounts_to_launch = 8
    
    launch_trove_accounts(num_accounts_to_launch)
