from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)  # Padding ditambahkan

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)  # Padding ditambahkan

        # Teks berada di tengah canvas
        self.question_text = self.canvas.create_text(
            150, 125,  # Posisi teks di tengah canvas
            text="Test",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280,  # Agar teks tidak keluar dari area
            anchor="center"  # Pastikan teks ditampilkan dengan titik tengah di posisi yang benar
        )

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_input)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)  # Padding ditambahkan

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_input)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)  # Padding ditambahkan

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_input(self):
        is_right = self.quiz.check_answer("True")  # Gunakan instance `self.quiz`
        self.give_feedback(is_right)

    def false_input(self):
        is_right = self.quiz.check_answer("False")  # Gunakan instance `self.quiz`
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
