from hangman import HangmanEngine
from words import choose_word
from io_utils import input_with_timeout

def run_game():
    print("===Welcome to my Hangman Game. Made for S225 PRT582 SOFTWARE ENGINEERING: PROCESS AND TOOLS Assessment ===")
    level = input("Choose level you wish to play (basic/intermediate): ").strip().lower()
    answer = choose_word(level)
    engine = HangmanEngine(answer, lives=6)

    while not (engine.state.is_won() or engine.state.is_lost()):
        print(f"\nWord: {engine.state.masked()}   Lives: {engine.state.lives}")
        got, value = input_with_timeout("\nGuess the letter : ", 15)

        if not got:
            engine.state.lives -= 1
            continue

        letter = value.strip().lower()
        try:
            correct = engine.guess(letter)
            if correct:
                print(f"✅ {letter} is in the word")
            else:
                print(f"❌ {letter} is not in the word.")
        except ValueError:
            print("Please enter a single letter.")

    if engine.state.is_won():
        print(f"🎉 You won! The answer was: {engine.state.answer}")
    else:
        print(f"💀 Game over! The answer was: {engine.state.answer}")

if __name__ == "__main__":
    run_game()
