#Ageel  10/05/2019
#100 Days of Python 
#Day 36 - Lambda2


def format(prefix,word):
    return lambda prefix,word: prefix+"-"+word

perfixer = format(word="motive",prefix="auto")
print(perfixer(word="a",prefix="b"))




