import math
teamNumber = 27

#Our patient's body weight -- units: Newtons
bodyWeight = (52.5*9.8)
#The outer diameter of our patient's femur -- units: mm
outerDia =  17
#The diameter of our patient's medular canal -- units: mm
canalDiameter =9.5
#The offset of the centre of their mdular canal from the centre of the femoral head -- units: mm
canalOffset = 39
#The elastic modulus of bone
modulusBone = 30

#We allowed the user to input the following values so taht it will function for whichever material they choose
#The maximum stress a material can stand before it breaks  -- units: MPa
ultTenStrength = float(input("Enter the ultimate tnesile strength of the implant material in MPa: ")) 
#The elastic modulus of the implant material -- units: GPa
modulusImplant = float(input("Enter the elastic modulus of the implant material in GPa: "))

#define the subprogram 1 function 
def sp1 ():
    #set d equal to 0 -- it will increase by increments in the while loop 
    d = 0
    #the minimum required stem diameter for the inputed UTS -- it will be assigned the actual value in the while loop once the correct value as been determined
    minStemDia=0
    #the maximum amount of tensile stress applied to the implant -- it will be assigned the actual value in the while loop once the correct value as been determined
    appTenStress = 0
    #set c equal to 0 -- it will increase by increments in the while loop 
    c = 0
    #determines whether the while loop needs to continue -- becomes true when the correct value has been found 
    correct = False
    
    #runs until correct becomes True
    while(correct==False):
        
        #d increases by one each time the while loop runs
        d+=1
        
        #call the function ATSfunction to determine what applied tensile stress that will result in and if it is equal to the UTS entered
        if (round(ATSfunction(d),4)==round(ultTenStrength,4)):
            
            #set the minimum stem diameter equal to d (diameter that resulted in an applied tensile stress equal to the UTS entered)
            minStemDia=round(d,3)
            #set the applied tensile strength equal to the applied tensile strenght determined by ATSfunction using the parameter d
            appTenStress = round(ATSfunction(d),2)
            #change correct to True so that the while loop will no run again
            correct = True
            #break out of the first while loop
            break
        
        #if the applied tensile stress determined from ATSfunction is less than the UTS entered then d is too high
        elif (round(ATSfunction(d),4)<round(ultTenStrength,4)):
            
            #set c equal to d so that you have a maximum value (you know that the value of d is too high) 
            c=d
            #reduce d by 1
            d-=1
            
            #runs until correct becomes True, or the maximum value is reached
            while (correct==False and d+0.1<c):
                
                #d increases by 0.1 each time the while loop runs 
                d+=0.1
                
                #call the function ATSfunction to determine what applied tensile stress that will result in and if it is equal to the UTS entered
                if (round(ATSfunction(d),4)==round(ultTenStrength,4)):
                    
                    #set the minimum stem diameter equal to d (diameter that resulted in an applied tensile stress equal to the UTS entered)
                    minStemDia=round(d,3)
                    #set the applied tensile strength equal to the applied tensile strenght determined by ATSfunction using the parameter d
                    appTenStress = round(ATSfunction(d),2)
                    #change correct to True so that the while loop will no run again
                    correct = True
                    #break out of the second while loop
                    break
                
                #if the applied tensile stress determined from ATSfunction is less than the UTS entered then d is too high
                elif (round(ATSfunction(d),4)<round(ultTenStrength,4)):
                    
                    #set c equal to d so that you have a maximum value (you know that the value of d is too high)
                    c=d
                    #reduce d by 0.1
                    d-=0.1
                    
                    #runs until correct becomes True, or the maximum value is reached
                    while(correct == False and d+0.01<c):
                        
                        #d increases by 0.01 each time the while loop runs 
                        d+=0.01
                        
                        #call the function ATSfunction to determine what applied tensile stress that will result in and if it is equal to the UTS entered
                        if (round(ATSfunction(d),4)==round(ultTenStrength,4)):
                            
                            #set the minimum stem diameter equal to d (diameter that resulted in an applied tensile stress equal to the UTS entered)
                            minStemDia=round(d,3)
                            #set the applied tensile strength equal to the applied tensile strenght determined by ATSfunction using the parameter d
                            appTenStress = round(ATSfunction(d),2)
                            #change correct to True so that the while loop will no run again
                            correct = True
                            #break out of the third while loop
                            break
                        
                        #if the applied tensile stress determined from ATSfunction is less than the UTS entered then d is too high
                        elif (round(ATSfunction(d),4)<round(ultTenStrength,4)):
                            
                            #set c equal to d so that you have a maximum value (you know that the value of d is too high)
                            c=d
                            #reduce d by 0.01
                            d-=0.01
                            
                            #runs until correct becomes True, or the maximum value is reached
                            while(correct == False and d+0.001<c):
                                
                                #d increases by 0.1 each time the while loop runs 
                                d+=0.001
                                
                                #call the function ATSfunction to determine what applied tensile stress that will result in and if it is equal to the UTS entered
                                if (round(ATSfunction(d),4)==round(ultTenStrength,4)):
                                    
                                    #set the minimum stem diameter equal to d (diameter that resulted in an applied tensile stress equal to the UTS entered)
                                    minStemDia=round(d,3)
                                    #set the applied tensile strength equal to the applied tensile strenght determined by ATSfunction using the parameter d
                                    appTenStress = round(ATSfunction(d),2)
                                    #change correct to True so that the while loop will no run again
                                    correct = True
                                    #break out of the fourth while loop
                                    break
                                
                                #if the applied tensile stress determined from ATSfunction is less than the UTS entered then d is too high
                                elif (round(ATSfunction(d),4)<round(ultTenStrength,4)):
                                    
                                    #set c equal to d so that you have a maximum value (you know that the value of d is too high)
                                    c=d
                                    #reduce d by 0.001
                                    d-=0.001
                                    
                                    #runs until correct becomes True, or the maximum value is reached
                                    while(correct == False and d+0.0001<c):
                                        
                                        #d increases by 0.1 each time the while loop runs 
                                        d+=0.0001
                                        
                                        #call the function ATSfunction to determine what applied tensile stress that will result in and if it is equal to the UTS entered
                                        if (round(ATSfunction(d),2)==round(ultTenStrength,2)):
                                            
                                            #set the minimum stem diameter equal to d (diameter that resulted in an applied tensile stress equal to the UTS entered)
                                            minStemDia=round(d,3)
                                            #set the applied tensile strength equal to the applied tensile strenght determined by ATSfunction using the parameter d
                                            appTenStress = round(ATSfunction(d),2)
                                            #change correct to True so that the while loop will no run again
                                            correct = True
                                            #break out of the fifth while loop
                                            break
                                        
                                    #break out of the fourth while loop
                                    break
                            #break out of the third while loop 
                            break
                    #break out of the second while loop
                    break
            #break out of the first while loop
            break
    #
    
    #print all of the values that are asked for 
    print ("\nThe patients bodyweight is "+str(bodyWeight)+" N")
    print ("The diameter of the canal is "+str(canalDiameter)+" mm")
    print ("The Ultimate Tensile Strength is "+str(ultTenStrength)+" MPa")
    print ("The minimum implant stem diameter required is "+str(minStemDia)+" mm")
    print ("The applied tensile stress taht corresponds to the minimum allowable stem diameter is "+str(appTenStress)+" MPa\n")
#end of subprogram1

#define the ATSfunction that takes in one parameter d = diameter
def ATSfunction(d):
    #return the value of the applied tensile stress determined using d as the diameter
    return (14*bodyWeight*((8*canalOffset)-d))/(math.pi*(d**3))
#end of ATSfunction

#define the subprogram 3 function
def subprogram3():
   
    #the force applied is assumed to be 30 times the bodyweight of the patient
    force = 30*bodyWeight
    
    #the cross sectional area fo the patient's femur
    cross_secArea = math.pi/4 *(outerDia**2 - canalDiameter**2)
    #the compressive stress applied to the patient's femur
    stress_compression = force/cross_secArea
    #the compressive stress applied to the patient's femur after receiving their implant due to stress sheilding
    stressReduc = stress_compression * ((2*modulusBone)/(modulusBone + modulusImplant))**(1/2)
    #modulus ratio between the elastic modulus of the implant and the bone 
    Eratio = (modulusImplant/modulusBone)**(1/2)
    
    #the number of years since implantation -- it will increase by increments in the while loop 
    x = 0
    #the compressive stress on the bone that corresponds to yrsFail -- it will be set to the correct value in the while loop 
    stressFail = 0
    #the number of years after implantation before there is risk of femoral fracture -- it will be set to the correct value in the while loop 
    yrsFail = 0
    
    #runs until years since implantation reaches 100 -- we can be certain that the correct value can be found within this range
    while (x<100):
        #the value of years is going up by 0.01 each time the loop iterates, equivalent to saying x = x + 0.01
        x+= 0.01
        #call the function compStrength to determine if the compressive strength of the bone after x years is less than stressReduc
        #the stressFail will occur at the first value of compStrength that drops below the value of stressReduc
        if (round(compStrength(x,Eratio),4) <(stressReduc)):
            #set the value of stressFail equal to the compressive strength of the bone after x years
            stressFail = round(compStrength(x,Eratio),4)
            #set the value of yrsFail to x 
            yrsFail = round(x,4)
            #break out of the while loop
            break
    #print all of the values that are asked for 
    print ("\nThe number of years post-implantation before there is a risk of femoral fracture is "+str(yrsFail)+" years")
    print ("The compressive stress on the bone that corresponds to failure is "+str(round(stressFail,4))+" MPa\n" )
 
#define compStrength that takes in two variables, x = number of years since implantation, and Eration = the modulus ration   
def compStrength (x, Eratio):
    #return the value of compressive strength of bone determined using x as the number of years since implantation and Eratio as the modulus ratio
    return (0.001*x**2 - 3.437*x*(Eratio) + 181.72)

def main():
    exit = False
    while (exit==False):
        print ("      HOME")
        print ("1. Subprogram 1 \n2. Subprogram 2 \n3. Subprogram 3 \n4. Exit from program \n")
        choice = int(input("Please choose one of the following options by indicating the number that corresponds to your choice: "))
        if choice == 1:
            sp1()
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
