all = ""

try :
    fhandler = open("att.txt", 'r')
except :
    fhandler = open("att.txt", 'x')
finally : 
    file = fhandler.read()
    fhandler.close()
    all = file
    print(all)
    # file = fhandler.readlines()
    # all = file

    # CSV, comma sepreate values

fhandler = open("att.txt", 'w')

print("Attended are " + str(len(all.split("\n"))-1), end="")
print("\n"+str(all))

attendance = input("\nHow many are in class: ")

for i in range(int(attendance)):
    name = input("Name: ")
    all = (str(all) + str(name)+"\n")

print(all)

fhandler.write(str(all))


fhandler.close