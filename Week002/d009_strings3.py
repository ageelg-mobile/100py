#Ageel  8/30/2019
#100 Days of Python 
#Day 9 - Strings Format

x , y , z = "Xbox One" , "Xbox 360" , "Xbox Original"
message = "First Microsoft released the {2} then the {1} and finally the current {0}"
print(message.format(x,y,z))