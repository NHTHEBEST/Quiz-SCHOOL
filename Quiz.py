# Author NHTHEBEST
# Project Quiz
# Subject DTP
import random, time, winsound, os
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
    q1 = random.randint(1,10) * level # first num
    q2 = random.randint(1,10) * level # sec 
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
        # make div work
        q1 = q1 * q2
        q = "%d / %d = "%(q1,q2)
        a = int(q1/q2)
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
    # level
    leval = getnum("Level :\n")
    
    for x in range(0,numqs):# the main loop
        q = Genarate(leval)
        cor = ask(q)
        if cor:
            score += 1
        else:
            wrong.append(q)
    winsound.PlaySound("End.wav", winsound.SND_ASYNC)
    print("Score :", score)
    print("Wrong :")
    for x in wrong:
        print(x.text, x.answer)
    time.sleep(27)


winsound.PlaySound("back.wav", winsound.SND_ASYNC)
os.system("color da")
if __name__ == "__main__":
    quiz()


