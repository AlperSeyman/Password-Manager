from cryptography.fernet import Fernet


# Execute only once.
def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)



def read_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

master_pwd = input("What is the master password? ")
key = read_key() + master_pwd.encode()
fer = Fernet(key)

def add():
    user_name = input("Username: ")
    pwd = input("Password: ")
    encrpted_pwd = fer.encrypt(pwd.encode())
    with open('password.txt', 'a') as file:
        file.write(f"{user_name} : {encrpted_pwd.decode()}\n")

def view():
    with open('password.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user_name, encrypted_password = data.split(" : ")
            password = fer.decrypt(encrypted_password.encode())
            print(f"Username: {user_name}\nPassword: {password.decode()}")
            print("*******************************")



while True:
    mode = input("Do you want to add a new password or view existing ones (add, view), press q to quit ? ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode")
        continue

