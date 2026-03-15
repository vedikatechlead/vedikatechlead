import random 
chars = "abcdefghijklmnopqrstuvwxyz!@@##$%"
length = int(input("enter length:"))
passwords = ""

for a in range (length):
    passwords += random.choice(chars)
    
print("generated password:",passwords)    