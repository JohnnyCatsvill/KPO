import os
from subprocess import run, PIPE

print("%Program Name% %Test File%")
arguments = [i for i in input().split()]

program = arguments[0]
testFile = open(arguments[1])

testData = testFile.read()
testFile.close()

for testCase in testData.split("\e"):
    testData = testCase.split("\n")
    if testData[0] == "":
        testData.pop(0)
        if testData[1] == "":
            testData[1] = "\n"
    programData = run(program, stdout=PIPE, input = testData[1], encoding="windows-1251")
    if testData[2] == programData.stdout.replace("\n", ""):
        print(testData[0], " success;")
    else:
        print(testData[0], " error; ", "expected - '", testData[2], "', actual - '", programData.stdout.replace("\n", ""), "'")
    
os.system("pause")
