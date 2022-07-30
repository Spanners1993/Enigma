#Contains the rotor and rotor position information

rotorPosition = { 

    "rotor1" : 12,
    "rotor2" : 7,
    "rotor3" : 9
}

class rotors:
    def __init__(self, wiring):
        self.wiring = wiring
        self.convert_to_dictionary(wiring)
        self.reverse_dictionary()
        
    def convert_to_dictionary(self, wiring):
        newList = []
        numbers = list(range(25))
        letters = list(wiring)
        for eachLetter in letters:
            newNumber = ord(eachLetter) - 65 
            newList.append(newNumber)
        letters = newList
        dictionary = list(zip(numbers, letters))
        self.wiring = dict(dictionary)
        return self.wiring

    def reverse_dictionary():
        #This function needs to take the dictionary created above and reverse it
        pass
        
rotor_one = rotors('DMTWSILRUYQNKFEJCAZBPGXOHV')
rotor_two = rotors('XXX')

print(rotor_one.wiring)


rotor_1 = {

0 : 3,
1 : 12,
2 : 19,
3 : 22,
4 : 18,
5 : 8,
6 : 11,
7 : 17,
8 : 20,
9 : 24,
10 : 16,
11 : 13,
12 : 10,
13 : 5,
14 : 4,
15 : 9,
16 : 2,
17 : 0,
18 : 25,
19 : 1,
20 : 15,
21 : 6,
22 : 23,
23 : 14,
24 : 7,
25 : 21,

}

rotor_2 = {

0 : 7,
1 : 16,
2 : 25,
3 : 6,
4 : 15,
5 : 9,
6 : 19,
7 : 12,
8 : 14,
9 : 1,
10 : 11,
11 : 13,
12 : 2,
13 : 8,
14 : 5,
15 : 3,
16 : 24,
17 : 0,
18 : 22,
19 : 21,
20 : 4,
21 : 20,
22 : 18,
23 : 17,
24 : 10,
25 : 23,

}

rotor_3 = {

0 : 20,
1 : 16,
2 : 13,
3 : 19,
4 : 11,
5 : 18,
6 : 25,
7 : 5,
8 : 12,
9 : 17,
10 : 4,
11 : 7,
12 : 3,
13 : 15,
14 : 23,
15 : 10,
16 : 8,
17 : 1,
18 : 21,
19 : 24,
20 : 6,
21 : 9,
22 : 2,
23 : 22,
24 : 14,
25 : 0,

}

rotor_1_b = {

0 : 17,
1 : 19,
2 : 16,
3 : 0,
4 : 14,
5 : 13,
6 : 21,
7 : 24,
8 : 5,
9 : 15,
10 : 12,
11 : 6,
12 : 1,
13 : 11,
14 : 23,
15 : 20,
16 : 10,
17 : 7,
18 : 4,
19 : 2,
20 : 8,
21 : 25,
22 : 3,
23 : 22,
24 : 9,
25 : 18,

}

rotor_2_b = {

0 : 17,
1 : 9,
2 : 12, 
3 : 15,
4 : 20,
5 : 14,
6 : 3,
7 : 0,
8 : 13,
9 : 5,
10 : 24,
11 : 10,
12 : 7,
13 : 11, 
14 : 8,
15 : 4,
16 : 1,
17 : 23,
18 : 22,
19 : 6,
20 : 21,
21 : 19,
22 : 18,
23 : 25,
24 : 16,
25 : 2,

}

rotor_3_b = {

0 : 25,
1 : 17,
2 : 22,
3 : 12,
4 : 10,
5 : 7,
6 : 20,
7 : 11,
8 : 16,
9 : 21,
10 : 15,
11 : 4,
12 : 8,
13 : 2,
14 : 24,
15 : 13,
16 : 1,
17 : 9,
18 : 5,
19 : 3,
20 : 0,
21 : 18,
22 : 23,
23 : 14,
24 : 19,
25 : 6,

}

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
