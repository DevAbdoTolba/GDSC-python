def exception(condition_selector):
    """
    This function checks if the code is working properly.
    If not it will raise an error.    
    """
    if condition_selector == 1:
        # This is the code that will be checked and it has no error
        try:
            print("Hello World")     # This is the code that will be checked
        except:
            print("Error")           # This is the error message if the code is not working
        else:
            print("No, error, I am inside else")        # This is the message if the code is working
        finally:
            print("The 'try except' is finished") # This is the message that will be printed no matter what
    elif condition_selector == 2:
        # This is the code that will be checked and it has a syntax error
        try:
            prin("Hello World")     # This is the code that will be checked
        except Exception as e:
            # print the exception error message
            print("inside except block")
            print(e)
        else:
            print("No error, I am inside else")
        finally:
            print("The 'try except' is finished")

    elif condition_selector == 3:
         # This is the code that will be checked and it has a value error
        try:
            print(x)     # This is the code that will be checked
        except Exception as e:
            # print the exception error message
            print("inside except block")
            print(e)
        else:
            print("No error, I am inside else")
        finally:
            print("The 'try except' is finished")
    elif condition_selector == 4:
            # This is the code that will be checked and it has a name error
            try:
                x = int("Hello")     # This is the code that will be checked
            except Exception as e:
                # print the exception error message
                print("inside except block")
                print(e)
            else:
                print("No error, I am inside else")
            finally:
                print("The 'try except' is finished")




def error():
    """
    This function will raise an error.
    """
    raise Exception("Heello :>\n I am an error for no reason :D")



"""
================================//        //==============================
===============================// Errors //===============================
==============================//        //================================
"""

def syntaxError():
    """
    This function will raise a SyntaxError.
    """
    prin("Hello World")




def divide(x, y):
    """
    This function will divide two numbers.
    """
    try:
        result = x / y
    except ZeroDivisionError:
        print("You can't divide by zero")
    except TypeError:
        print("You can't divide a string by a number")
    else:
        print("The result is", result)
    finally:
        print("The 'try except' is finished")

def nameError():
    """
    This function will raise a NameError.
    """
    print(x)

def typeError():
    """
    This function will raise a TypeError.
    """
    print(5 + "5")

def valueError():
    """
    This function will raise a ValueError.
    """
    x = int("Hello")

def indexError():
    """
    This function will raise an IndexError.
    """
    x = [1, 2, 3]
    print(x[5])

def keyError():
    """
    This function will raise a KeyError.
    """
    x = {"name" : "John", "age" : 36}
    print(x["city"])

def attributeError():
    """
    This function will raise an AttributeError.
    """
    x = "Hello World"
    print(x.uppercase())

def importError():
    """
    This function will raise an ImportError.
    """
    import mymodule



# def indentationError():
#     """
#     This function will raise an IndentationError.
#     """
#     for x in range(5):
#     print(x)

# def tabError():
#     """
#     This function will raise a TabError.
#     """
#     print("Hello")
#         print("World")

def unicodeError():
    """
    This function will raise a UnicodeError.
    """
    x = b"\x81\x82"
    print(x.decode("utf-8"))

def unicodeEncodeError():
    """
    This function will raise a UnicodeEncodeError.
    """
    x = "Hello World"
    print(x.encode("ascii"))

def unicodeDecodeError():
    """
    This function will raise a UnicodeDecodeError.
    """
    x = b"\x81\x82"
    print(x.decode("ascii"))

def unicodeTranslateError():
    """
    This function will raise a UnicodeTranslateError.
    """
    x = b"\x81\x82"
    print(x.decode("utf-8", "ignore"))

def osError():
    """
    This function will raise an OSError.
    """
    f = open("demofile.txt")

def eofError():
    """
    This function will raise an EOFError. EOFERror stands for End Of File Error.
    """
    x = int(input("Enter a number: "))
    print(x)

def runtimeError():
    """
    This function will raise a RuntimeError.
    """
    x = 5
    y = 0
    z = x / y

def notImplementedError():
    """
    This function will raise a NotImplementedError.
    """
    x = 5
    y = 0
    z = x / y
    raise NotImplementedError

def recursionError():
    """
    This function will raise a RecursionError.
    """
    def tri_recursion(k):
        if(k > 0):
            result = k + tri_recursion(k - 1)
            print(result)
        else:
            result = 0
        return result
    print("\n\nRecursion Example Results")
    tri_recursion(6)

def memoryError():
    """
    This function will raise a MemoryError.
    """
    x = []
    while True:
        x.append("Hello World")

def referenceError():
    """
    This function will raise a ReferenceError.
    """
    x = 5
    print(x)
    del x # This will delete the variable x from the memory
    print(x)

def systemError():
    """
    This function will raise a SystemError.
    """
    x = 5
    print(x)
    del x # This will delete the variable x from the memory
    print(x)
