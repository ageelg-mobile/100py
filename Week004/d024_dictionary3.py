#Ageel  9/13/2019
#100 Days of Python 
#Day 23 - Disctionary 3

employees1 = {"2001":"Ahmed","2002":"Salem","2003":"Waseem"}

#employees2 = employees1.copy()
employees2 = dict(employees1)

print(employees2.values())

myfamily = {

        "dad" :
        {
                "name" : "Ahmed",
                "year" : "1900"
        },
        "mom" :
        {
                "name" : "Sarah",
                "year" : "1904"
        },
         "son" :
        {
                "name" : "Jafar",
                "year" : "1944"
        },

}

dad = {
                "name" : "Ahmed",
                "year" : "1900"
}

mom = {
                    "name" : "Sarah",
                    "year" : "1904"
}

son = {
                    "name" : "Jafar",
                    "year" : "1944"
}

alsomyfamily = { 
         "dad" : dad,
         "mom" : mom,
         "son" : son,
}


frindsfamily = dict(dad="John",mom="Martha",son="Kevin")

print(alsomyfamily)
print(frindsfamily)