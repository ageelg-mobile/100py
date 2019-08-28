#Ageel  8/28/2019
#100 Days of Python 
#Day 8 - Strings2


z = '''           Onions are greate for your health ! كلام جميل         '''

print(z.strip().lower() + "is " + str(len(z)) + " chars long".replace("chars","characters").upper() )
print(z.split("!"))
