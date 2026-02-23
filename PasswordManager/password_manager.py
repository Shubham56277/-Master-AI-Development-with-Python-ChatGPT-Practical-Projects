import os
import base64
import getpass

FILE_NAME = "passwords.txt"
MASTER_PASSWORD = "admin123"  # Change this to your own master password


# -----------------------------
# Encode / Decode Functions
# -----------------------------
def encrypt(text):
    return base64.b64encode(text.encode()).decode()


def decrypt(text):
    return base64.b64decode(text.encode()).decode()


# -----------------------------
# Add Password
# -----------------------------
def add_password():
    website = input("Website: ").strip().lower()
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{website}|{username}|{encrypt(password)}\n")

    print("✅ Password saved successfully!")


# -----------------------------
# View Password
# -----------------------------
def view_password():
    website = input("Enter website name: ").strip().lower()

    if not os.path.exists(FILE_NAME):
        print("❌ No saved passwords found.")
        return

    found = False

    with open(FILE_NAME, "r") as f:
        for line in f:
            try:
                w, u, p = line.strip().split("|")

                if w.strip().lower() == website:
                    print("\n🔎 Password Found:")
                    print(f"Website : {w}")
                    print(f"Username: {u}")
                    print(f"Password: {decrypt(p)}")
                    found = True
                    break
            except ValueError:
                continue

    if not found:
        print("❌ Website not found.")


# -----------------------------
# Master Login
# -----------------------------
def login():
    entered = getpass.getpass("Enter Master Password: ")
    return entered == MASTER_PASSWORD


# -----------------------------
# Main Menu
# -----------------------------
def main():
    print("🔐 Welcome to Password Manager")

    if not login():
        print("❌ Wrong Master Password")
        return

    while True:
        print("\n1. Add Password")
        print("2. View Password")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid option. Try again.")


if __name__ == "__main__":
    main()