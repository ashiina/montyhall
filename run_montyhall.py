#-----------
# Usage: 
# python run_montyhall.py (change_door= y|n) (tries= 1~...)
#-----------

import sys
import os
import random
import subprocess

# which door will be chosen
target = random.randint(0,2)
# whether to change door everytime (argv = 'y') or not
changeDoor = sys.argv[1]
# number of tries
numTries = int(sys.argv[2])

count = {'Correct':0, 'Wrong':0}
for i in range(0,numTries):
	print "%s" % i
	output = os.popen("python montyhall.py %s %s" % (target, changeDoor)).read()
	count[output.strip()] += 1

print count

