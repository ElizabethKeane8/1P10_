'''
DP-3 Milestone 4 -- Preliminary Python Program
Elizabeth, Kate, Sofie, Mandy
Jan 28
'''

def readData(filename):
    '''
    Name: readData
    Purpose: to read the data from the sample text file
    @param: filename --> the name of the file we are reading from
    @return: linesList --> a list containing the contents of the file
    '''
    
    inFile = open(filename,'r')
    linesList = inFile.readlines()
    inFile.close()
    
    return linesList

def Check(file):
    '''
    Name: Check
    Purpose: To check if there is any rotation around the X and Y axis
    @param: file --> a list containing the contents of the text file
    @return: void
    '''
    
    #starts with vib as False since it is not vibrating
    vib = False
    #i is equal to three because the first three indices (0,1,2) are not significant to our program
    i=3
    #runs through the length of the list called file
    while i<len(file):
        angleX = file[i]
        angleY = file[i+1]
        #will run if the motor is not vibrating
        if (vib == False):
            #if it is (significantly) rotated around the Y axis then it will start vibrating
            if (float(angleY)>=15): 
                print("Starts to vibrate!")
                vib = True
            elif (float(angleY)<=-15):
                print("Starts to vibrate!")
                vib = True
            #if it is (significantly) rotated around the X axis then it will start vibrating
            elif (float(angleX)<=-15):
                print("Starts to vibrate!")
                vib = True
            elif (float(angleX)>=15):
                print("Starts to vibrate!")
                vib = True
            #if the rotation is not significant enough it will not vibrate
            else:
                print("Does not vibrate")
                
        #will run if the motor is vibrating but the button hasn't been pressed yet
        elif (vib == True):
            print("Still vibrating")
            
        #checks to see if the button is pressed after the data is inputed
        try:
            #if the data is a float, then this will be true and the button hasn't been pressed so it will continue to run as normal
            float(file[i+3])
        except:
            #if the data is not a float that means that it is 'button' and the button has been pressed --> it stops vibrating
            print("Button pressed - stops vibrating")
            vib = False
            i=i+1
        #i is increased by six since the data is given in groups of six, so the next value will be six indices away
        i+=6

def main():
    #calls readData
    filename = 'SampleData.txt'
    file = readData(filename) 
    #calls the check method
    Check(file)
main()
