import subprocess

testCoordinate = (538, -208)
testSystem = "X1-YC38"

subprocess.run(['python', 'map.py', str(testCoordinate[0]), str(testCoordinate[1])])

subprocess.run(['python', 'map.py', testSystem])

