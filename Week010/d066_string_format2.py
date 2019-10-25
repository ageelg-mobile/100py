#Ageel  10/25/2019
#100 Days of Python 
#Day 66 - String formating2

price = 49
txt = "The price for {1} meals is {0:0.2f} dollars, again thats the price for {1} meals"
print(txt.format(price,2))

Size = '12'
txt = "The shoe size is {shoe_size}"
print(txt.format(shoe_size=Size))