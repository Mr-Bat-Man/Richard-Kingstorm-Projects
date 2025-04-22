from tkinter import *
from tkinter import messagebox, ttk
import random
import time

class EnhancedNumberGuessingGame:
    def __init__(self):
        self.window = Tk()
        self.window.title("Number Guessing Game")
        self.window.geometry("650x550")
        self.window.configure(bg="#2c3e50")
        self.window.resizable(True, True)
        
        # Modern color scheme
        self.colors = {
            "background": "#2c3e50",
            "primary": "#3498db",
            "secondary": "#2ecc71",
            "danger": "#e74c3c",
            "warning": "#f39c12",
            "light": "#ecf0f1",
            "dark": "#34495e"
        }
        
        # Game variables
        self.numb_guess = 0
        self.guess_chance = 0
        self.lowest_numb = 0
        self.highest_numb = 0
        
        # Animation variables
        self.animation_running = False
        
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Configure grid layout
        for i in range(7):
            self.window.rowconfigure(i, weight=1)
        for i in range(2):
            self.window.columnconfigure(i, weight=1)
        
        # Title Label with gradient effect
        title_frame = Frame(self.window, bg=self.colors["background"])
        title_frame.grid(row=0, column=0, columnspan=2, pady=(20,10), sticky="nsew")
        
        self.title_label = Label(
            title_frame,
            text="Number Guessing Game",
            font=("Helvetica", 24, "bold"),
            fg=self.colors["light"],
            bg=self.colors["background"]
        )
        self.title_label.pack(pady=10)
        
        # Animated border for title
        self.animate_title_border(title_frame)

        # Number range selection
        input_frame = Frame(self.window, bg=self.colors["dark"], padx=10, pady=10, relief=RAISED, borderwidth=2)
        input_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        
        # Lowest number entry
        lowest_label = Label(
            input_frame,
            text="Lowest Number:",
            font=("Helvetica", 14),
            bg=self.colors["dark"],
            fg=self.colors["light"]
        )
        lowest_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.lowest_numb_entry = Entry(
            input_frame,
            font=("Helvetica", 14),
            justify="center",
            bg=self.colors["light"],
            relief=FLAT,
            highlightthickness=2,
            highlightbackground=self.colors["primary"],
            highlightcolor=self.colors["primary"]
        )
        self.lowest_numb_entry.grid(row=0, column=5, padx=5, pady=5, sticky="nsew")
        self.lowest_numb_entry.bind("<Return>", lambda e: self.start_game())
        self.lowest_numb_entry.bind("<Down>", lambda e: self.highest_numb_entry.focus_set())
        
        # Highest number entry
        highest_label = Label(
            input_frame,
            text="Highest Number:",
            font=("Helvetica", 14),
            bg=self.colors["dark"],
            fg=self.colors["light"]
        )
        highest_label.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.highest_numb_entry = Entry(
            input_frame,
            font=("Helvetica", 14),
            justify="center",
            bg=self.colors["light"],
            relief=FLAT,
            highlightthickness=2,
            highlightbackground=self.colors["primary"],
            highlightcolor=self.colors["primary"]
        )
        self.highest_numb_entry.grid(row=1, column=5, padx=5, pady=5, sticky="nsew")
        self.highest_numb_entry.bind("<Return>", lambda e: self.start_game())
        self.highest_numb_entry.bind("<Up>", lambda event: self.lowest_numb_entry.focus_set())
        
        # Start button with hover effect
        self.start_btn = Button(
            self.window,
            text="Start Game",
            command=self.start_game,
            font=("Helvetica", 16, "bold"),
            bg=self.colors["primary"],
            fg="white",
            activebackground=self.colors["secondary"],
            activeforeground="white",
            relief=FLAT,
            borderwidth=0,
            padx=20,
            pady=10
        )
        self.start_btn.grid(row=2, column=0, columnspan=2, pady=20, sticky="nsew")
        
        # Add hover effects
        self.start_btn.bind("<Enter>", lambda e: self.start_btn.config(bg=self.colors["secondary"]))
        self.start_btn.bind("<Leave>", lambda e: self.start_btn.config(bg=self.colors["primary"]))
        
        # Instructions label
        instructions = Label(
            self.window,
            text="Enter a number range and click Start Game",
            font=("Helvetica", 16, "italic", "bold"),
            fg=self.colors["light"],
            bg=self.colors["background"]
        )
        instructions.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

    def animate_title_border(self, frame):
        colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12"]
        def change_color(i=0):
            frame.config(highlightbackground=colors[i], highlightthickness=2)
            self.window.after(1000, change_color, (i+1)%len(colors))
        change_color()

    def start_game(self):
        try:
            self.lowest_numb = int(self.lowest_numb_entry.get())
            self.highest_numb = int(self.highest_numb_entry.get())

            if self.lowest_numb >= self.highest_numb:
                self.shake_window()
                messagebox.showerror("Error", "Highest number must be greater than lowest number")
                return

            self.numb_guess = random.randint(self.lowest_numb, self.highest_numb)
            self.guess_chance = 10
            self.create_guess_interface()

        except ValueError:
            self.shake_window()
            messagebox.showerror("Error", "Please enter valid numbers")

    def shake_window(self):
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        for _ in range(5):
            for dx, dy in [(10,0), (-10,0), (0,10), (0,-10)]:
                self.window.geometry(f"+{x+dx}+{y+dy}")
                self.window.update()
                time.sleep(0.05)
        self.window.geometry(f"+{x}+{y}")

    def create_guess_interface(self):
        # Clear previous widgets
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Game area frame
        game_frame = Frame(self.window, bg=self.colors["dark"], padx=20, pady=20)
        game_frame.grid(row=0, column=0, rowspan=6, columnspan=2, sticky="nsew")
        
        # Guess prompt
        guess_label = Label(
            game_frame,
            text=f"Guess between {self.lowest_numb} and {self.highest_numb}",
            font=("Helvetica", 16),
            bg=self.colors["dark"],
            fg=self.colors["light"]
        )
        guess_label.pack(pady=(0, 20))
        
        # Guess entry with animation
        self.guess_entry = Entry(
            game_frame,
            font=("Helvetica", 18),
            justify="center",
            bg=self.colors["light"],
            relief=FLAT,
            highlightthickness=2,
            highlightbackground=self.colors["primary"]
        )
        self.guess_entry.pack(fill=X, pady=10)
        self.guess_entry.bind("<Return>", lambda e: self.check_guess())
        self.guess_entry.focus_set()
        
        # Submit button
        submit_btn = Button(
            game_frame,
            text="Submit Guess",
            command=self.check_guess,
            font=("Helvetica", 14, "bold"),
            bg=self.colors["primary"],
            fg="white",
            activebackground=self.colors["secondary"],
            activeforeground="white",
            relief=FLAT,
            padx=20,
            pady=8
        )
        submit_btn.pack(pady=10)
        
        # Feedback label with typing animation
        self.feedback_label = Label(
            game_frame,
            text="",
            font=("Helvetica", 14),
            bg=self.colors["dark"],
            fg=self.colors["light"],
            wraplength=400
        )
        self.feedback_label.pack(pady=10)
        
        # Progress bar with style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("custom.Horizontal.TProgressbar",
                       thickness=20,
                       troughcolor=self.colors["background"],
                       background=self.colors["primary"],
                       lightcolor=self.colors["secondary"],
                       darkcolor=self.colors["primary"])
        
        self.progress = ttk.Progressbar(
            game_frame,
            style="custom.Horizontal.TProgressbar",
            maximum=10,
            value=self.guess_chance,
            length=400
        )
        self.progress.pack(pady=10)
        
        # Chances label
        self.chances_label = Label(
            game_frame,
            text=f"Chances left: {self.guess_chance}",
            font=("Helvetica", 14),
            bg=self.colors["dark"],
            fg=self.colors["light"]
        )
        self.chances_label.pack(pady=5)
        
        # Reset button
        reset_btn = Button(
            game_frame,
            text="New Game",
            command=self.reset_game,
            font=("Helvetica", 12),
            bg=self.colors["danger"],
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            relief=FLAT,
            padx=15,
            pady=5
        )
        reset_btn.pack(pady=20)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.guess_chance -= 1
            self.progress["value"] = self.guess_chance
            self.chances_label.config(text=f"Chances left: {self.guess_chance}")
            
            if guess == self.numb_guess:
                self.celebrate()
                messagebox.showinfo("Congratulations!", f"You guessed it! The number was {self.numb_guess}")
                self.reset_game()
            elif self.guess_chance <= 0:
                self.shake_window()
                messagebox.showinfo("Game Over", f"Don't forget to do your study next time. The number was {self.numb_guess}")
                self.reset_game()
            elif guess < self.numb_guess:
                self.animate_feedback("You're too short! Jump Higher!!", self.colors["warning"])
            else:
                self.animate_feedback("Don't raise your head too high, dumbass!!", self.colors["warning"])
            
            self.guess_entry.delete(0, END)
            
        except ValueError:
            self.animate_feedback("Please enter a valid number", self.colors["danger"])

    def animate_feedback(self, text, color):
        if self.animation_running:
            return
            
        self.animation_running = True
        self.feedback_label.config(fg=color)
        
        # Typewriter effect
        for i in range(len(text)+1):
            self.feedback_label.config(text=text[:i])
            self.window.update()
            time.sleep(0.03)
        
        # Pulse animation
        for _ in range(2):
            for size in [14, 16, 14]:
                self.feedback_label.config(font=("Helvetica", size))
                self.window.update()
                time.sleep(0.1)
        
        self.animation_running = False

    def celebrate(self):
        colors = ["#f1c40f", "#2ecc71", "#e74c3c", "#3498db", "#9b59b6"]
        for _ in range(10):
            for color in colors:
                self.window.config(bg=color)
                self.window.update()
                time.sleep(0.05)
        self.window.config(bg=self.colors["background"])

    def reset_game(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.create_widgets()

if __name__ == "__main__":
    EnhancedNumberGuessingGame()
