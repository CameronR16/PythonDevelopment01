#age = 21
#age_to_string = str(age)
#print("Cameron you are " + age_to_string)
#print(f"Cameron you are {age}") # f strings are easier to use than the above. Only v3.6.1 and above

#name = "Bob"
#greeting = f"How are you {name}"
#print(greeting)

#name = "Dave"
#print(greeting) #This will return the name as bob twice, because name was defined as bob when the greeting was created.


#This solves the above problem
name = "Bob"
final_greeting = "How are you,{}" #Creates a template to use
bob_greeting = final_greeting.format(name) #Passes in the name variable to {}
print(bob_greeting)

name = "Juan"
juan_greeting = final_greeting.format(name)
print(juan_greeting)

