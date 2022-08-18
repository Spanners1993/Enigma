# This file will take a message/encrypted message, run it through the rotors/reflector and make it into encrypted message/message.
# Will have to:
# 1) Get message
# 2) Run one letter through rotor/reflector encryption
# 3) Increment rotor position
# 3) Repeat steps 2 + 3 until message is fully encrypted
# 4) Write message to text file.

from rotors import rotorPosition, reflector, rotor_one, rotor_two, rotor_three
# NOTE:  The rotorPosition variable will change as this file runs. The new rotor position will not be saved to the rotors module. 


newList = []

def access_text_file():
    #opens the file
    #creates a file object (f)
    #reads the file object
    #creates the global "message" variable using the file object
    #uses 'with' because this ensures file is shut when we are done with it
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

    newLetter = rotor_one.wiring.get(letterNumber)
    rotorPosDif = rotorPosition.get("rotor2") - rotorPosition.get("rotor1")
    newLetter = newLetter + rotorPosDif
    newLetter = rationalise_newLetter(newLetter)
    newLetter = rotor_two.wiring.get(newLetter)
    rotorPosDif = rotorPosition.get("rotor3") - rotorPosition.get("rotor2")
    newLetter = newLetter + rotorPosDif
    newLetter = rationalise_newLetter(newLetter)
    newLetter = rotor_three.wiring.get(newLetter) 
    
    global newLetterCharacter
    newLetterCharacter = chr(newLetter + 97)

def reflect_letter():
    #Runs the letter through the reflector
    global reflectedLetter
    reflectedLetter = reflector.get(newLetterCharacter)


def encode_letter_backwards():
    #This function runs the letter through rotors backwards

    letterNumber = ord(reflectedLetter) - 97

    newLetter = rotor_three.reverse_wiring.get(letterNumber)
    rotorPosDif = rotorPosition.get("rotor2") - rotorPosition.get("rotor3") 
    newLetter = newLetter + rotorPosDif
    newLetter = rationalise_newLetter(newLetter)
    newLetter = rotor_two.reverse_wiring.get(newLetter)
    rotorPosDif = rotorPosition.get("rotor1") - rotorPosition.get("rotor2")
    newLetter = newLetter + rotorPosDif
    newLetter = rationalise_newLetter(newLetter)
    newLetter = rotor_one.reverse_wiring.get(newLetter) 
    
    newLetterCharacter = chr(newLetter + 97)
    newList.append(newLetterCharacter)

def rationalise_newLetter(newLetter):
    #a=0, b=1 etc. This ensures the addition/subraction operations taking place in the encode_xxx functions
    #can't lead to a number >25 or <0 being passed back into the rotors
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
    #This function runs the file when called. Cycles through each letter in message.
    
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














