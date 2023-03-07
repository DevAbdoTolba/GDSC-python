def readData():
    """
    This function reads all the data from the file you are storing as csv format,
    it skips the first line and start removing all '\\n' in the code,
    separate every single line and store every slice into an element in an array.
    finally return all the lines after it is fully compatible for the next step to be computed 

    ! make sure that the file is closed after every operation
    """

    file_data = open("./files/gameDataBase.txt", 'r') # opening the file in read mode and store it in f
    
    file_data.seek(11) # skip 11 characters  # ! Not 10?!, yep as '\n' is counted also
    
    lines = file_data.readlines() # Reading all lines from the file

    file_data.close() # closing the file

    lines = [ x.strip() for x in lines ] # remove all '\n' in all lines
    
    lines = [ x.split(',') for x in lines ] # divide every line into an array of values we stored in our database

    # print(lines) # print the lines :D
    return lines


def printData():
    """
    The function takes the return value of the function readData and prints all of it in a formatted and clear way,
    it has 3 attributes : (ID name score)
    """

    lines = readData()
    print(" ________________")
    print(" |ID\tname\t|score\t|")
    print(" ----------------")
    i = 0
    for line in lines:
        if i % 2 == 0:
            print(f' |{i+1}|{line[0]}\t|{line[1]}\t|')
        else :
            print(f' :{i+1}:{line[0]}\t:{line[1]}\t:')
        i +=1
    print(" ________________")




def readPlayer(id):
    """
    This function takes the id of the player wanted and returns the line which this player is located after calling the function readData
    """
    lines = readData()
    return lines[id]


def settingsMenu():
    """
    This function prints all players in a sorted and clear way to be represented for the user.
    Then ask the user which player is the one needed to be edited, using the id of the player.
    Show the player that was selected and then ask for what operation is wanted to be done (+,-,*,/)  # !make sure that outliers is handled
    take the amount that will be edited and send him a confirmation message of how will the score be if he confirmed this operation
    then send those parameters (playerId, operation, amount) to a function called updatePlayer
    """
    printData()
    playerId = input("\n\nchose the player you want to edit : ")
    playerData = readPlayer(int(playerId) - 1)
    print(f"editing {playerData[0]}...")
    operation = input("what operation do you want to do (+,-,*,/) : ") 

    # handle outliers
    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print("invalid operation")
        return

    amount = input("how much do you want to change : ")
    print(f"{playerData[0]} will be {int(playerData[1]) + int(amount)} after this operation")
    confirmation = input("confirm? (y/n) : ")
    if confirmation == 'y':
        updatePlayer(playerId, operation, amount)
    else:
        print("operation canceled")
        return
    

def updatePlayer(playerId, operation, amount):
    """
    This function takes the parameters (playerId, operation, amount) and then open the file in read mode and read all the lines
    then open the file in write mode and write all the lines except the one that was edited, then close the file.
    then open the file in append mode and append the edited line to the file.

    ! make sure that the file is closed after every operation
    """

    
    lines = readData()
    playerData = readPlayer(int(playerId) - 1)

    file_data = open("./files/gameDataBase.txt", 'w')
    
    file_data.write("name,score\n")
    for line in lines:
        if line[0] == playerData[0]:
            continue
        file_data.write(f"{line[0]},{line[1]}\n")

    file_data = open("./files/gameDataBase.txt", 'a')
    if operation == '+':
        file_data.write(f"{playerData[0]},{int(playerData[1]) + int(amount)}\n")

    elif operation == '-':
        file_data.write(f"{playerData[0]},{int(playerData[1]) - int(amount)}\n")

    elif operation == '*':
        file_data.write(f"{playerData[0]},{int(playerData[1]) * int(amount)}\n")

    elif operation == '/':

        file_data.write(f"{playerData[0]},{int(playerData[1]) / int(amount)}\n")

    else:
        print("invalid operation")
        return
    file_data.close()
    print("operation done successfully")



