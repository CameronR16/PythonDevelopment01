age = 25

results = age > 18 and age < 30 #True and True
#True is only returned with "and" when both values are true. If the first comparison is false then that is outputted, if it is true then the second evaluation is outputted.

print(results)

ortest = age <18 or age > 22 #or only needs one value to be true to return true

print(ortest)

#and and or have opposite functionality

default_name = "there"
name = input("Enter your name (optional):")
username = name or default_name
print(f"hello {username}")