
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choise = choices
        self.answer = answer
        
    def checkAnswer(self,answer):
        return self.answer == answer
  
#Quiz class
class Quiz:
    def __init__(self, question):
      self.question = question
      self.score = 0
      self.questionIndex = 0
    
    def getQuestion(self):
        return self.question[self.questionIndex]
    
    def displayQurstion(self):
        questions = self.getQuestion()
        print(f'Soru : {self.questionIndex + 1} : {questions.text}')

        for q in questions.choise:
            print('-' + q)
            
        answer = input("cevap : ")
        self.quess(answer)
        self.loadQuestion()
        
    def quess(self,answer):
        questions = self.getQuestion()
        
        if questions.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        
        
    def loadQuestion(self):
        if len(self.question) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQurstion()

            
    def showScore(self):
        print("Score :" , self.score)
        
    def displayProgress(self):
        totalQuestion = len(self.question)
        questionsNumber= self.questionIndex + 1
        
        if questionsNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f'Question {questionsNumber} of {totalQuestion}'.center(100,'*'))
          
      
  
q1  = Question("En iyi programlama dili hangisidir ?", ['C#','java','python','javascript'], 'python');
q2  = Question("En popüler programlama dili hangisidir ?", ['java','C#','python','javascript'], 'python');
q3  = Question("En cok kazandiran programlama dili hangisidir ?", ['python','java','C#','javascript'], 'python');
q4  = Question("En sevilen programlama dili hangisidir ?", ['python','java','C#','javascript'], 'python');
q5  = Question("En kolay programlama dili hangisidir ?", ['python','java','C#','javascript'], 'python');


questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

quiz.loadQuestion()








