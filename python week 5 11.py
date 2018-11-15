Userinput ="changeme"
password = str
print("* * * Welcome to program! * * *")
print("* * * Give me the password!* * *")
attempts = 1


while password != Userinput:
    password = input("Give me the correct password: ")
    if apttemps > 3:
        print ("Acces denied")
        break
    if password != Userinput:
        print("Wrong password")
        attemps = attemps + 1
    if password == Userinput:
        print ("Accepted")
        print("Your attemps: ", attemps)
        break
