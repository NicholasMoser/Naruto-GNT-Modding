'''
Unpack all .mot files in a directory.
'''
import struct
import sys
import os

def main():
    if len(sys.argv) != 2:
        print('Please provide a path to GNT4 files.')
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(directory + ' is not a valid directory.')
        sys.exit(1)
    for root, _, files in os.walk(directory):
        for cur_file in files:
            if cur_file.endswith('.mot'):
                file_path = os.path.join(root, cur_file)
                output_dir = file_path.replace('.mot', '')
                if not os.path.isdir(output_dir):
                    os.mkdir(output_dir)
                unpack(file_path, output_dir)

def unpack(path, output):
    ''' From https://github.com/mitchellhumphrey/MOT-Dumping-Tool/blob/v1.0/MOTTool.py '''
    mot = open(path, "rb")

    if not os.path.exists(output + "\\"):
        os.mkdir(output + "\\")

    header = struct.unpack(">iiii", mot.read(16))

    list = []
    indexDict = {}

    list.append(header[3])
    indexDict[header[3]] = -1

    for j in range(header[1]):
        off = struct.unpack(">i", mot.read(4))[0]
        if off != 0:
            list.append(off)
            indexDict[off] = j

    print("Extracted " + str(len(list)) + " animations")

    list.sort()

    for i in range(len(list) - 1):
        indexName = '0x{0:0{1}X}'.format(indexDict[list[i]], 4)
        mot.seek(list[i])
        with open(output + "\\" + indexName + ".gnta", 'wb') as f:
            f.write(mot.read(list[i + 1] - list[i]))

    mot.close()

    # Write out the total number of animation ids
    with open(output + '/totalAnimationIds', 'w') as totalAnimationIds:
        totalAnimationIds.write(str(header[1]))

if __name__ == "__main__":
    main()
