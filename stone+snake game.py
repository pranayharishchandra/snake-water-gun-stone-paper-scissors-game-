import random

print("\n🙏.........................WELCOME.......................🙏\n")

def snake():
    t=0
    count, comp=0, 0
    while t==0:
        print("\n")
    

        A=int(input("PRESS \n0 for SNAKE \n1 for WATER \n2 for GUN \n👉  "))
        B = random.randrange(0, 3)

        C =["SNAKE" , "WATER" , "GUN"]
        print("\n")
        print("---------------------------------------------------------","\n")
        print("You chose               :              ", C[A])
        print("Computer chose          :              ", C[B], "\n")

        print("---------------------------------------------------------","\n")
    
        if (A==B):
            print("RESULT                 :          DRAW")

        elif(((A==0)&(B==1)) or ((A==1)&(B==2)or( ((A==2)&(B==0))))):
            count = count+1
            print("                     RESULTS           ")
            print("\n                     YOU WIN            ")
            print("Your score is           :              ",count, "\nComp score is           :              ", comp, "\n")
        else:
            comp+=1
            print("             ",C[B]," WINS OVER ", C[A])
            print("                    COMP WIN             ")
            print("Your score is           :              ",count, "\nComp score is           :              ", comp, "\n")
            print("")

        print("---------------------------------------------------------","\n")



        # print("*****************************************************")
        print("*********************************************************")


        t = int(input ("PRESS 0 TO KEEP PLAYING THE GAME  \n1 TO EXIT FROM SNAKE WATER GUN  \n 👉 "))

        # print("*****************************************************")
        print("*********************************************************")



def stone():
    t=0
    count, comp=0, 0

    while t==0:
        print("\n")
    

        A=int(input("PRESS \n0 for STONE \n1 for PAPER \n2 for SCISSORS \n👉  "))
        B = random.randrange(0, 3)

        C =["STONE" , "PAPER" , "SCISSORS"]
        print("\n")
        print("---------------------------------------------------------","\n")
        print("You chose               :              ", C[A])
        print("Computer chose          :              ", C[B], "\n")

        print("---------------------------------------------------------","\n")
    
        if (A==B):
            print("RESULT                 :          DRAW")

        elif(((A==0)&(B==1)) or ((A==1)&(B==2)or( ((A==2)&(B==0))))):
            count = count+1
            print("                     RESULTS           ")
            print("\n                     YOU WIN            ")
            print("Your score is           :              ",count, "\nComp score is           :              ", comp, "\n")
        else:
            comp+=1
            print("             ",C[B]," WINS OVER ", C[A])
            print("                    COMP WIN             ")
            print("Your score is           :              ",count, "\nComp score is           :              ", comp, "\n")
            print("")

        print("---------------------------------------------------------","\n")




        print("*********************************************************")


        t = int(input ("PRESS 0 TO KEEP PLAYING THE GAME     \n1 TO EXIT FROM STONE PAPER SCISSORS\n👉 "))

        print("*********************************************************")



p=0
while p==0 :
    a = int(input("\nPRESS \n0 for STONE PAPER SCISSORS \n1 for SNAKE WATER GUN \n👉 "))
    if (a==0) :
        stone()
    elif a==1 :
        snake()
    print("\n👉   NOW YOU CAN CHOOSE BETWEEN SNAKE GAME AND STONE GAME   ")
    p = int(input("\n           PRESS 0 TO SWITH BETWEEN GAMES😇 \n             1 TO EXIT FROM WHOLE GAME😢 \n👉 "))

print("\n                  THANK FOR PLAYING\n                   HAVE A NICE DAY😊\n")

