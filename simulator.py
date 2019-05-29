#Assembly simulator
#Written by Dr. Panos Papazoglou
#For educational purposes
#fisrt draft 29-5-19
#Copyright Dr. P. Papazoglou
import array
import os
import sys


CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

ins=['NOP 00 00 00 00',
'RD (A <-- KEYB) 01 00 00 00',
'WR (A --> CON) 02 00 00 00',
'ADD (A <-- A+B) 03 00 00 00',
'MOV (A <-- XX)  04 00 00 XX',
'MOV (B <-- XX)  05 00 00 XX',
'INC (A <-- A+1) 06 00 00 00',
'INC (B <-- B+1) 07 00 00 00',
'DEC (A <-- A-1) 08 00 00 00',
'DEC (B <-- B-1) 09 00 00 00',
'JNZ (A<>0, goto XX) 10 00 00 XX',
'JNZ (B<>0, goto XX) 11 00 00 XX',
'STOP (Termination)  12 00 00 00']

global PC
global A
global B
mem=array.array('i',(0 for i in range(0,100)))

PC=0
A=0
B=0





   
def main():
    empty_lines() 
    init_instructions() 
    print(CRED+"Dr. Panos Papazoglou \n"+CEND) 
    print("Assembly Simulator v1.0\n\n") 

    c=7

    while (c!=0): #do
        menu()
        c=read()
        if c==1:
            help()

        if c==2:
            execute()

        if c==3:
            enter_source()

        if c==4:
            clear_mem()

        if c==5:
            command_list()

        if c==6:
            print_mem_reg()

    return



def menu():
    print(CGREEN+"--------[Main menu]---------"+CEND) 
    print("[1] Help") 
    print("[2] Run") 
    print("[3] Insert code") 
    print("[4] Clear memory") 
    print("[5] Instruction set") 
    print("[6] Display REG/MEM") 
    print("[0] Exit") 
    print("---------------------------------") 
    print("Selection [1 to 6] or 0 for exit ") 
    return	 		 

		 #end menu
		 
def command_list():
    print("\n\n---[ Instruction set ]---") 
    for i in range (1,13,1): 
	    print(ins[i]) 
    print("-----------------------\n\n\n") 
    return
		
		 #end command list
		 
def init_instructions():


    return


def execute():
    print("Program execution...\n\n\n")
    global PC
    global jump
    PC=0
    inn=13
    while inn!=12:
        jump=0
        #next_command=mem[PC]
        next_command=mem[PC]
        print("next_command=",next_command)
        print("A=",A,", B=",B," , PC=",PC)
        next_command= { 1: exec1(),
			2: exec2(),
			3: exec3(),
			4: exec4(),
			5: exec5(),
			6: exec6(),
			7: exec7(),
			8: exec8(),
			9: exec9(),
			10: exec10(),
			11: exec11(),
		 }

        if (jump==0):
	        PC+=4
        inn=(mem[PC])


    print("\n Completed!!!")
    return


def exec1():
    global A
    print("A=")
    A=read()
    return

###########################################################



def exec2():
    global A
    print(A)
    return

def exec3():
    global A
    global B
    A=A+B
    return

def exec4():
    global A
    A=mem[PC+3]
    return

def exec5():
    global B
    B=mem[PC+3]
    return

def exec6():
    global A
    A+=1
    return

def exec7():
    global B
    B+=1
    return
 
def exec8():
    global A
    A-=1
    return 

def exec9():
    global B
    B-=1
    return 

def exec10():
    global PC
    global jump
    global A
    global mem 
    if (A!=0):
        PC=mem[PC+3]
        jump=1
    else:
        jump=0
    return 

def exec11():
    global B
    global PC
    global jump
    global mem
    if (B!=0):
        PC=mem[PC+3]  
        jump=1
    else:
        jump=0
    return




###########################################################






		 
def print_mem_reg():
    i=0
    while (i<=99):
        if (mem[i]!=0):
            print(CWHITEBG2+CBLACK+"["+str(i)+"]\t\t"+CGREEN+ins[mem[i]]+CEND)
        else:
            print(CGREY+"["+str(i)+"]\t\t"+CGREEN+ins[mem[i]])
        if (mem[i+3]!=0):
            print(CWHITE+", VALUE="+mem[i+3]+CEND)
        #else:
            #print("")
        i+=4
    print("\n PC=",PC,", A=",A,", B=",B)
    return


def enter_source():
    print("Instruction code")
    print("----------")
	#int command 
    XX=0
    PC=0
    command=13
    while (command!=12):
        print_mem_reg()
        print("Starting address [",PC,"]:")
        command=read()
        mem[PC]=command #bytes(command)
        if command==4:
            print("MOV A,XX\t[XX]=")
        if command==5:
            print("MOV B,XX\t[XX]=")
        if command==10:
            print("JNZ A,XX\t[XX]=")
        if command==11:
            print("JNZ B,XX\t[XX]=")
        if (command==4 or command==5 or command==10 or command==11):
            XX=read()
            mem[PC+3]=XX
        PC+=4
    return
		# }
		# while (command!=12) 
		 
		  		 
		 #end enter_source
		 
		 
def help():
    print(CWHITE+"----[Help]----\n") 
    print(CGREY+"1.Help = Display this text!") 
    print("2.Run = Assembly program execution starting from address 0 (PC=0)") 
    print("3.Insert code = Insert Assembly instruction in memory") 
    print("4.Clear memory = Set memory contents to zero") 
    print("5.Instruction set = Display available instruction set") 
    print("6.Display REGS/MEM = Display register and memory contents") 
    print("0.Exit = Exit from simulator\n\n") 
    return


def clear_mem():
    for i in range (0,99,1):
        mem[i]=0
    print("Memory Cleared!!")
    return

def empty_lines():
    os.system("clear")
    return


	#    for (byte i=1  i<=100  i++)
	#    System.out.print("\n") 
 
    
def read():
    br = input(":") 
    choice=int(br) 	 
    return choice
 
 
main()
sys.exit()

