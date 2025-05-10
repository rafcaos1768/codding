import random

def dados():
    return random.randint(1,6)

if __name__ == "__main__":
    print("dado rolando...")
    numero = dados()
    print(f"você rolou o número: {numero}")
    