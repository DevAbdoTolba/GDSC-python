# check if equal or max and min from 2 aprmaters

def max(a,b):
    try:
        int(a)
        int(b)
    except Exception as e:
        print(e)
    else:
        if a > b:
            return a
        else:
            return b
    
def min(a,b):
    try:
        int(a)
        int(b)
    except Exception as e:
        print(e)
    else:
        if a < b:
            return a
        else:
            return b
        
def equal(a,b):
    try:
        int(a)
        int(b)
    except Exception as e:
        print(e)
    else:
        if a == b:
            return True
        else:
            return False