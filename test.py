file = open("textadventure.txt","w")
file.write("Welcome text file \n")
file.close()

file = open("textadventure.txt","r")
print(file.read())
file.close()



