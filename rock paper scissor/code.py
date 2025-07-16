import random
import os

SCORE_FILE = "scores.txt"

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def print_result(user, computer, winner):
    print(f"\n🧍 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")
    
    if winner == "tie":
        print("🟡 It's a tie!")
    elif winner == "user":
        print("✅ You win!")
    else:
        print("❌ Computer wins!")

def save_score(user_score, computer_score):
    with open(SCORE_FILE, "a") as f:
        f.write(f"You: {user_score} | Computer: {computer_score}\n")

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            print("\n📊 Past Scores:")
            print(f.read())
    else:
        print("\n❌ No past scores found.")

def main():
    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    while True:
        print("\n📜 MENU")
        print("1. Play Game")
        print("2. View Past Scores")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            user_score = 0
            computer_score = 0

            while True:
                user_choice = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()
                
                if user_choice == 'q':
                    print("🛑 Ending game...")
                    break
                elif user_choice not in ["rock", "paper", "scissors"]:
                    print("❗ Invalid choice. Try again.")
                    continue

                computer_choice = get_computer_choice()
                winner = determine_winner(user_choice, computer_choice)

                print_result(user_choice, computer_choice, winner)

                if winner == "user":
                    user_score += 1
                elif winner == "computer":
                    computer_score += 1

                print(f"📈 Score => You: {user_score} | Computer: {computer_score}")

            save_score(user_score, computer_score)

        elif choice == "2":
            load_scores()

        elif choice == "3":
            print("👋 Goodbye! Thanks for playing.")
            break

        else:
            print("⚠️ Invalid input. Please select from menu.")

if __name__ == "__main__":
    main()
