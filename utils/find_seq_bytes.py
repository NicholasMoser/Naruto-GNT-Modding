'''
Find which seq files contain a specific pattern of bytes
'''
import sys
import os
from bitstring import ConstBitStream

def main():
    # Get arguments and check for validity
    args = len(sys.argv)
    if (args == 1):
        print('Usage: python find_seq_bytes.py {path to seq files} {bytes in hex}')
        print('Example: python find_seq_bytes.py C:/GNT4 04027000000000683f0000000000c001')
        sys.exit(0)
    elif (args != 3):
        print('Please include both a path to your seq files and the bytes in hex')
        sys.exit(1)
    path = sys.argv[1]
    if (not(os.path.isdir(path))):
        print(path + ' is not a valid directory')
        sys.exit(1)
    byte_array = bytearray.fromhex(sys.argv[2])

    # Find and print files
    for root, _, files in os.walk(path):
        for cur_file in files:
            if cur_file.endswith('.seq'):
                file_path = os.path.join(root, cur_file)
                check_file(file_path, byte_array)

def check_file(file_path, byte_array):
    s = ConstBitStream(filename=file_path)
    found = s.find(byte_array, bytealigned=True)
    if found:
        print("File: %s" % file_path)
        print("Found start code at byte offset %d." % found[0])
        s0f0, length, bitdepth, height, width = s.readlist('hex:16, uint:16, uint:8, 2*uint:16')
        print("Width %d, Height %d\n" % (width, height))

if __name__ == "__main__":
    main()