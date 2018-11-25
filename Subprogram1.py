import math
teamNumber = 27
bodyWeight = (52.5*9.8)
#units: Newtons
outerDia =  17
#units: mm
canalDiameter =9.5
#units: mm
canalOffset = 39
#units: mm
modulusBone = 30
ultTenStrength = 490
#units: MPa
#The maximum stress a material can stand before it breaks 
#material is a Titanium alloy --> Ti-29Nb-13Ta-4.6Zr
modulusImplant = 47 
#units: GPa

def subprogram1 ():
    d = canalDiameter
    minStemDia=0
    appTenStress = 0
    c = 0
    correct = False
    
    while(correct==False):
        d+=1
        if (round(UTSfunction(d),4)==ultTenStrength):
            minStemDia=round(d,3)
            correct = True
            break
        elif (round(UTSfunction(d),4)<ultTenStrength):
            c=d
            d-=1
            while (correct==False and d+0.1<c):
                d+=0.1
                if (round(UTSfunction(d),4)==ultTenStrength):
                    minStemDia=round(d,3)
                    appTenStress = round(UTSfunction(d),2)
                    correct = True
                    break
                elif (round(UTSfunction(d),4)<ultTenStrength):
                    c=d
                    d-=0.1
                    while(correct == False and d+0.01<c):
                        d+=0.01
                        if (round(UTSfunction(d),4)==ultTenStrength):
                            minStemDia=round(d,3)
                            appTenStress = round(UTSfunction(d),2)
                            correct = True
                            break
                        elif (round(UTSfunction(d),4)<ultTenStrength):
                            c=d
                            d-=0.01
                            while(correct == False and d+0.001<c):
                                d+=0.001
                                if (round(UTSfunction(d),4)==ultTenStrength):
                                    minStemDia=round(d,3)
                                    appTenStress = round(UTSfunction(d),2)
                                    correct = True
                                    break
                                elif (round(UTSfunction(d),4)<ultTenStrength):
                                    c=d
                                    d-=0.001
                                    while(correct == False and d+0.0001<c):
                                        d+=0.0001
                                        if (round(UTSfunction(d),2)==ultTenStrength):
                                            minStemDia=round(d,3)
                                            appTenStress = round(UTSfunction(d),2)
                                            correct = True
                                            break
                                        #if 0.0001
                                    #while 0.0001
                                    break
                                #elif 0.001        
                            #while 0.001  
                            break
                        #elif 0.01
                    #while 0.01
                    break
                #elif 0.1
            #while 0.1
            break
        #elif 1
    #while
    print ("\nThe patients bodyweight is "+str(bodyWeight)+" N")
    print ("The diameter of the canal is "+str(canalDiameter)+" mm")
    print ("The Ultimate Tensile Strength is "+str(ultTenStrength)+" MPa")
    print ("The minimum implant stem diameter required is "+str(minStemDia)+" mm")
    print ("The applied tensile stress taht corresponds to the minimum allowable stem diameter is "+str(appTenStress)+" MPa\n")


def UTSfunction(d):
    return (14*bodyWeight*((8*canalOffset)-d))/(math.pi*(d**3))

def main():
    exit = False
    while (exit==False):
        print ("      HOME")
        print ("1. Subprogram 1 \n2. Subprogram 2 \n3. Subprogram 3 \n4. Exit from program \n")
        choice = int(input("Please choose one of the following options by indicating the number that corresponds to your choice: "))
        if choice == 1:
            subprogram1()
            #a parameter must be passed in the paranthesis
        elif choice == (2):
            subprogram2()
            #a parameter must be passed in the paranthesis
        elif choice == (3):
            subprogram3()
            #a parameter must be passed in the paranthesis
        elif choice ==(4):
            exit = True
            print ("You have exited from the program.")
    
    print ("Thank you for using the program")
main()
