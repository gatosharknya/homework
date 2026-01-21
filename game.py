import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game - Guess Number 1-50")
        self.root.geometry("500x600")
        self.root.config(bg="#f0f0f0")
        
        # Game variables
        self.secret_number = None
        self.attempts_left = 5
        self.points = 0
        self.game_started = False
        self.total_points = 0
        
        # Title
        title_label = tk.Label(root, text="🎮 Number Guessing Game 🎮", 
                               font=("Arial", 18, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        # Game Info Frame
        info_frame = tk.Frame(root, bg="white", relief="solid", borderwidth=1)
        info_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(info_frame, text="Guess a number between 1 and 50", 
                font=("Arial", 12), bg="white").pack(pady=5)
        
        # Attempts left
        self.attempts_label = tk.Label(info_frame, text="Attempts Left: 5", 
                                       font=("Arial", 11, "bold"), 
                                       fg="red", bg="white")
        self.attempts_label.pack(pady=5)
        
        # Hint Display
        self.hint_label = tk.Label(info_frame, text="Make your first guess!", 
                                   font=("Arial", 11), fg="blue", bg="white")
        self.hint_label.pack(pady=5)
        
        # Start Button
        self.start_button = tk.Button(root, text="START GAME", 
                                     command=self.start_game,
                                     font=("Arial", 12, "bold"),
                                     bg="#4CAF50", fg="white",
                                     width=20)
        self.start_button.pack(pady=10)
        
        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Your Guess:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        
        self.input_entry = tk.Entry(input_frame, font=("Arial", 11), width=15)
        self.input_entry.pack(side="left", padx=5)
        self.input_entry.bind("<Return>", lambda e: self.make_guess())
        
        self.guess_button = tk.Button(input_frame, text="GUESS", 
                                     command=self.make_guess,
                                     font=("Arial", 11, "bold"),
                                     bg="#2196F3", fg="white")
        self.guess_button.pack(side="left", padx=5)
        
        # History Frame
        history_label = tk.Label(root, text="Game History:", 
                                font=("Arial", 11, "bold"), bg="#f0f0f0")
        history_label.pack(pady=5)
        
        self.history_text = tk.Text(root, height=10, width=55, 
                                   font=("Courier", 10),
                                   bg="white", relief="solid", borderwidth=1)
        self.history_text.pack(padx=20, pady=5)
        self.history_text.config(state="disabled")
        
        # Points Frame
        points_frame = tk.Frame(root, bg="white", relief="solid", borderwidth=1)
        points_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(points_frame, text="Current Points: ", 
                font=("Arial", 11, "bold"), bg="white").pack(side="left", padx=10, pady=5)
        
        self.points_label = tk.Label(points_frame, text="0", 
                                     font=("Arial", 14, "bold"), 
                                     fg="green", bg="white")
        self.points_label.pack(side="left", padx=5, pady=5)
        
        tk.Label(points_frame, text="Total Points: ", 
                font=("Arial", 11, "bold"), bg="white").pack(side="left", padx=10, pady=5)
        
        self.total_points_label = tk.Label(points_frame, text="0", 
                                          font=("Arial", 14, "bold"), 
                                          fg="darkgreen", bg="white")
        self.total_points_label.pack(side="left", padx=5, pady=5)
        
        # Reset Button
        self.reset_button = tk.Button(root, text="NEW GAME", 
                                     command=self.start_game,
                                     font=("Arial", 11, "bold"),
                                     bg="#FF9800", fg="white")
        self.reset_button.pack(pady=10)
        
    def start_game(self):
        self.secret_number = random.randint(1, 50)
        self.attempts_left = 5
        self.points = 0
        self.game_started = True
        
        self.input_entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        
        self.update_display()
        self.add_to_history("🎮 GAME STARTED! Guess the secret number (1-50)")
        self.hint_label.config(text="Make your first guess!")
        
    def make_guess(self):
        if not self.game_started:
            messagebox.showwarning("Warning", "Please start the game first!")
            return
        
        try:
            guess = int(self.input_entry.strip())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return
        
        if guess < 1 or guess > 50:
            messagebox.showerror("Error", "Number must be between 1 and 50!")
            return
        
        self.input_entry.delete(0, tk.END)
        
        # Check the guess
        if guess == self.secret_number:
            self.points = self.attempts_left * 10  # Points based on attempts left
            self.total_points += self.points
            self.add_to_history(f"✅ CORRECT! The secret number was {self.secret_number}!")
            self.add_to_history(f"🎉 Points earned: {self.points}")
            self.hint_label.config(text=f"🎉 CORRECT! You earned {self.points} points!", fg="green")
            self.update_display()
            self.end_game(True)
            return
        
        self.attempts_left -= 1
        
        # Provide hint
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
        
        self.hint_label.config(text=hint, fg="orange")
        self.add_to_history(hint)
        
        if self.attempts_left == 0:
            self.add_to_history(f"💔 GAME OVER! The secret number was {self.secret_number}!")
            self.add_to_history(f"😢 You earned 0 points this round")
            self.hint_label.config(text=f"Game Over! The secret number was {self.secret_number}", fg="red")
            self.update_display()
            self.end_game(False)
        else:
            self.update_display()
    
    def end_game(self, won):
        self.game_started = False
        self.input_entry.config(state="disabled")
        self.guess_button.config(state="disabled")
        self.input_entry.config(state="disabled")
    
    def update_display(self):
        self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")
        self.points_label.config(text=str(self.points))
        self.total_points_label.config(text=str(self.total_points))
    
    def add_to_history(self, message):
        self.history_text.config(state="normal")
        self.history_text.insert(tk.END, message + "\n")
        self.history_text.see(tk.END)
        self.history_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()
    