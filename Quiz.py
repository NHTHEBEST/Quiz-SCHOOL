# Author NHTHEBEST
# Porject Quiz
# Subject DTP
import random, time
# Class for question 
class question:
    # init function
    def __init__(self, text, answer):
        # set answer
        self.answer = answer
        # set question text
        self.text = text

    # when printing this class
    def __str__(self):
        return "Question : "+self.text+"\nAnswer : "+str(self.answer)


def Genarate(level): # genarate func
    ran = random.randint(1,4) # add sub mul div
    q = ""
    a = 1
    q1 = random.randint(1,100) * level # first num
    q2 = random.randint(1,100) * level # sec num
    if ran == 1: # add
        q = "%d + %d = "%(q1,q2) # text
        a = q1+q2 # awser
    elif ran == 2: # sub
        q = "%d - %d = "%(q1,q2)
        a = q1-q2
    elif ran == 3: # mul
        q = "%d x %d = "%(q1,q2)
        a = q1*q2
    else:          # div
        q = "%d / %d = "%(q1,q2)
        a = q1/q2
    return question(q, a) # new class 

# get number
def getnum(prompt):
    try: # try if not number
        return int(input(prompt))
    except:
        return getnum(prompt)

# asks the question
def ask(question):
    a = 0
    try:
        a = int(input(question.text))
    except:
        return ask(question)
    if a == question.answer:
        return True
    else:
        return False

# main quiz
def quiz():
    # all wrong answers
    wrong = []
    # the score
    score = 0
    # number of questions 
    numqs = getnum("Number of Questions :\n")
    # leval
    leval = getnum("Leval :\n")
    
    for x in range(0,numqs):# the main loop
        q = Genarate(leval)
        cor = ask(q)
        if cor:
            score += 1
        else:
            wrong.append(q)
    print("Score :", score)
    print("Wrong :")
    for x in wrong:
        print(x.text+"=", x.answer)



if __name__ == "__main__":
    quiz()

