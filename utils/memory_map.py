'''
Tool for working with memory maps
'''

import sys

def main():
    ''' Main function, responsible for parsing args and running the appropriate tool. '''
    if len(sys.argv) < 3:
        print('Usage:')
        print('-d   Find duplicate functions.')
        print('-l   Map length check.')
        print('-v   Check the memory map for validity.')
        print('-z   Find functions that still are unidentified.')
        print('Example:')
        print('python memory_map.py -l RNEEDA.map')
        sys.exit(0)
    arg = sys.argv[1]
    if arg == '-d':
        find_duplicates()
    elif arg == '-l':
        map_length_check()
    elif arg == '-v':
        is_map_valid()
    elif arg == '-z':
        find_unidentified_functions()
    else:
        print('Unknown argument: ' + arg)
        sys.exit(1)
    sys.exit(0)

def find_duplicates():
    ''' Finds duplicate functions. '''
    map_file = sys.argv[2]
    with open('../general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    all_functions = []
    for count, line in enumerate(lines):
        if len(line) > 29:
            function = line[29:-1]
            if function in all_functions:
                print(f'Found: "{function}" on line {count}')
            all_functions.append(function)

def map_length_check():
    '''
    Checks the length of each function in the symbol map and prints which ones may be incorrect.
    The reason that some lengths are incorrect is because they may contain a branch that shouldn't
    count for the function length, but did count when Dolphin automatically generated the symbol
    map. It accomplished this by counting the difference in bytes between the start and end
    of the function.
    '''
    map_file = sys.argv[2]
    with open('../general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    previous = []
    for _, line in enumerate(lines):
        parts = line.split(' ')
        if line.startswith('8'):
            addr = int(parts[0], 16)
            if previous:
                previous_length = int(previous[1], 16)
                previous_addr = int(previous[0], 16)
                diff = addr - previous_addr
                if diff < previous_length:
                    print('Function: {} ({:02X})'.format(previous[4].strip(), previous_addr))
                    print('  Expected: {:02X} Actual: {:02X}'.format(previous_length, diff))
            previous = parts

def is_map_valid():
    ''' Checks that the given memory map file is a valid memory map. '''
    # Check that the address in the 1st and 3rd spot of each line match
    map_file = sys.argv[2]
    with open('../general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    for count, line in enumerate(lines):
        parts = line.split(' ')
        if line.startswith('8'):
            first = parts[0]
            second = parts[2]
            if first != second:
                print('Not equal on line ' + str(count + 1))

def find_unidentified_functions():
    ''' Print out the functions that have yet to be identified (named). '''
    map_file = sys.argv[2]
    with open('../general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    for line in lines:
        if len(line) > 31 and line[29:32] == 'zz_':
            print('Found ' + line[29:-1])

if __name__ == "__main__":
    main()
