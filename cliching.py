#!/usr/bin/python3
# # -*- coding: utf-8 -*-

import random
import json
import os

class Color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Color:
    """Class for terminal color codes."""
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Line:
    """Class for generating and converting hexagram lines."""

    @classmethod
    def intro(cls):
        """Clears the terminal and generates a hexagram."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╭━━━┳╮╱╭━━━┳╮")
        print ("┃╭━╮┃┃╱┃╭━╮┃┃")
        print ("┃┃╱╰┫┃╭┫┃╱╰┫╰━┳┳━╮╭━━╮")
        print ("┃┃╱╭┫┃┣┫┃╱╭┫╭╮┣┫╭╮┫╭╮┃")
        print ("┃╰━╯┃╰┫┃╰━╯┃┃┃┃┃┃┃┃╰╯┃")
        print ("╰━━━┻━┻┻━━━┻╯╰┻┻╯╰┻━╮┃")
        print ("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃")
        print ("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯")
        print('─' * 20)
        cls.generate_hexagram()

    @classmethod
    def cointoss(cls):
        """Tosses a coin and returns a result."""
        return random.choice([3, 2])

    @classmethod
    def generate_line(cls):
        """Prompts the user to press Enter and then generates a line."""
        input("Premi Invio per lanciare le monete.")
        return cls.cointoss() + cls.cointoss() + cls.cointoss()
    
    _hexagrams = None

    @staticmethod
    def load_hexagrams():
        """Loads the hexagrams in a class attribute."""
        try:
            with open('hexagrams.json') as f:
                Line._hexagrams = json.load(f)
        except IOError:
            print("Error opening 'hexagrams.json' file")
            Line._hexagrams = {}
        except ValueError:
            print("Error parsing JSON data")
            Line._hexagrams = {}

    @staticmethod
    def locate_hexagram(hex_pattern):
        if Line._hexagrams is None:
            Line.load_hexagrams()
        int_hex = int(hex_pattern)
        found = next((d for d in Line._hexagrams['hexagrams'] if d['pattern'] == int_hex), {})
        return found


    @staticmethod
    def log_format(hex_type, transforming_lines):
        """Prints out the hexagram information for the given hexagram pattern."""
        result = Line.locate_hexagram(hex_type)
        if not result:  # Check if the result dictionary is empty
            print("Esagramma non trovato")
            return
        print("   ", result['name']['zh'], "   ")
        print(Color.BOLD + "Esagramma", str(result['number']) + ":", result['name']['it'], Color.END)
        print("   ", result['symbol'], "   ")
        print(Color.UNDERLINE + "La Sentenza:" + Color.END)
        print(result['judgment'])
        print(Color.UNDERLINE + "Immagine:" + Color.END)
        print(result['image'])
        if transforming_lines:
            print(Color.UNDERLINE + "Linee Mobili:" + Color.END)
            for x in transforming_lines:
                print(result['transforming_lines'][x])
        print("\n")


    @classmethod
    def convert_hexagrams(cls, hexagram):
        """Converts a hexagram to its changing and relating hexagrams, if applicable."""
        changing = False
        primary = ""
        relating = ""
        transforming_lines = []
        for i in range(len(hexagram)):
            if hexagram[i] == "6":
                changing = True
                primary += str(8)
                relating += str(7)
                transforming_lines.append(i)
            elif hexagram[i] == "9":
                changing = True
                primary += str(7)
                relating += str(8)
                transforming_lines.append(i)
            else:
                primary += hexagram[i]
                relating += hexagram[i]
        os.system('cls' if os.name == 'nt' else 'clear')
        if changing:
            Line.log_format(primary, transforming_lines)
            Line.log_format(relating, transforming_lines)
        else:
            Line.log_format(primary, transforming_lines)

    @classmethod
    def generate_hexagram(cls):
        """Generates a hexagram by tossing coins six times and converting the resulting lines."""
        hexagram = []
        for i in range(6):
            line = str(cls.generate_line())  # convert the result to a string before appending it to the hexagram list
            hexagram.append(line)
        print("\n")
        hexagram = "".join(hexagram)  # join the elements of the hexagram list into a single string
        cls.convert_hexagrams(hexagram)

if __name__ == "__main__":
    Line.intro()