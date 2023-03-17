def readData():
    """
    This function reads all the data from the file you are storing as csv format,
    it skips the first line and start removing all '\\n' in the code,
    separate every single line and store every slice into an element in an array.
    finally return all the lines after it is fully compatible for the next step to be computed 

    ! make sure that the file is closed after every operation

    """



def printData():
    """
    The function takes the return value of the function readData and prints all of it in a formatted and clear way,
    it has 3 attributes : (ID name score)
    """



def readPlayer(id):
    """
    This function takes the id of the player wanted and returns the line which this player is located after calling the function readData
    """



def settingsMenu():
    """
    This function prints all players in a sorted and clear way to be represented for the user.
    Then ask the user which player is the one needed to be edited, using the id of the player.
    Show the player that was selected and then ask for what operation is wanted to be done (+,-,*,/)  # ! make sure that outliers is handled
    take the amount that will be edited and send him a confirmation message of how will the score be if he confirmed this operation
    then send those parameters (playerId, operation, amount) to a function called updatePlayer
    """




def updatePlayer(playerId, operation, amount):
    """
    This function takes the parameters (playerId, operation, amount) and then open the file in read mode and read all the lines
    then open the file in write mode and write all the lines except the one that was edited, then close the file.
    then open the file in append mode and append the edited line to the file.

    ! make sure that the file is closed after every operation
    """
