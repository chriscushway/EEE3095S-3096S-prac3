
# Define files
goldenFile = open("goldenResult.txt", "r")
bit64File = open("../C/hetrodyning64bit1Thread.txt", "r")
bit32File = open("../C/hetrodyning32bit1Thread.txt", "r")
bit16File = open("../C/hetrodyning16bit1Thread.txt", "r")
# Define data structures

golden = []
bit64  = []
bit32  = []
bit16  = []
report = {} 

# Main function
def main():
    readFromFileToArray(golden, goldenFile)
    readFromFileToArray(bit64, bit64File)
    readFromFileToArray(bit32, bit32File)
    readFromFileToArray(bit16, bit16File)
    print("Running accuracy test of using double in c program (64bits) \n")
    compareArrays(golden, bit64)
    print("Running accuracty test for using float in c program (32bits) \n")
    compareArrays(golden, bit32)
    print("Running accuracy test for using float in c program (16bits) \n")
    compareArrays(golden, bit16)

# function passes by reference
def readFromFileToArray(array, file):
    lines = file.readlines()
    for line in lines:
        array.append(float(line))

def compareArrays(array1, array2):
    falseCount = 0
    trueCount = 0
    for i in range(len(array1)):
        if(array1[i] == array2[i]):
            trueCount += 1
        else:
            falseCount += 1
            compareFloatAccuracy(str(array1[i]), str(array2[i]))
    if (falseCount > 0):
        print("The results were not as accurate as the golden standard having " + str(falseCount) + " values not being correct \n")
        printReport()
        report.clear()
    else:
        print("All results were accurate \n")

def compareFloatAccuracy(float1, float2):
    accuracyCount = 0
    count = 0
    measureDecimals = False
    while count < len(float1) and float1[count] == float2[count]:
        if (float1[count] != '.' and measureDecimals):
            accuracyCount += 1
        else:
            if (float1[count] == '.'):
                measureDecimals = True 
        count += 1

    if (accuracyCount in report):
	report[accuracyCount] += 1
    else:
        report[accuracyCount] = 1

def printReport():
    for key, value in report.items():
        print("There were " + str(value) + " value(s) that were accurate to " + str(key) +  " decimal places \n")

# Only run the functions if this module is run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))
