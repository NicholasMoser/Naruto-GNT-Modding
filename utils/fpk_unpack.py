"""
FPK Unpacker
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
group.add_argument('-f', '--file', help='FPK file to unpack.')
group.add_argument('-d', '--directory', help='Directory of FPK files to unpack.')

def main():
    ''' Unpack an FPK file or directory of FPK files. '''
    args = parser.parse_args()
    fpk_path = args.file
    if fpk_path is None:
        directory = args.directory
        files = [file for file in next(os.walk(directory))[2] if file.endswith('.fpk')]
        for file in files:
            fpk_path = os.path.join(directory, file)
            unpack_fpk(fpk_path)
    else:
        unpack_fpk(fpk_path)

def unpack_fpk(fpk_path):
    ''' Unpacks a single FPK file. '''
    with open(fpk_path, 'rb') as fpk_file:
        header = read_fpk_header(fpk_file)
        files = read_file_headers(fpk_file, header['file_count'])
        for file_header in files:
            start_byte = file_header['offset']
            if fpk_file.tell() < start_byte:
                empty_bytes = start_byte - fpk_file.tell()
                print('{} padding bytes found. Skipping...'.format(empty_bytes))
                fpk_file.read(empty_bytes)
            file_size = file_header['compressed_size']
            data = fpk_file.read(file_size)
            write_file(data, file_header['name'])
        print('Ended at byte {}'.format(fpk_file.tell()))

def read_fpk_header(fpk_file):
    ''' Read and return the first 16 bytes that describe the FPK file itself. '''
    header = {}
    header['null'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    header['file_count'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    header['header_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    header['file_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    print('Begin to unpack fpk file: {}'.format(fpk_file.name))
    print('File count: {}'.format(header['file_count']))
    print('File size: {}\n'.format(header['file_size']))
    return header

def read_file_headers(fpk_file, file_count):
    ''' Read and return the headers of each file contained in the FPK file. '''
    files = []
    for _ in range(file_count):
        file = {}
        name_value = binascii.hexlify(fpk_file.read(16))
        file['name'] = codecs.decode(name_value, 'hex').decode('utf-8')[:-1]
        file['null_value'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file['offset'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file['compressed_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file['uncompressed_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        files.append(file)
        print('Found file: {}'.format(file['name']))
        print('Offset: {}'.format(file['offset']))
        print('Compressed size: {}'.format(file['compressed_size']))
        print('Uncompressed size: {}\n'.format(file['uncompressed_size']))
    return files

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
