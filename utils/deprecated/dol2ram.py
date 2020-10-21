# Convert address from Start.dol to address in RAM while the game is running
import sys

input = int(sys.argv[1], 16)
output = input + 0x80003000
print('%0X' % output)