
"""
===================================//             //===================================
==================================//   import    //====================================
=================================//             //=====================================
"""


# import SayingHelloToTheWorldAllOfIt 


# SayingHelloToTheWorldAllOfIt.SayHelloName("Aya Sameh")


"""
===================================//         //===================================
==================================//   as    //====================================
=================================//         //=====================================
"""

# import SayingHelloToTheWorldAllOfIt as h


# h.SayHello()



"""
===================================//              //===================================
==================================//   shorter    //====================================
=================================//              //=====================================
"""


# from SayingHelloToTheWorldAllOfIt import SayHelloName

# SayHelloName("Tolba")




"""
===================================//          //===================================
==================================//   all    //====================================
=================================//          //=====================================
"""


# from SayingHelloToTheWorldAllOfIt import *

# SayHello()
# SayHelloName("Tolba")



"""
===================================//          //===================================
==================================//   dir    //====================================
=================================//          //=====================================
"""


import SayingHelloToTheWorldAllOfIt
import Alot

print(dir(SayingHelloToTheWorldAllOfIt)) #! This will print all the functions in the file
print(dir(Alot))

for var in dir(SayingHelloToTheWorldAllOfIt) :
    for sec in dir(Alot) :
        if sec == var :
            print("Conflict! " + str(sec) + " is found in both files" )
            break
    


"""
===================================//                      //===================================
==================================//     Conflicting!     //====================================
=================================//                      //=====================================
"""

# from SayingHelloToTheWorldAllOfIt import *

# from Alot import * # ! here



# # Logical Error :\

# SayHello()


"""
===================================//           //===================================
==================================//   Game    //====================================
=================================//           //=====================================
"""

"""
    For observing only, have a look at the code in the file "Game.py"
"""

# ! Now lets TEST A package

