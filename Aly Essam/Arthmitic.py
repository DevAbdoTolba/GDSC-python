# sum and div and sub and mul methods with excpetion handling

def sum(a,b):
    try :
        int(a)
        int(b)
    except Exception as e:
        print(e)
    else :
        return a+b
    
def div(a,b):
    try :
        int(a)
        int(b)
        res = a/b
    except Exception as e:
        print(e)
    else :
        return res

def sub(a,b):
    try :
        int(a)
        int(b)
    except Exception as e:
        print(e)
    else :
        return a-b
    

def mul(a,b):
    try :
        int(a)
        int(b)
    except Exception as e:
        print(e)
    else :
        return a*b
    
