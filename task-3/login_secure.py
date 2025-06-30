import bcrypt
import time

users = {
    "nour": bcrypt.hashpw("nour123".encode(), bcrypt.gensalt()),
    "emma": bcrypt.hashpw("Sunshine456!".encode(), bcrypt.gensalt())
}

def login():
    attempts = 0
    while attempts < 3:
        username = input("👤 Enter your username: ").strip()
        password = input("🔑 Enter your password: ").strip()

        if username in users and bcrypt.checkpw(password.encode(), users[username]):
            print(f"💖 Welcome, {username}! Secure login successful.")
            return True
        else:
            print("❌ Incorrect credentials.")
            attempts += 1
            print(f"⏳ Remaining attempts: {3 - attempts}")
            time.sleep(1)

    print("🚫 Access denied. Too many failed attempts.")
    return False

if __name__ == "__main__":
    print("🔐 Secure Login Portal")
    login()
