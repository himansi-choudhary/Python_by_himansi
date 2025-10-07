# if user don't give value for ending then this default value will use
def greet(name, ending = "Thank You"):
    print(f"Good day, {name}")
    print(ending)



greet("Himansi", "Have a nice Day!")
greet("Ritika")  #in this we did'n pass 2nd value so it we set default value