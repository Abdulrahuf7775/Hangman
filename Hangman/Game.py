import random
from Hangman_stages import hangman_stages
import retrieve_word_fn
import accounts

def play_game() -> None:


    # The game gets to run from the decision of menu.py____#Quick play
    lives: int = 6 #live count for the game

    # importing the text file from retrieve_word_fn
    print("Fetching word...")
    word_length: int = random.randint(5, 12)
    chosen_word: str = retrieve_word_fn.retrieve_word(word_length).lower()


    # when the importing does not work or services is bad

    # word =['apple', 'Lemon', 'beauty', 'oranges']
    # chosen_word = random.choice(word)

    print('Word fetched ', chosen_word)
    display: list[str] = []
    for i in range(len(chosen_word)):
        display += '_'
    print(display)

    game_over: bool = False
    while not game_over: #keeps running till the lives over
        guessed_letter: str = input("Guess a Letter: ").lower()
        for position in range(len(chosen_word)):
            letter:str = chosen_word[position]
            if guessed_letter == letter:
                display[position] = guessed_letter
        print(display)  #display the correct matches
        if guessed_letter not in chosen_word:
            lives -= 1
            if lives == 0:
                game_over = True
                print("You lose!!")
                if accounts.current_account:
                    accounts.current_account["session_losses"] += 1
        if '_' not in display:
            game_over:bool = True
            print("You won")
            if accounts.current_account:
                accounts.current_account["session_wins"] += 1

        if accounts.current_account:
            accounts.current_account["session_plays"] += 1
        print(hangman_stages[len(hangman_stages) - 1 - lives])

# === Save account stats back to accounts.json ===
    if accounts.current_account:
        all_accounts = accounts.load_accounts()
        for acc in all_accounts:
            if acc["username"] == accounts.current_account["username"]:
                acc.update(accounts.current_account)  # update stats
                break
        accounts.save_accounts(all_accounts)
        print(f"Stats saved for {accounts.current_account['username']}")
