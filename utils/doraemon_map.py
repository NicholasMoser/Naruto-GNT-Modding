'''
Converts the symbol map from Doraemon Wii to one that can be read by Ghidra.
'''

import sys

def main():
    if len(sys.argv) != 3:
        print('Parameter 1: Doraemon Wii symbol map')
        print('Parameter 2: Output symbol map')
        sys.exit(1)
    path = sys.argv[1]
    out = sys.argv[2]
    with open(out, 'w', newline='\r\n') as output_file:
        with open(path, 'r') as mem_map:
            for line in mem_map.readlines():
                if ' 4 ' in line:
                    line = handle_parts(line)
                elif ' 1 ' in line or 'UNUSED' in line or line.startswith('  00'):
                    continue
                output_file.write(line)

def handle_parts(line):
    """ Break down a symbol down into parts understood by Ghidra. """
    parts = line.strip().split()
    virtual_addr = parts[2]
    type_flag = parts[4]
    if virtual_addr.startswith('8') and type_flag == '4':
        size = int(parts[1], 16)
        size_hex = '%08x' % size
        the_rest = line.split(' 4 ')[1].strip()
        return '{} {} {} 0 {}\n'.format(virtual_addr, size_hex, virtual_addr, the_rest)
    return line

if __name__ == "__main__":
    main()
