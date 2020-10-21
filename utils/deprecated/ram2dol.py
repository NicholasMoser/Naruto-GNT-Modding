# Convert address from RAM while the game is running to address in Start.dol 
import sys

input = int(sys.argv[1], 16)
output = input - 0x80003000
print('%0X' % output)