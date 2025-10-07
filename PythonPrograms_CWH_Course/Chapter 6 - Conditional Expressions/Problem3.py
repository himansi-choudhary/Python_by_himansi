# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams.


spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

msg = input("Entre message: ")

if((spam1 in msg) or (spam2 in msg) or (spam3 in msg) or (spam4 in msg)):
    print("Detected Spam keywords")
else:
    print("not detect spam keyword, this is safe!")

