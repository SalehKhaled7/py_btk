import random
class Question:
    def __init__(self , text ,choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer




class Quiz:
    def __init__(self,questions):
        random.shuffle(questions) #shuffle the list to get the question in a random order
        self.questions = questions
        self.questionscount = len(questions)
        self.points = 0

    

    def start(self):
        print("quiz started".center(50,"*"))
        x = 1
        for index, question in enumerate(self.questions):
            print(f"question {x} - {question.text}:")
            for choice in question.choices:
                print("-",choice)
            x += 1
            answer = self.getUserAnswer()

            if self.checkAnswer(index,answer):
                self.points += 1
                print(f"right answer !")
                print("your score:",self.score())
            else:
                print(f"wrong answer ")
                print("your score:",self.score())

            print("_"*10)
    def checkAnswer(self ,index ,answer):
        return self.questions[index].answer == answer
    
    def score(self):
        return f"{self.points}/{self.questionscount}"

    def getUserAnswer (self) -> str:
        while 1:
            answer = input("your answer : ").strip()
            if answer.isdigit():
                return answer
            else:
                print("please enter a valid answer !!")
    

q1 = Question("2+2",['1','2','3','4'],'4')
q2 = Question("77/2",['1','105','38','10'],'38')
q3 = Question("0*100",['0','2','100','4'],'0')
q4 = Question("3**2",['1','9','81','6'],'9')

questions = [q1,q2,q3,q4]


quiz = Quiz(questions)
quiz.start()

