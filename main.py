from easy import *
from medium import *
from hard import *

BACKGROUND_COLOR = '#FDD2BF'
FOREGROUND_COLOR = '#262A53'
BUTTON_COLOR = '#262A53'
BUTTON_FOREGROUND = '#FFE3E3'


def easy_window():
    easy_obj = Easy()


def medium_window():
    med_obj = Medium()


def hard_window():
    hard_obj = Hard()


main_window = Tk()
main_window.title("TYPING SPEED TEST")
main_window.config(padx=100, pady=70, bg=BACKGROUND_COLOR)

title_label = Label(text="TYPING SPEED TEST", font=('Courier', 15, 'bold'), bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
title_label.grid(row=1, column=2, pady=7)

level_title = Label(text="Select your level to play: ", font=('Courier', 12, 'bold'), bg=BACKGROUND_COLOR
                    , fg=FOREGROUND_COLOR)
level_title.grid(row=2, column=2, pady=20)

easy_button = Button(text="Easy", font=('Courier', 10, 'bold'), command=easy_window, bg=BUTTON_COLOR
                     , fg=BUTTON_FOREGROUND)
easy_button.grid(row=3, column=1)

medium_button = Button(text="Medium", font=('Courier', 10, 'bold'), command=medium_window, bg=BUTTON_COLOR,
                       fg=BUTTON_FOREGROUND)
medium_button.grid(row=3, column=2)

hard_button = Button(text="Hard", font=('Courier', 10, 'bold'), command=hard_window, bg=BUTTON_COLOR,
                     fg=BUTTON_FOREGROUND)
hard_button.grid(row=3, column=3)

main_window.mainloop()
