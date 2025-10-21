from accounts import guest_login, login, register, logout
from Game import play_game


def main_menu() -> None:
    guest_login()  # Start as guest by default
    while True:
        print("\n--- Main Menu ---")
        print("1. Quick Game")
        print("2. Login")
        print("3. Register")
        print("4. Exit")

        choice = input("Select option: ")
        if choice == "1":
            play_game()
        elif choice == "2":
            login()
        elif choice == "3":
            register()
        elif choice == "4":
            logout()
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice!")
