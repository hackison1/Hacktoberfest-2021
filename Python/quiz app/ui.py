from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzGui:
    def __init__(self,quiz_brain:QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("quizz")
        self.window.config(bg = THEME_COLOR,padx = 20,pady = 20)
        self.scorelable = Label(text = "score =",bg = THEME_COLOR, font =("Courier", 18),fg = 'white' )
        self.scorelable.grid(row =0,column = 1)
        self.whitescreen = Canvas(bg ="white", height = 250, width = 300)
        self.questiontext = self.whitescreen.create_text(150,125,width = 280,text = "some question",fill =THEME_COLOR, font = ("Arial",18))
        self.whitescreen.grid(row = 1,column =0,columnspan = 2,pady = 50)
        self.rightImage = PhotoImage(file = "images/false.png")
        self.correctImage = PhotoImage(file = "images/true.png")
        self.rightbutton = Button(image = self.rightImage,border = 0,command =self.rightanswer)
        self.rightbutton.grid(row = 2, column = 0,padx = 40)
        self.correctbutton = Button(image = self.correctImage,border = 0,command =self.correctanswer )
        self.correctbutton.grid(row = 2, column = 1,padx = 40)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.scorelable.config(text = f"Score = {self.quiz.score}")
            self.whitescreen.itemconfig(self.questiontext,text = q_text)
        else :
            self.whitescreen.itemconfig(self.questiontext, text="You have completed the quiz")
            self.rightbutton.config(state ="disabled ")
            self.correctbutton.config(state = "disabled")


    def rightanswer(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def correctanswer(self):
        self.get_feedback(self.quiz.check_answer("False"))


    def get_feedback(self,isright):
        if isright:
            self.window.after(1000,self.greencolour)
        else:
            self.window.after(500,self.redcolour)

    def greencolour(self):
        self.whitescreen.configure(bg= "green")
        self.window.after(500,self.whitecolour)


    def redcolour(self):
        self.whitescreen.configure( bg="red")
        self.window.after(500,self.whitecolour)


    def whitecolour(self):
        self.whitescreen.configure( bg = "white")
        self.window.after(500, self.get_next_question)
