def add(a, b): #Vi laver en funktion og navngiver den. Til denne kan vi tilføje 2 værdier
    print(f"ADDING {a} + {b}") #Vi printer via en "f-string" hvor vi opstiller a og b med et plus tegn imellem. Disse er sat i {} da vi kalder på dem fra definationen af funktionen (a/b)
    return a + b #Vi returnere a+b når vi kalder funktionen 

def subtract(a, b): #Vi laver en funktion og navngiver den. Til denne kan vi tilføje 2 værdier
    print(f"SUBTRACTING {a} - {b}") #Omvendt opstiller vi her 2 tal med et minus imellem de angivet værdier
    return a - b #Vi returnere a+b når vi kalder funktionen 

def multiply(a, b): #Samme som ovenstående med gange
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b): #Samme som ovenstående blot med divider
    print(f"DIVIDING {a} / {b}")
    return a / b
 
 
print("Let's do some math with just functions!") #printer en string
 
age = add(30, 5) #Vi laver en variabel kaldet "age" og sætte den lig funktionen add lavet i linje 1
height = subtract(78, 4) #Vi laver en variabel kaldet "height" og sætte den lig funktionen add lavet i linje 5
weight = multiply(90, 2) #Vi laver en variabel kaldet "weight" og sætte den lig funktionen add lavet i linje 9
iq = divide(100, 2) #Vi laver en variabel kaldet "iq" og sætte den lig funktionen add lavet i linje 13

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}") #Her printer vi ovenstående variabler via en f-string med de givne variabler kaldet i {x} 
  
# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
 
what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) #Vi laver en variabel kaldet "What" og bruger de forskellige variable til at regne dem i "par" i forhold til
what2 = age + (height - (weight * (iq / 2))) #simplificeret

print("That becomes: ", what, "Can you do it by hand?")
print("That also becomes: ", what2, "Can you do it by hand?")