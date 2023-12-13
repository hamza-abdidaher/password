import hashlib
import random
import string

def check_password_requirements(password):
    
    if (
        len(password) >= 8
        and any(char.isupper() for char in password)
        and any(char.islower() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in "!@#$%^&*" for char in password)
    ):
        return True
    else:
        return False

def generate_random_password():
    
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(characters) for _ in range(12))  
    return password

def get_valid_password():
    while True:
        user_choice = input("Voulez-vous choisir un mot de passe vous-même (1) ou générer un mot de passe aléatoire (2) ? ")

        if user_choice == "1":
            password = input("Choisissez un mot de passe : ")
        elif user_choice == "2":
            password = generate_random_password()
            print(f"Mot de passe généré : {password}")
        else:
            print("Choix invalide. Veuillez choisir 1 ou 2.")
            continue

        if check_password_requirements(password):
            return password
        else:
            print("Erreur : Le mot de passe ne respecte pas les exigences de sécurité.")
            print("Veuillez choisir un nouveau mot de passe.")

def hash_password(password):
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

if __name__ == "__main__":
    
    user_password = get_valid_password()

    
    hashed_password = hash_password(user_password)


    print(f"Mot de passe crypté (SHA-256) : {hashed_password}")
