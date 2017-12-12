"""
Wikipedia Quiz
Unpacks a FPK file or directory of FPK files from the Naruto GNT series.
Only works with Python 3.2+
Written by Nicholas Moser. NicholasMoser56@gmail.com www.github.com/NicholasMoser
"""
import os
import argparse
import binascii
import codecs

parser = argparse.ArgumentParser(description='Unpack FPK files.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--file', type=argparse.FileType('rb'), help='FPK file to unpack.')
group.add_argument('-d', '--directory', help='Directory of FPK files to unpack.')

def main():
    ''' Unpack an FPK file or directory of FPK files. '''
    args = parser.parse_args()
    fpk_file = args.file
    if fpk_file is None:
        directory = args.directory
        files = [file for file in next(os.walk(directory))[2] if file.endswith('.fpk')]
        for file in files:
            file_path = os.path.join(directory, file)
            fpk_file = open(file_path, 'rb')
            unpack_fpk(fpk_file)
    else:
        unpack_fpk(fpk_file)

def unpack_fpk(fpk_file):
    ''' Unpacks a single FPK file. '''
    current_byte = 0
    header, current_byte = read_fpk_header(fpk_file, current_byte)
    files, current_byte = read_file_headers(fpk_file, header['number_of_files'], current_byte)
    for file_header in files:
        start_byte = file_header['offset']
        if current_byte < start_byte:
            empty_bytes = start_byte - current_byte
            print('{} padding bytes found. Skipping...'.format(empty_bytes))
            fpk_file.read(empty_bytes)
            current_byte += empty_bytes
        file_size = file_header['size']
        data = fpk_file.read(file_size)
        current_byte += file_size
        write_file(data, file_header['name'])
    print('Ended at byte {}'.format(current_byte))
    fpk_file.close()

def read_fpk_header(fpk_file, current_byte):
    ''' Read and return the first 16 bytes that describe the FPK file itself. '''
    header = {}
    header['file_int'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    header['number_of_files'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    header['string_entry_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    header['file_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    current_byte += 16
    print('Begin to unpack fpk file: {}'.format(fpk_file.name))
    print('File int: {}'.format(header['file_int']))
    print('Number of files: {}'.format(header['number_of_files']))
    print('String entry size: {}'.format(header['string_entry_size']))
    print('File size: {}\n'.format(header['file_size']))
    return header, current_byte

def read_file_headers(fpk_file, number_of_files, current_byte):
    ''' Read and return the headers of each file contained in the FPK file. '''
    files = []
    for _ in range(number_of_files):
        file = {}
        name_value = binascii.hexlify(fpk_file.read(16))
        file['name'] = codecs.decode(name_value, 'hex').decode('utf-8')[:-1]
        file['null_value'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file['offset'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file['size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file['unknown'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        files.append(file)
        current_byte += 32
        print('Found file: {}'.format(file['name']))
        print('Null value: {}'.format(file['null_value']))
        print('Offset: {}'.format(file['offset']))
        print('Size: {}'.format(file['size']))
        print('Unknown: {}\n'.format(file['unknown']))
    return files, current_byte

def write_file(data, file_name):
    ''' Write binary data to file_name. '''
    split_path = file_name.split('/')
    if not os.path.exists(split_path[1]):
        os.makedirs(split_path[1])
    full_path = os.path.join(split_path[1], split_path[2])
    if os.path.isfile(full_path):
        print('Ignoring {}; file already exists.'.format(full_path))
    else:
        with open(full_path, 'wb') as file:
            file.write(data)

main()
