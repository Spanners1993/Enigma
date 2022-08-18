#Contains the rotor and rotor position information

rotorPosition = { 

    "rotor1" : 12,
    "rotor2" : 7,
    "rotor3" : 9
}

class rotors:
    def __init__(self, wiring):
        self.wiring = wiring
        self.convert_to_dictionary()
        self.reverse_dictionary()
        
    def convert_to_dictionary(self):
        #This function takes the string of letters and converts it into a dictionary 
        newList = []
        numbers = list(range(26))
        letters = list(self.wiring)
        for eachLetter in letters:
            newNumber = ord(eachLetter) - 65 
            newList.append(newNumber)
        letters = newList
        dictionary = list(zip(numbers, letters))
        self.wiring = dict(dictionary)
        return self.wiring

    def reverse_dictionary(self):
        #This function creates a new dictionary with the keys and values swapped using the output from the function above
        self.reverse_wiring = {v: k for k, v in self.wiring.items()}
        return self.reverse_wiring
        
rotor_one = rotors('DMTWSILRUYQNKFEJCAZBPGXOHV')
rotor_two = rotors('HQZGPJTMOBLNCIFDYAWVEUSRKX')
rotor_three = rotors('UQNTLSZFMREHDPXKIBVYGJCWOA')


reflector = {

    "a" : "q",
    "b" : "y",
    "c" : "h",
    "d" : "o",
    "e" : "g",
    "f" : "n",
    "g" : "e",
    "h" : "c",
    "i" : "v",
    "j" : "p",
    "k" : "u",
    "l" : "z",
    "m" : "t",
    "n" : "f",
    "o" : "d",
    "p" : "j",
    "q" : "a",
    "r" : "x",
    "s" : "w",
    "t" : "m",
    "u" : "k",
    "v" : "i",
    "w" : "s",
    "x" : "r",
    "y" : "b",
    "z" : "l",
}
