# This file will take a message, run it through the rotors/reflector and make it into gobbledegook.
# Will have to:
# 1) Get message
# 2) Run one letter through rotor/reflector encryption
# 3) Increment rotor position
# 3) Repeat steps 2 + 3 until message is fully encrypted
# 4) Write message to text file (this could be happening continuously whilst each letter is encrypted)

from rotors import rotorPosition, rotor_1, rotor_2, rotor_3, reflector, rotor_1_b, rotor_2_b, rotor_3_b
# NOTE:  The rotorPosition variable will change as this file runs. The new rotor position will not be saved to the rotors module. 





newList = []

def access_text_file():
    #opens the file
    #creates a file object (f)
    #reads the file object
    #creates the global "message" variable using the file object
    global message
    with open('write_message_here.txt', 'r', encoding="utf-8") as f:
        print("message imported")
        print("message reads as follows:")
        message = f.read()
        print(message)
    

def increment_rotor_position():
    #Each time a letter is encrypted, the rotor position increments.
    #Rotor 3 increases by 1 every time the rotor position increments.
    #If rotor 3 = 26, it goes back to zero and the rotor 2 position increases by one.
    #If rotor 2 = 26, it goes back to zero and the rotor 1 position increases by one.
    #If rotor 1 = 26, it goes back to zero.

    rotorPosition["rotor3"] = rotorPosition["rotor3"]+1
    if rotorPosition["rotor3"] == 26:
        rotorPosition["rotor3"] = 0
        rotorPosition["rotor2"] = rotorPosition["rotor2"]+1
        if rotorPosition["rotor3"] == 26:
            rotorPosition["rotor2"] = 0
            rotorPosition["rotor1"] = rotorPosition["rotor1"]+1
            if rotorPosition["rotor1"] == 26:
                rotorPosition["rotor1"] = 0

    
def encode_letter_forwards():
    #This has to run the letter in question through the rotors to get a new letter
    #Change the letter into an initial number
    #Run through first rotor (use dictionary)
    #Get correct corresponding second rotor starting value
    #Run through second rotor etc.
    #Change number back into a letter
    #NOTE - ord() makes a = 97- it uses ASCII (https://www.asciitable.com/)
    
    letterNumber = ord(letter) - 97 

    newLetter = rotor_1.get(letterNumber)
    rotorPosDif = rotorPosition.get("rotor2") - rotorPosition.get("rotor1")
    newLetter = newLetter + rotorPosDif
    newLetter = rationalise_newLetter(newLetter)
    newLetter = rotor_2.get(newLetter)
    rotorPosDif = rotorPosition.get("rotor3") - rotorPosition.get("rotor2")
    newLetter = newLetter + rotorPosDif
    newLetter = rationalise_newLetter(newLetter)
    newLetter = rotor_3.get(newLetter) 
    
    global newLetterCharacter
    newLetterCharacter = chr(newLetter + 97)

def reflect_letter():
    #Runs the letter through the reflector
    global reflectedLetter
    reflectedLetter = reflector.get(newLetterCharacter)


def encode_letter_backwards():
    #This function runs the letter through rotors backwards

    letterNumber = ord(reflectedLetter) - 97

    newLetter = rotor_3_b.get(letterNumber)
    rotorPosDif = rotorPosition.get("rotor2") - rotorPosition.get("rotor3") 
    newLetter = newLetter + rotorPosDif
    newLetter = rationalise_newLetter(newLetter)
    newLetter = rotor_2_b.get(newLetter)
    rotorPosDif = rotorPosition.get("rotor1") - rotorPosition.get("rotor2")
    newLetter = newLetter + rotorPosDif
    newLetter = rationalise_newLetter(newLetter)
    newLetter = rotor_1_b.get(newLetter) 
    
    newLetterCharacter = chr(newLetter + 97)
    newList.append(newLetterCharacter)

def rationalise_newLetter(newLetter):
    #Must be 26, not 25 to account for the fact that a = 0, not 1
    if newLetter > 25:
        newLetter = newLetter - 26
    if newLetter < 0:
        newLetter = newLetter + 26
    return newLetter


def write_message():
    #opens encoded_message_here.txt
    #deletes all content in file
    #writes new message to file
    global newList
    newList = ''.join(str(x) for x in newList)
    with open("encoded_message_here.txt", "a") as f:
        f.truncate(0)
        f.write(newList)
    print("encoded file written")
    print(newList)
    

def run():
    #This function runs the file when called
    
    access_text_file()

    global letter
    l = list(message)
    
    for letter in l:
        encode_letter_forwards()
        reflect_letter()
        encode_letter_backwards()
        increment_rotor_position()

    write_message()


run()














