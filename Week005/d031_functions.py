#Ageel  9/29/2019
#100 Days of Python 
#Day 31 - Functions



def reverseMe(string):
    
    index = len(string)
    revString = [None]*index
    index = index - 1
   
    for x in string:
        #print("adding "+x+" at index "+str(index))
        revString[index] = x
        index -= 1
    print(''.join(revString))



reverseMe("TEST")