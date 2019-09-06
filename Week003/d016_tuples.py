#Ageel  9/6/2019
#100 Days of Python 
#Day 16 - Tuples

popGamesTuple = ("Fortnite","Apex Legends","Mario Maker 2")
print(popGamesTuple)

emptyTuple = ()
singletonTuple = (3,)

print(" Empty "+str(emptyTuple))
print(" One record "+str(singletonTuple))

print("back to the games , I sometimes play "+str(popGamesTuple[0]))

print("I want to also try this a new game but no time")
# Cant change items , give error
# popGamesTuple[0] = "WoW classic"  

print("I am stuck with")

for x in popGamesTuple:
    print(x)

del popGamesTuple

# gives error , tuple was destored and dosnt exist anymore
# print("Forget about them , I rather do somthing else , "+ str(len(popGamesTuple))+ " games to play")

gamesIhaveTuple = ("Fortnite","Call of Duty","Tekken 6","Street Fighter 3")

print("There is always time for "+str(gamesIhaveTuple[2:4]))
