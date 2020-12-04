class Question:
    
    question = ""
    options = []
    answer = 0


class Parser:
        
    dir = ''
    questions = ''
        
    def __init__(self, direction):
        super().__init__()
	 	
        self.dir = direction
        self.questions = self.getQuestions()
	
	
    def getQuestions(self):
        questions = []
		
        f = open(self.dir, "r", encoding="utf8")
		
        text = ''
        for line in f:
            line = line[0:-1]
            
            if (line == '!|'):
                curQuestion = self.__parse(text)
                questions.append(curQuestion)
                text = ''
            else:
                text += line
		
        f.close()
        return questions
	
    def getNewQuestion(self):
        if (len(self.questions) != 0):
            return self.questions.pop()
        else:
            return ''
    	
    def __parse(self, text):
        curQuestion = Question()
        curQuestion.answer = ''
        curQuestion.options = []
        curQuestion.question = ''
        copyStart = 0
        copyEnd = 0
        
        copyStart = text.find('==') + 2
        copyEnd = text.find('!=')
        curQuestion.question = text[copyStart:copyEnd]
       
       
        copyStart = text.find('--', copyEnd) + 2
        copyEnd = text.find('!-', copyStart)
        curQuestion.options.append(text[copyStart:copyEnd])
        
        for i in range(3):
            copyStart = text.find('--', copyEnd) + 3
            copyEnd = text.find('!-', copyStart)
            curQuestion.options.append(text[copyStart:copyEnd])
		
        copyStart = text.find('**', copyEnd) + 2
        copyEnd = text.find('!*', copyStart)
        curQuestion.answer = text[copyStart:copyEnd]
        
        return curQuestion



import tkinter as tk
import tkinter.messagebox
import time


# region Setup
win = tk.Tk()
win.geometry(f"600x400")
win.title("Who wants to be a millionaire")
win.resizable(False, False)
#endregion

    
# region Variables
question = tk.StringVar()
options = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
answer = 0
parser = ''
#endregion

# region main functions
def chooseOption(event, option):
    global parser
    global answer

    if (int(option) == int(answer)):
        tk.messagebox.showinfo("Круто", "Правильный ответ")
        updateVariables(parser.getNewQuestion())
    else:
        tk.messagebox.showerror("Не круто", "Неправильный ответ, ты проиграл :/")
        
        parser = Parser("questions.txt")
        updateVariables(parser.getNewQuestion())
# endregion

# region Additional Functions
def addButtonLambda(name, function, row, column, lambdaVar, stick="nswe"):
    button = tk.Button(win, textvariable=name)
    button.grid(row=row, column=column, stick=stick)
    button.bind("<Button-1>", lambda e, temp=lambdaVar: function(e, temp))
    
def updateVariables(newQuestion):
    global options
    global answer
    
    if(newQuestion != ''):  
        question.set(newQuestion.question)
        
        for i in range(4):
            options[i].set(newQuestion.options[i])
            
        answer = newQuestion.answer
    else:
        tk.messagebox.showinfo("ААААА", "Победа, супер круто!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        win.destroy()
# endregion

# region Main
parser = Parser("C:/Users/valer/Desktop/Programming/Python/Exam/millionaire/questions.txt")

updateVariables(parser.getNewQuestion())

tk.Label(win, textvariable=question).grid(row=0, column=0, columnspan=2, stick="nswe")

# Options
addButtonLambda(name=options[0], function=chooseOption, lambdaVar=0,  row=1, column=0)
addButtonLambda(name=options[1], function=chooseOption, lambdaVar=1, row=1, column=1)

addButtonLambda(name=options[2], function=chooseOption, lambdaVar=2, row=2, column=0)
addButtonLambda(name=options[3], function=chooseOption, lambdaVar=3, row=2, column=1)

# endregion

# region Footer
for i in range(2):
    win.grid_columnconfigure(i, minsize=600 / 2)
for i in range(3):
    win.grid_rowconfigure(i, minsize=400 / 3)

win.mainloop()
# endregion

