people = 20 
cars = 30
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't deside.")

if trucks > cars:
    print("That's too many trucks")
elif trucks < cars:
    print("Mabye we could take the trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's just stay home then")
