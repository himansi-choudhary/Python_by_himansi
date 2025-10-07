# 3. Install an external module and use it to perform an operation of your interest. 

# step 1:- open vs code terminal write --> pip install pyttsx3

# step 2:-
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()