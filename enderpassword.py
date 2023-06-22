import string
import secrets

def generate_password(length):
    characters = string.ascii_letters * 2 + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Inserisci la lunghezza della password desiderata: "))
    print(f"La tua password generata è: {generate_password(password_length)}")
