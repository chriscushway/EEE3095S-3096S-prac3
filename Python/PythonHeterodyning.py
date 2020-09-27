#!/usr/bin/python3
"""
Python Practical Code for heterodyning and performance testing
Keegan Crankshaw
Date: 7 June 2019

This isn't necessarily performant code, but it is Pythonic
This is done to stress the differences between Python and C/C++

"""

# import Relevant Librares
import sys,Timing
from data import carrier, data

# Define values.
c = carrier
d = data
result = []

outputFile = open("goldenResult.txt", "w")

# Main function
def main():
    print("There are {} samples".format(len(c)))
    print("using type {}".format(type(data[0])))
    Timing.startlog()
    for i in range(len(c)):
        result.append(c[i] * d[i])
    Timing.endlog()
def writeToFile():
    for item in result:
       outputFile.write(str(item) + "\n")
    outputFile.close()

# Only run the functions if this module is run
if __name__ == "__main__":
    try:
        main()
        print("Writing to output file")
        writeToFile()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))
