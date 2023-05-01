types_of_people = 10
x = f"There are {types_of_people} types of people."    #String inside a string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #String inside a string

#This is a comment - lad os bare sige de er på allesammen
print(x)
print(y)

print(f"I said: {x}") #String inside a string
print(f"I also said: '{y}'") #String inside a string 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) 
#String inside a string. joke_evaluation indeholder en string som har en "pladsholder" via {}. 
#Denne pladsholder sættes lig med hilarious som resultere en ny tekstreng med værdien tilført

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
#Strengen bliver længere da vi + to ens typer af data "strings"