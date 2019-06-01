'''
Replaces a character select screen animation file with an animation file
from battle animations. Simply run the script with quickbms.exe, naruto_mot.bms,
0000.mot, and 0001.mot in the same directory. It will then list all of the
animation identifiers in 0000.mot that are smaller than the idle animation
in 0001.mot. Because they are smaller, they can be replaced without issue.
Simply input the number and it will modify 0001.mot for you.
'''
import os
import subprocess
import shutil
import sys

QUICK_BMS = 'quickbms.exe'
MOT_BMS = 'naruto_mot.bms'
MOT_0000 = '0000.mot'
MOT_0001 = '0001.mot'
FILES_0000 = '0000'
FILES_0001 = '0001'

# Check that files exist
if not os.path.isfile(QUICK_BMS):
    print('{} not found.'.format(QUICK_BMS))
    sys.exit(1)
if not os.path.isfile(MOT_BMS):
    print('{} not found.'.format(MOT_BMS))
    sys.exit(1)
if not os.path.isfile(MOT_0000):
    print('{} not found.'.format(MOT_0000))
    sys.exit(1)
if not os.path.isfile(MOT_0001):
    print('{} not found.'.format(MOT_0001))
    sys.exit(1)

# Unpack .mot files into .gnta files
subprocess.run([QUICK_BMS, '-Y', '-Q', MOT_BMS, MOT_0000, FILES_0000])
subprocess.run([QUICK_BMS, '-Y', '-Q', MOT_BMS, MOT_0001, FILES_0001])

# List animations in the .gnta files for 0000.mot
original_file = os.path.join(FILES_0001, '0.gnta')
original_size = os.path.getsize(original_file)
mot_files = [int(mot_file.split('.')[0]) for mot_file in os.listdir(FILES_0000)]

# User input animation will replace 0001.mot from 0000.mot
animation = input('\nPlease select a number from 0 to {} inclusive: '.format(max(mot_files)))
animation_file = os.path.join(FILES_0000, '{}.gnta'.format(animation))
if not os.path.isfile(animation_file):
    print('{} not found.'.format(animation_file))
    sys.exit(1)
shutil.copy(animation_file, original_file)

# We must use force in order to repack a large file into the motion archive.
# This is okay to do since 0001.mot only contains a single animation.
p = subprocess.run([QUICK_BMS, '-r', '-w', '-Y', '-Q', 'naruto_mot.bms', MOT_0001, FILES_0001],
                   stdout=subprocess.PIPE,
                   input='force',
                   encoding='ascii')

shutil.rmtree(FILES_0000)
shutil.rmtree(FILES_0001)
print('Done.')
