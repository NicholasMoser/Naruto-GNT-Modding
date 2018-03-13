"""
NOTE: This file should not be used anymore, as it does not decompress the files. Please use QuickBMS instead.

FPK Unpacker
Unpacks a FPK file or directory of FPK files from the Naruto GNT series.
Only works with Python 3.2+
Written by Nicholas Moser. NicholasMoser56@gmail.com www.github.com/NicholasMoser
"""
import os
import argparse

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
        fpk_header = read_fpk_header(fpk_file)
        file_headers = read_file_headers(fpk_file, fpk_header['file_count'])
        for file_header in file_headers:
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
    fpk_header = {}
    fpk_header['null'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    fpk_header['file_count'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    fpk_header['header_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    fpk_header['file_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
    print('Begin to unpack fpk file: {}'.format(fpk_file.name))
    print('File count: {}'.format(fpk_header['file_count']))
    print('File size: {}\n'.format(fpk_header['file_size']))
    return fpk_header

def read_file_headers(fpk_file, file_count):
    ''' Read and return the headers of each file contained in the FPK file. '''
    file_headers = []
    for _ in range(file_count):
        file_header = {}
        file_header['name'] = fpk_file.read(16).decode('utf-8').rstrip('\0')
        file_header['null_value'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file_header['offset'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file_header['compressed_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file_header['decompressed_size'] = int.from_bytes(fpk_file.read(4), byteorder='big')
        file_headers.append(file_header)
        print('Found file: {}'.format(file_header['name']))
        print('Offset: {}'.format(file_header['offset']))
        print('Compressed size: {}'.format(file_header['compressed_size']))
        print('decompressed size: {}\n'.format(file_header['decompressed_size']))
    return file_headers

def write_file(data, file_name):
    '''
    Write binary data to file_name.
    Files are in the form folder/.../file, and will save them as such.
    Example: hr/ank/0000.dat
    '''
    split_path = file_name.split('/')
    path = ''
    for folder in split_path[:-1]:
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = os.path.join(path, folder)
    file_path = os.path.join(path, split_path[-1])
    print(file_path)
    if os.path.isfile(file_path):
        print('Ignoring {}; file already exists.'.format(file_path))
    else:
        with open(file_path, 'wb') as file:
            file.write(data)

main()
