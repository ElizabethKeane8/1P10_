'''
Created on Nov 23, 2018

@author: Elizabeth
'''

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
        print("while 1",d,c)
        if (round(function(d),4)==ultTenStrength):
            minStemDia=function(d)
            correct = True
            break
        elif (round(function(d),4)<ultTenStrength):
            c=d
            d-=1
            while (correct==False and d+0.1<c):
                d+=0.1
                print ("while 2",d,c)
                if (round(function(d),4)==ultTenStrength):
                    minStemDia=function(d)
                    correct = True
                    break
                elif (round(function(d),4)<ultTenStrength):
                    c=d
                    d-=0.1
                    while(correct == False and d+0.01<c):
                        d+=0.01
                        print("while 3",d,c)
                        if (round(function(d),4)==ultTenStrength):
                            minStemDia=function(d)
                            correct = True
                            break
                        elif (round(function(d),4)<ultTenStrength):
                            c=d
                            d-=0.01
                            while(correct == False and d+0.001<c):
                                d+=0.001
                                print("while 4",d,c)
                                if (round(function(d),4)==ultTenStrength):
                                    minStemDia=function(d)
                                    correct = True
                                    break
                                elif (round(function(d),4)<ultTenStrength):
                                    c=d
                                    d-=0.001
                                    while(correct == False and d+0.0001<c):
                                        d+=0.0001
                                        print("while 5",d, c)
                                        if (round(function(d),4)==ultTenStrength):
                                            minStemDia=function(d)
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


def function(d):
    return (14*bodyWeight*((8*canalOffset)-d))/(math.pi*(d**3))

sp1()