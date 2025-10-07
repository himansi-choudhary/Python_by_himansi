# name is argument it receive value
def greet(name):
    print("Good day, " + name)


# Himanis is parameter that passed to fuction
greet("Himansi")






# we can tack more than one argument
def greet(name, ending):
    print("Good day, " + name)
    print(ending)
    return "Done"  # this will return to last one a = gourav...

greet("Himansi", "Thank you")
greet("Ritika", "Thank you")

a = greet("Gourav", "Thanks")
print(a)