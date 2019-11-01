
age = {}
colour = {}


name = input("What's your name?")
print("That's a good name!")

age_key = input("How old are you?")
if age_key in age.keys():
	print(age[age_key])
else:
	print("Nice!")

colour_key = input("What is your favourite colour?")
if colour_key in colour.keys():
	print(colour[colour_key])
else:
	print("I like that too!")

py = input("Do you like python?")
py.lower()
if py == "yes" or "y":
	print("Great!")
elif py == "no" or "n":
	print("Oh no! You should try Python!")
else:
	print("Hmmm")

world = input("The world is flat: True or False?")
if world == "True" or "true":
	print("Clever!")
else:
	print("The world should be flat...")
