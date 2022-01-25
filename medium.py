from tkinter import *
from text import *
import random

MEDIUM_TIME_INTERVAL = 60
BACKGROUND_COLOR = '#A3DA8D'
FOREGROUND_COLOR = '#000B49'
BUTTON_COLOR = '#146356'
BUTTON_FOREGROUND = '#FFF1BD'

medium_word = random.choice(medium)
med_score = 0


class Medium:
    def start_game(self, count):
        self.timer_label.config(text=f"TIMER: {count}")
        self.start_button.config(state=DISABLED)
        self.message.destroy()
        if count > 0:
            self.top_window2.after(1000, self.start_game, count - 1)
        elif count == 0 and med_score > 10:
            self.last_score.config(text=f"Your score is {med_score}Great job!!")
            self.text_entry.config(state=DISABLED)
        elif count == 0 and 5 < med_score < 10:
            self.last_score.config(text=f"Your score is {med_score}.Good!")
            self.text_entry.config(state=DISABLED)
        elif count == 0 and 0 < med_score < 5:
            self.last_score.config(text=f"Your score is {med_score}.Average :)")
            self.text_entry.config(state=DISABLED)
        elif count == 0 and med_score == 0:
            self.last_score.config(text=f"Your score is {med_score}.Try again!")
            self.text_entry.config(state=DISABLED)

    def update_score(self, points):
        self.score_label.config(text=f"Score: {points}")

    def call_score(self, event):
        global med_score
        if self.text_entry.get() == medium_word:
            med_score += 1
            self.update_score(med_score)
        self.text_entry.delete(0, 'end')
        self.show_text()

    def show_text(self):
        global medium_word
        medium_word = random.choice(medium)
        self.text_entry.focus()
        self.text_label.config(text=medium_word)

        self.top_window2.bind('<Return>', self.call_score)

    def start_timer(self):
        self.start_game(MEDIUM_TIME_INTERVAL)
        self.show_text()

    def exit_game(self):
        global med_score
        med_score = 0
        self.top_window2.destroy()

    def __init__(self):
        self.top_window2 = Toplevel()
        self.top_window2.title("LEVEL~MEDIUM")
        self.top_window2.config(padx=100, pady=60, bg=BACKGROUND_COLOR)

        self.start_button = Button(self.top_window2, text="START", font=('Courier', 12, 'bold'),
                                   command=self.start_timer, bg=BUTTON_COLOR, fg=BUTTON_FOREGROUND)
        self.start_button.grid(row=1, column=2, pady=10)

        self.timer_label = Label(self.top_window2, text="", font=('Courier', 15, 'bold'), bg=BACKGROUND_COLOR,
                                 fg=FOREGROUND_COLOR)
        self.timer_label.grid(row=2, column=2, pady=5)

        self.text_label = Label(self.top_window2, text="", font=('Courier', 16), bg=BACKGROUND_COLOR, wraplength=300,
                                fg=FOREGROUND_COLOR)
        self.text_label.grid(row=3, column=2, pady=5)

        self.text_entry = Entry(self.top_window2, width=60)
        self.text_entry.grid(row=4, column=2, pady=5)

        self.score_label = Label(self.top_window2, text="", font=('Courier', 10, 'bold'), bg=BACKGROUND_COLOR,
                                 fg=FOREGROUND_COLOR)
        self.score_label.grid(row=5, column=2, pady=5)

        self.last_score = Label(self.top_window2, text="", font=('Courier', 13, 'bold'), bg=BACKGROUND_COLOR,
                                fg=FOREGROUND_COLOR)
        self.last_score.grid(row=6, column=2, pady=6)

        self.exit_button = Button(self.top_window2, text="EXIT", font=('Courier', 12, 'bold'), command=self.exit_game,
                                  bg=BUTTON_COLOR, fg=BUTTON_FOREGROUND)
        self.exit_button.grid(row=7, column=2, pady=15)

        self.message = Label(self.top_window2, text="Click the START button to start.Type in the word and hit Enter."
                                                    "You'll have 60 seconds", font=('Courier', 10, 'bold'),
                             wraplength=350, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR)
        self.message.grid(row=8, column=2)

        self.top_window2.mainloop()
