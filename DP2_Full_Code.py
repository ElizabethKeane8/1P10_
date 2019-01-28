'''
Elizabeth Keane, Yasemin Al-Banna, Haider Khan, Aiden Delaney
Team Number 27 
'''

import math
    
'''
Name: subprogram1
Purpose: to determine the minimum stem diameter required for a given ultimate tensile strength using Newton's Method
Parameters: float ultTenStrength - ultimate tensile strength of the implant material, float bodyWeight - the body weight of our patient,
            float canalOffset - the horizontal distance between the centre of the femoral head and the centre of the medulary canal of our 
            patient, float canalDiameter - the diameter of our patient's medulary canal
Return: void
'''
def subprogram1 (ultTenStrength, bodyWeight, canalOffset, canalDiameter):
    
    d = canalDiameter
    #calculate the absolute difference between the ATS value and the UTS value (to make sure that they are within the tolerance of 0.0001)
    delta = abs(ultTenStrength-ATS(d,bodyWeight, canalOffset))
    
    #it will run until an ATS value is found that is within the tolerance
    while (delta>0.0001):
        #use Newton's Method 
        #(it is ATS - UTS since Newton's method is solving for the root (0) which is the difference between the two)
        d = d - (ATS(d,bodyWeight, canalOffset)-ultTenStrength)/ATSderivative(d)
        delta = abs(ultTenStrength-ATS(d,bodyWeight, canalOffset))
    #minStemDia is equal to the d value that led to an ATS within the tolerance of UTS
    minStemDia = round(d,4)
    appTenStress = round(ATS(d,bodyWeight, canalOffset),2)
    
    #print all of the values that are asked for 
    print ("\n    The patients bodyweight is "+str(bodyWeight)+" N")
    print ("    The diameter of the canal is "+str(canalDiameter)+" mm")
    print ("    The Ultimate Tensile Strength is "+str(ultTenStrength)+" MPa")
    print ("    The minimum implant stem diameter required is "+str(minStemDia)+" mm")
    print ("    The applied tensile stress taht corresponds to the minimum allowable stem diameter is "+str(appTenStress)+" MPa\n") 

'''
Name: ATS
Purpose: to calculate the applied tensile strength for a given diameter 
Parameters: float d - diameter, float bodyWeight - the body weight of our patient, float canalOffset - the horizontal distance between 
            the centre of the femoral head and the centre of the medulary canal,
Return: float
'''
def ATS(d, bodyWeight, canalOffset):
    return (14*bodyWeight*((8*canalOffset)-d))/(math.pi*(d**3))

'''
Name: ATSderivative
Purpose: to calculate derivative of ATS at the point d
Parameters: float d - diameter
Return: float
'''
def ATSderivative(d):
    #this is the derivative for the equation in ATS using the bodyWeight and canalOffset values at the begining of the program
    return (-(14406*(468-d))/(math.pi*(d**4)))

'''
Name: subprogram2
Purpose: to determine the number of cycles until failure due to fatigue 
Parameters: String filename - the file with the S-N values, float bodyWeight - the body weight of our patient, float canalDiameter
             - the diameter of our patient's medulary canal
Return: void
'''
def subprogram2 (filename, bodyWeight, canalDiameter):
    #open and read the file
    inFile = open(filename,'r')
    lines = inFile.readlines()
    inFile.close()
    
    #split the list lines into a list of lists
    linesL = []
    for i in lines:
        split = i.split()
        split[0] = float(split[0])
        split[1] = float(split[1])
        linesL.append(split)
    #
    
    #determine the maximum and minimum loads
    maxLoad = bodyWeight*10
    minLoad = bodyWeight*(-10)
    
    #determine the maximum and minimum stress and the stress amplitude
    #we used the canalDiameter for the stem diameter since the minimum stem diameter is only known if subprogram 1 is run first
    maxStress = maxLoad/((math.pi/4)*(canalDiameter**2)) ##stemDia
    minStress = minLoad/((math.pi/4)*(canalDiameter**2)) ##stemDia
    amplitude = ((maxStress-minStress)/2)
    
    stressFail = 0
    cyclesFail = 0
    
    #it will run through all of the values in the linesL list until one of the conditions is met
    for i in range(len(linesL)):
        
        #checks if the maximum amplitude for a given N value is equal to the S value corresponding to that N value
        if (linesL[i][0]==Smax(amplitude,linesL[i][1])):
            #then that is the exact number of cycles until failure
            stressFail = Smax(amplitude,linesL[i][1])
            cyclesFail = linesL[i][1]
            break
        #checks if the maximum amplitude for a given N value is greater than the S value corresponding to that N value
        elif (linesL[i][0]<Smax(amplitude,linesL[i][1])):
            #then that is more than the number of cycles until failure
            #therefore you set the values equal to the item in the list directly before, since you know for sure that it won't fail after that many cycles
            stressFail = Smax(amplitude,linesL[i-1][1]) 
            cyclesFail = linesL[i-1][1]
            break
    
    #print all of the values that are asked for 
    print ("\n    The number of cycles N at which failure due to fatigue is likely to occur is "+str(cyclesFail)+" cycles")
    print ("    The maximum stress amplitude that corresponds to failure is "+str(stressFail)+" MPa\n")
 
'''
Name: Smax
Purpose: to determine the maximum stress amplitude based on the number of cycles N
Parameters: float A -- the stress amplitude, float N -- the number of cycles
Return: float
'''   
def Smax (A, N):
    return A*(6+(math.log(N,10)**(teamNumber/30)))

'''
Name: subprogram3
Purpose: to determine the number of years post-implantation before there is risk of femora fracture
Parameters: float modulusImplant - the elastic modulus of the implant material, float bodyWeight - the body weight of our patient,
            float outerDia - the outer diameter our our patient's femur, float canalDiameter - the diameter of our patient's medulary canal,
            int modulusBone - the elastic modulus of bone
Return: void
'''
def subprogram3(modulusImplant, bodyWeight, outerDia, canalDiameter, modulusBone):
   
    force = 30*bodyWeight
    
    cross_secArea = math.pi/4 *(outerDia**2 - canalDiameter**2)
    stress_compression = force/cross_secArea
    #the compressive stress applied to the patient's femur after receiving their implant due to stress sheilding
    stressReduc = stress_compression * ((2*modulusBone)/(modulusBone + modulusImplant))**(1/2)
    #modulus ratio between the elastic modulus of the implant and the bone 
    Eratio = (modulusImplant/modulusBone)**(1/2)
    #the number of years since implantation 
    x = 0
    stressFail = 0
    yrsFail = 0
    
    correct = False
    
    #runs until a correct value is found
    while (correct == False):
        #the value of years is going up by 0.01 each time the loop iterates, equivalent to saying x = x + 0.01
        x+= 0.01
        #call the function compStrength to determine if the compressive strength of the bone after x years is less than stressReduc
        #the stressFail will occur at the first value of compStrength that drops below the value of stressReduc
        if (round(compStrength(x,Eratio),4) <=(stressReduc)):
            stressFail = round(compStrength(x,Eratio),4)
            #yrsFail is the int of x since it is rounded down -- it can't be rounded up since it will fail have failed by that point
            yrsFail = int(x)
            correct = True
            break
    #print all of the values that are asked for 
    print ("\n    The number of years post-implantation before there is a risk of femoral fracture is "+str(yrsFail)+" years")
    print ("    The compressive stress on the bone that corresponds to "+str(yrsFail)+ " years is "+str(round(stressFail,4))+" MPa\n" )
 
'''
Name: compStrength
Purpose: to determine the compressive strength of bone based on the number of years post-implantation
Parameters: float x -- number of year post-implantation, float Eratio -- the elastic modulus ratio
Return: float
'''
def compStrength (x, Eratio):
    #return the value of compressive strength of bone determined using x as the number of years since implantation and Eratio as the modulus ratio
    return (0.001*x**2 - 3.437*x*(Eratio) + 181.72)

def main():
    
    teamNumber = 27
    bodyWeight = (52.5*9.8) #N
    outerDia =  17 #mm
    canalDiameter = 9.5 #mm
    canalOffset = 39 #mm
    #modulusBone was found in the IBEHS 1P10 Project Modules, pg.41 DP-2
    modulusBone = 30
    
    exit = False
   
    #We allowed the user to input the modulus and UTS of the material so that it will function for whichever material they choose

    while (exit==False):
        print ("      HOME")
        print ("1. Subprogram 1 \n2. Subprogram 2 \n3. Subprogram 3 \n4. Exit from program \n")
        choice = int(input("Please choose one of the following options by indicating the number that corresponds to your choice: "))
        if choice == 1:
            #call subprogram 1 using the UTS entered by the user
            ultTenStrength = float(input("Enter the ultimate tnesile strength of the implant material in MPa: "))
            subprogram1(ultTenStrength, bodyWeight, canalOffset, canalDiameter)
        elif choice == (2):
            #call subprogram 2 using the file entered by the user
            filename = str(input("Enter the filename you would like to open: "))
            subprogram2(filename, bodyWeight, canalDiameter)
        elif choice == (3):
            #call subprogram 3 using the elastic modulus entered by the user
            modulusImplant = float(input("Enter the elastic modulus of the implant material in GPa: "))
            subprogram3(modulusImplant, bodyWeight, outerDia, canalDiameter, modulusBone)
        elif choice ==(4):
            #exit the program
            exit = True
            print ("You have exited from the program.")
    
    print ("Thank you for using the program")
main()   
