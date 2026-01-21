import random

class GuessingGame:
    def __init__(self):
        self.secret_number = None
        self.attempts_left = 5
        self.points = 0
        self.total_points = 0
        self.game_started = False
        self.guesses = []
    
    def display_banner(self):
        print("\n" + "="*50)
        print("🎮 NUMBER GUESSING GAME 🎮")
        print("="*50)
        print("Guess a number between 1 and 50")
        print("You have 5 attempts to guess correctly!")
        print("="*50 + "\n")
    
    def start_game(self):
        self.secret_number = random.randint(1, 50)
        self.attempts_left = 5
        self.points = 0
        self.game_started = True
        self.guesses = []
        
        print("\n🎲 A secret number has been chosen!")
        print(f"📊 Attempts Left: {self.attempts_left}")
        print(f"💰 Current Points: {self.points}")
        print(f"🏆 Total Points: {self.total_points}\n")
    
    def make_guess(self):
        while self.game_started and self.attempts_left > 0:
            try:
                guess = int(input("Enter your guess (1-50): "))
            except ValueError:
                print("❌ Please enter a valid number!")
                continue
            
            if guess < 1 or guess > 50:
                print("❌ Number must be between 1 and 50!")
                continue
            
            self.guesses.append(guess)
            
            # Check the guess
            if guess == self.secret_number:
                self.points = self.attempts_left * 10
                self.total_points += self.points
                print(f"\n✅ CORRECT! The secret number was {self.secret_number}!")
                print(f"🎉 Points earned this round: {self.points}")
                print(f"🏆 Total Points: {self.total_points}\n")
                self.game_started = False
                return True
            
            # Provide hint
            self.attempts_left -= 1
            
            if guess < self.secret_number:
                difference = self.secret_number - guess
                if difference > 15:
                    hint = f"❌ '{guess}' - The number is too far ABOVE your guess!"
                else:
                    hint = f"❌ '{guess}' - The number is ABOVE your guess!"
            else:  # guess > self.secret_number
                difference = guess - self.secret_number
                if difference > 15:
                    hint = f"❌ '{guess}' - The number is too far BELOW your guess!"
                else:
                    hint = f"❌ '{guess}' - The number is BELOW your guess!"
            
            print(hint)
            
            if self.attempts_left == 0:
                self.points = 0
                print(f"\n💔 GAME OVER! The secret number was {self.secret_number}!")
                print(f"😢 You earned 0 points this round")
                print(f"🏆 Total Points: {self.total_points}\n")
                self.game_started = False
                return False
            else:
                print(f"📊 Attempts Left: {self.attempts_left}")
                print(f"💰 Current Points: {self.points}\n")
    
    def display_history(self):
        if self.guesses:
            print("\n📜 Your Guesses: " + ", ".join(map(str, self.guesses)))
    
    def play(self):
        self.display_banner()
        
        while True:
            print("\n" + "="*50)
            print(f"🏆 TOTAL POINTS: {self.total_points}")
            print("="*50)
            print("1. Start New Game")
            print("2. Exit")
            print("="*50)
            
            choice = input("Choose an option (1 or 2): ")
            
            if choice == "1":
                self.start_game()
                self.make_guess()
                self.display_history()
            elif choice == "2":
                print(f"\n🏆 Final Total Points: {self.total_points}")
                print("Thanks for playing! 👋\n")
                break
            else:
                print("❌ Invalid option! Please choose 1 or 2.")

if __name__ == "__main__":
    game = GuessingGame()
    game.play()
    