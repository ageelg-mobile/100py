#Ageel  9/14/2019
#100 Days of Python 
#Day 25-26 Quiz

#Question 1

easyset = {1,3,5,7,8}
toadd = {4,8,12}
easyset = easyset.union(toadd)

print("Adding the two sets gets you "+str(easyset))
easyset.remove(8)
print("Removing 8 gets you "+str(easyset))
easyset.clear()
print("The set is now empty "+str(easyset))

#Question 2
bird = {
                "name" : "pigeon",
                "type" : "bird",
                "skin cover":"feathers"
}

fish = {
                "skin cover":"scales"
}

print("Pigeon is of type "+ bird.get("type"))
bird.update(fish)
print("Pigeon's skin is covered with "+ bird.get("skin cover"))
