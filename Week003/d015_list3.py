#Ageel  9/6/2019
#100 Days of Python 
#Day 15 - List3

#old way to def a list
# moviesToWatch = ["John Wick 3","Pets 2","Shaw and Hobbs","Crawl"]

#new way to def a list
moviesToWatch = list(("John Wick 3","Pets 2","Shaw and Hobbs","Crawl"))

print("I have "+str(len(moviesToWatch))+" movies to watch "+str(moviesToWatch))
print("Ohh forgot about the new Joker movie and IT")
moviesToWatch.append("The Joker")
moviesToWatch.insert(0,"IT Ends")
print("Now I have "+str(len(moviesToWatch))+" movies to watch "+str(moviesToWatch))
print("But I dont have time for all of them , so better skip Pets 2")
moviesToWatch.remove("Pets 2") 
print("Now I have "+str(len(moviesToWatch))+" movies to watch "+str(moviesToWatch))
print("Watching them now")
print(".......")

watchedMovies = moviesToWatch.copy() # you can also use list() instead of copy()
moviesToWatch.clear()

print("Now I have "+str(len(moviesToWatch))+" movies to watch "+str(moviesToWatch))

print("Movies that I have just watched"+str(watchedMovies))

