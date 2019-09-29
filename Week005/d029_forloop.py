#Ageel  9/29/2019
#100 Days of Python 
#Day 29 - For Loop

songlist = ["FLO","EMPIRE OF THE SUN","DMC"]

for x in songlist:
    if x == songlist[1]:
        for y in songlist[1]:
            print(y)
        continue
    print(x)