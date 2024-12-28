#!/usr/bin/env python

import sys
import json

input = " ".join(sys.argv).lower()

alphabet = {"a":0,
            "b":0,
            "c":0,
            "d":0,
            "e":0,
            "f":0,
            "g":0,
            "h":0,
            "i":0,
            "j":0,
            "k":0,
            "l":0,
            "m":0,
            "n":0,
            "o":0,
            "p":0,
            "q":0,
            "r":0,
            "s":0,
            "t":0,
            "u":0,
            "v":0,
            "w":0,
            "x":0,
            "y":0,
            "z":0,
            "ß":0,
            "ä":0,
            "ö":0,
            "ü":0,
            "1":0,
            "2":0,
            "3":0,
            "4":0,
            "5":0,
            "6":0,
            "7":0,
            "8":0,
            "9":0,
            "0":0,
            }
for key in alphabet.keys():
    alphabet[key] = input.count(key)

json_object = json.dumps(alphabet, indent=4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)
