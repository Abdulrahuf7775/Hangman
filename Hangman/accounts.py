import json
import pathlib
from password import generate_password

SAVE_DIR = pathlib.Path("save")
SAVE_DIR.mkdir(exist_ok=True)

ACCOUNTS_FILE = SAVE_DIR / "accounts.json"
if not ACCOUNTS_FILE.exists():
    ACCOUNTS_FILE.write_text("[]")  # Start with an empty list of accounts

current_account = None


# === Helper functions for JSON storage ===
def load_accounts():
    with open(ACCOUNTS_FILE, "r") as f:
        return json.load(f)


def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=4)


#  Account System
def guest_login():
    global current_account
    name = input("Enter your name: ")
    current_account = {
        "name": name,
        "username": None,  # guest has no username
        "password": None,
        "wins": 0,
        "losses": 0,
        "plays": 0,
        "session_wins": 0,
        "session_losses": 0,
        "session_plays": 0
    }
    print(f"Welcome, {name}! You're playing as Guest.")


def register():
    # Register a new account
    accounts = load_accounts()
    username:str = input("Choose a username: ")

    # Check if the username already exists
    for acc in accounts:
        if acc["username"] == username:
            print("❌ Username already taken!")
            return

    # Ask if user wants auto-generated password
    response: str = input("Do you want me to generate a password for you? (y/n): ").lower()
    while True:
        if response.isalpha(): #Check if the value entered is a letter
            if response == "y":
                password: str = generate_password(12)  # generate 12-char password
                print(f"🔑 Your generated password is: {password}")
                break
            elif response == "n":
                password: str = input("Choose a password: ")
                break
            else:
                print("Invalid response! Please enter 'y' or 'n'")
        else:
            print("You entered a wrong input")
            return


    name = input("Enter your display name: ")

    new_account = {
        "name": name,
        "username": username,
        "password": password,
        "wins": 0,
        "losses": 0,
        "plays": 0,
        "session_wins": 0,
        "session_losses": 0,
        "session_plays": 0
    }

    accounts.append(new_account)
    save_accounts(accounts)
    print("✅ Registration successful!")


def login():
    global current_account
    accounts = load_accounts()
    username = input("Enter username: ")
    password = input("Enter password: ")

    for acc in accounts:
        if acc["username"] == username and acc["password"] == password:
            current_account = acc
            print(f"✅ Welcome back, {acc['name']}!")
            return
    print("❌ Invalid login credentials!")


def logout():
    global current_account
    if current_account and current_account["username"]:
        accounts = load_accounts()
        for acc in accounts:
            if acc["username"] == current_account["username"]:
                acc["wins"] += current_account["session_wins"]
                acc["losses"] += current_account["session_losses"]
                acc["plays"] += current_account["session_plays"]
                acc["session_wins"] = 0
                acc["session_losses"] = 0
                acc["session_plays"] = 0
        save_accounts(accounts)
        print("📦 Account saved!")

    current_account = None
    print("🔓 Logged out!")
