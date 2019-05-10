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


