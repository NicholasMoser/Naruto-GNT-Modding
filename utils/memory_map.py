# Tool for working with memory maps

import sys

def main():
    if (len(sys.argv) < 3):
        print('Usage:')
        print('-v   Check the memory map for validity.')
        print('-l   Map length check.')
        print('Example:')
        print('python memory_map.py -l RNEEDA.map')
        sys.exit(0)
    arg = sys.argv[1]
    if (arg == '-v'):
        is_map_valid(sys.argv[2])
    elif (arg == '-l'):
        map_length_check(sys.argv[2])
    else:
        print('Unknown argument: ' + arg)
        sys.exit(1)
    sys.exit(0)

def is_map_valid(map_file):
    ''' Checks that the given memory map file is a valid memory map. '''
    # Check that the address in the 1st and 3rd spot of each line match
    with open('../general/symbol_maps/' + map_file, 'r') as f:
        lines = f.readlines()
    for count, line in enumerate(lines):
        parts = line.split(' ')
        if line.startswith('8'):
            first = parts[0]
            second = parts[2]
            if first != second:
                print('Not equal on line ' + str(count + 1))

def map_length_check(map_file):
    with open('../general/symbol_maps/' + map_file, 'r') as f:
        lines = f.readlines()
    previous = []
    for _, line in enumerate(lines):
        parts = line.split(' ')
        if line.startswith('8'):
            addr = int(parts[0], 16)
            if (previous):
                previousLength = int(previous[1], 16)
                previousAddr = int(previous[0], 16)
                diff = addr - previousAddr
                if (diff < previousLength):
                    print('Function: {} ({:02X})'.format(previous[4].strip(), previousAddr))
                    print('  Expected: {:02X} Actual: {:02X}'.format(previousLength, diff))
            previous = parts

if __name__ == "__main__":
    main()
