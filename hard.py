from tkinter import *
from text import *
import random

MEDIUM_TIME_INTERVAL = 30
BACKGROUND_COLOR = '#CF455C'
FOREGROUND_COLOR = '#0A043C'
BUTTON_COLOR = '#971549'
BUTTON_FOREGROUND = '#FF9898'

hard_word = random.choice(hard)
hard_score = 0


class Hard:
    def start_game(self, count):
        self.timer_label.config(text=f"TIMER: {count}")
        self.start_button.config(state=DISABLED)
        self.message.destroy()
        if count > 0:
            self.top_window3.after(1000, self.start_game, count - 1)
        elif count == 0:
            self.last_score.config(text=f"Your score is {hard_score}")
            self.text_entry.config(state=DISABLED)

    def update_score(self, points):
        self.score_label.config(text=f"Score: {points}")

    def call_score(self, event):
        global hard_score
        if self.text_entry.get() == hard_word:
            hard_score += 1
            self.update_score(hard_score)
        self.text_entry.delete(0, 'end')
        self.show_text()

    def show_text(self):
        global hard_word
        hard_word = random.choice(hard)
        self.text_entry.focus()
        self.text_label.config(text=hard_word)

        self.top_window3.bind('<Return>', self.call_score)

    def start_timer(self):
        self.start_game(MEDIUM_TIME_INTERVAL)
        self.show_text()

    def exit_game(self):
        global hard_score
        hard_score = 0
        self.top_window3.destroy()

    def __init__(self):
        self.top_window3 = Toplevel()
        self.top_window3.title("LEVEL~HARD")
        self.top_window3.config(padx=100, pady=60, bg=BACKGROUND_COLOR)

        self.start_button = Button(self.top_window3, text="START", font=('Courier', 12, 'bold'),
                                   command=self.start_timer, bg=BUTTON_COLOR, fg=BUTTON_FOREGROUND)
        self.start_button.grid(row=1, column=2, pady=10)

        self.timer_label = Label(self.top_window3, text="", font=('Courier', 15, 'bold'), bg=BACKGROUND_COLOR,
                                 fg=FOREGROUND_COLOR)
        self.timer_label.grid(row=2, column=2, pady=5)

        self.text_label = Label(self.top_window3, text="", font=('Courier', 13), wraplength=400, bg=BACKGROUND_COLOR,
                                fg=FOREGROUND_COLOR)
        self.text_label.grid(row=3, column=2, pady=5)

        self.text_entry = Entry(self.top_window3, width=70)
        self.text_entry.grid(row=4, column=2, pady=5)

        self.score_label = Label(self.top_window3, text="", font=('Courier', 10, 'bold'), bg=BACKGROUND_COLOR,
                                 fg=FOREGROUND_COLOR)
        self.score_label.grid(row=5, column=2, pady=5)

        self.last_score = Label(self.top_window3, text="", font=('Courier', 13, 'bold'), bg=BACKGROUND_COLOR,
                                fg=FOREGROUND_COLOR)
        self.last_score.grid(row=6, column=2, pady=6)

        self.exit_button = Button(self.top_window3, text="EXIT", font=('Courier', 12, 'bold'), command=self.exit_game,
                                  bg=BUTTON_COLOR, fg=BUTTON_FOREGROUND)
        self.exit_button.grid(row=7, column=2, pady=15)

        self.message = Label(self.top_window3, text="Click the START button to start.Type in the word and hit Enter."
                                                    "You'll have 30 seconds", font=('Courier', 10, 'bold'),
                             wraplength=350, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR)
        self.message.grid(row=8, column=2)

        self.top_window3.mainloop()
