import math
teamNumber = 27
bodyWeight = (52.5*9.8)
#units --> Newtons
outerDia =  17
#units --> mm
canalDiameter =9.5
#units --> mm
canalOffset = 39
#units --> mm
modulusBone = 30
ultTenStrength = 490
#The maximum stress a material can stand before it breaks 
#material is a Titanium alloy --> Ti-29Nb-13Ta-4.6Zr
modulusImplant = 47 
#units = GPa

def sp1 ():
    d = 9.5
    minStemDia=0
    c = 0
    
    correct = False
    
    while(correct==False):
        d+=1
        if (round(UTSfunction(d),4)==ultTenStrength):
            minStemDia=round(d,4)
            correct = True
            break
        elif (round(UTSfunction(d),4)<ultTenStrength):
            c=d
            d-=1
            while (correct==False and d+0.1<c):
                d+=0.1
                if (round(UTSfunction(d),4)==ultTenStrength):
                    minStemDia=round(d,4)
                    correct = True
                    break
                elif (round(UTSfunction(d),4)<ultTenStrength):
                    c=d
                    d-=0.1
                    while(correct == False and d+0.01<c):
                        d+=0.01
                        if (round(UTSfunction(d),4)==ultTenStrength):
                            minStemDia=round(d,4)
                            correct = True
                            break
                        elif (round(UTSfunction(d),4)<ultTenStrength):
                            c=d
                            d-=0.01
                            while(correct == False and d+0.001<c):
                                d+=0.001
                                print (round(UTSfunction(d),4), ultTenStrength)
                                if (round(UTSfunction(d),4)==ultTenStrength):
                                    minStemDia=round(d,4)
                                    correct = True
                                    break
                                elif (round(UTSfunction(d),4)<ultTenStrength):
                                    c=d
                                    d-=0.001
                                    while(correct == False and d+0.0001<c):
                                        d+=0.0001
                                        print (round(UTSfunction(d),2), ultTenStrength)
                                        if (round(UTSfunction(d),2)==ultTenStrength):
                                            minStemDia=round(d,4)
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
    
    print("minStemDia = ",minStemDia)


def UTSfunction(d):
    return (14*bodyWeight*((8*canalOffset)-d))/(math.pi*(d**3))

sp1()
