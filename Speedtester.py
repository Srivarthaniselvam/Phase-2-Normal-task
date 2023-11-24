from tkinter import *
import random
from timeit import default_timer
import difflib

print("-----------Project for My Python Typing Speed test------------")

class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title('Typing Speed Test')
        self.root.geometry("500x500")
        self.start_time = 0
        self.word = random.choice([
            'We are developing Python project',
            'This is Windows Os',
            'We are Hiring',
            'Lets Play a game',
            'Python is a programming language',
            'We love Coding',
            'This is an amazing Article',
            'I am an Intern',
            'Lets check the Output',
            'we are Compiling this program',
            'Python is a versatile and powerful programming language.',
            'Software development is the process of creating software through programming.',
            'In object-oriented programming, classes and objects are fundamental concepts.',
            'Debugging is twice as hard as writing the code in the first place.',
            'The best error message is the one that never shows up.',
            'Programming is thinking, not typing.',
            'Open-source software encourages collaboration and transparency.',
            'Algorithms + Data Structures = Programs.',
            'Coding is like solving puzzles, piece by piece.',
            'Git is a distributed version control system.'
        ])
        self.entered = StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.greet = Label(self.root, font=('Helvetica', 30, 'bold'), text="Welcome to My Typing Speed Test!")
        self.greet.grid(row=0, columnspan=3)

        self.label_word = Label(self.root, font=('Helvetica', 20, 'bold'), text=self.word)
        self.label_word.grid(row=3, columnspan=3)

        self.label_instruction = Label(self.root, font=('Georgia', 15), text="Type here :")
        self.label_instruction.grid(row=5, column=1, sticky='e')

        self.enter = Entry(self.root, textvariable=self.entered, font=('Georgia', 15), width=20)
        self.enter.grid(row=5, column=3)

        self.btn_check = Button(self.root, text="Check", command=self.check, bg="DodgerBlue2", fg="black", font=('arial', 10))
        self.btn_check.grid(row=6, columnspan=6)

    def play(self):
        self.label_instruction.config(text="Type here:")
        self.enter.delete(0, 'end')
        self.start_time = default_timer()
        self.word = random.choice([
            'We are developing Python project',
            'This is Windows Os',
            'We are Hiring',
            'Lets Play a game',
            'Python is a programming language',
            'We love Coding',
            'This is an amazing Article',
            'I am an Intern',
            'Lets check the Output',
            'we are Compiling this program',
            'Python is a versatile and powerful programming language.',
            'Software development is the process of creating software through programming.',
            'In object-oriented programming, classes and objects are fundamental concepts.',
            'Debugging is twice as hard as writing the code in the first place.',
            'The best error message is the one that never shows up.',
            'Programming is thinking, not typing.',
            'Open-source software encourages collaboration and transparency.',
            'Algorithms + Data Structures = Programs.',
            'Coding is like solving puzzles, piece by piece.',
            'Git is a distributed version control system.'
        ])
        self.label_word.config(text=self.word)

    def check(self):
        end_time = default_timer()
        time_taken = round(end_time - self.start_time, 2)

        typed_text = self.entered.get()
        accuracy = difflib.SequenceMatcher(None, self.word, typed_text).ratio() * 100
        speed = round(len(self.word.split()) * 70 / time_taken, 2)

        result_msg = f"Time: {time_taken} seconds\nAccuracy: {accuracy:.2f}%\nSpeed: {speed} wpm"

        self.label_result = Label(self.root, font=('arial', 15, 'bold'), text=result_msg)
        self.label_result.grid(row=7, columnspan=3)

if __name__ == "__main__":
    root = Tk()
    typing_test = TypingTest(root)

    btn_start = Button(root, text=" Start typing", command=typing_test.play, bg="DodgerBlue2", fg="white", font=('arial', 10))
    btn_start.grid(row=4, columnspan=6)
    start = default_timer()

    root.mainloop()
