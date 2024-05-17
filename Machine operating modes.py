# PROGRAMME DEFINITION
##  The programme shall have 3 modes of operation (Stop, Automatic and Manual) of the machine.
## At the same time the program will control 10 motors, for this we made the lists with the 3 modes and a multidimensional array to control the 10 motors.

# General Variables
BtnStop= False
BtnAuto= True
BtnMan= False

# Variables for registering arrays
Stop=0
Auto=1
Man=2
Pos=0 

# Arrays list of operating modes for the machine
ModVar_0= [False, False, False]
ModVar_1= [False, False, False]
ModVar_2= [False, False, False]
ModVar_3= [False, False, False]
ModVar_4= [False, False, False]
ModVar_5= [False, False, False]
ModVar_6= [False, False, False]
ModVar_7= [False, False, False]
ModVar_8= [False, False, False]
ModVar_9= [False, False, False]

# Array register (in the array [vGlobal] we enter the list of modes)
vGlobal= [ModVar_0, ModVar_1, ModVar_2, ModVar_3, ModVar_4, ModVar_5, ModVar_6, ModVar_7, ModVar_8, ModVar_9]

# Conditional modes (Stop, Auto and Manual) of the machine

if BtnStop:
    vGlobal[Pos][Stop]= True
    vGlobal[Pos][Auto]= False
    vGlobal[Pos][Man]= False

if BtnAuto:
    vGlobal[Pos][Stop]= False
    vGlobal[Pos][Auto]= True
    vGlobal[Pos][Man]= False

if BtnMan:
    vGlobal[Pos][Stop]= False
    vGlobal[Pos][Auto]= False
    vGlobal[Pos][Man]= True

print(vGlobal[0], vGlobal[1], vGlobal[2], vGlobal[3], vGlobal[4], vGlobal[5], vGlobal[6], vGlobal[7], vGlobal[8], vGlobal[9])