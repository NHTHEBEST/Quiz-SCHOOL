# Author NHTHEBEST
# Porject Quiz
# Subject DTP

# Class for question 
class question:
    # init function
    def __init__(self, answer, text):
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
        a = 0
        q1 = random.randint(0,100) * level # first num
        q2 = random.randint(0,100) * level # sec num
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