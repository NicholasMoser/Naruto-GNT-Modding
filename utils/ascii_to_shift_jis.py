'''
NOTE: This file is now deprecated. Please use the GNT Hex Editor instead: https://github.com/NicholasMoser/hexeditor

ASCII to Shift JIS
Convert standard ASCII characters to Big Endian Shift JIS hex.
Only works with Python 3.0+
Written by Nicholas Moser. NicholasMoser56@gmail.com www.github.com/NicholasMoser
'''
import argparse
from gooey import Gooey, GooeyParser

@Gooey()
def main():
    ''' Run GUI for program '''
    parser = GooeyParser(description='Convert ASCII to big endian Shift JIS hex.')

    parser.add_argument(
        'text',
        metavar='Insert Text',
        help='Example: ')

    parser.add_argument(
        '-c', '--count',
        metavar='Count Shift JIS characters',
        action='store_true',
        help='I want to count characters in Shift JIS bytes instead (make sure it starts with 00 00)')

    args = parser.parse_args()
    if args.count:
        count_characters_in_hex(args.text)
    else:
        ascii_to_shift_jis(args.text)
    print('\n\n---------------')

def count_characters_in_hex(text):
    '''
    Given shift-jis hex, count the number of characters.
    Example: 00 00 46 81 00 00 00 0A would be two.
    '''
    length = (len(text) + 1) // 12
    print('{0} characters long.'.format(length))

def ascii_to_shift_jis(text):
    '''
    Convert main English characters to big endian shift-jis.
    Instead of trying to do some weird mapping, why not just brute force it?
    This dictionary maps all of the important characters.
    \n is a newline, and \\ is the end command.
    '''
    print('Text: {}\n'.format(text))
    charmap = {}
    charmap['\n'] = '00 0A'
    charmap['\\'] = '00 1A'
    charmap[' '] = '40 81'
    charmap[','] = '43 81'
    charmap['.'] = '44 81'
    charmap[':'] = '46 81'
    charmap[';'] = '47 81'
    charmap['?'] = '48 81'
    charmap['!'] = '49 81'
    charmap['"'] = '4e 81'
    charmap["'"] = '65 81'
    charmap['('] = '69 81'
    charmap[')'] = '6a 81'
    charmap['['] = '6d 81'
    charmap[']'] = '6e 81'
    charmap['{'] = '6f 81'
    charmap['}'] = '70 81'
    charmap['+'] = '7b 81'
    charmap['-'] = '7c 81'
    charmap['<'] = '83 81'
    charmap['>'] = '84 81'
    charmap['%'] = '93 81'
    charmap['#'] = '94 81'
    charmap['&'] = '95 81'
    charmap['*'] = '96 81'
    charmap['@'] = '97 81'
    charmap['0'] = '4f 82'
    charmap['1'] = '50 82'
    charmap['2'] = '51 82'
    charmap['3'] = '52 82'
    charmap['4'] = '53 82'
    charmap['5'] = '54 82'
    charmap['6'] = '55 82'
    charmap['7'] = '56 82'
    charmap['8'] = '57 82'
    charmap['9'] = '58 82'
    charmap['A'] = '60 82'
    charmap['B'] = '61 82'
    charmap['C'] = '62 82'
    charmap['D'] = '63 82'
    charmap['E'] = '64 82'
    charmap['F'] = '65 82'
    charmap['G'] = '66 82'
    charmap['H'] = '67 82'
    charmap['I'] = '68 82'
    charmap['J'] = '69 82'
    charmap['K'] = '6A 82'
    charmap['L'] = '6B 82'
    charmap['M'] = '6C 82'
    charmap['N'] = '6D 82'
    charmap['O'] = '6E 82'
    charmap['P'] = '6F 82'
    charmap['Q'] = '70 82'
    charmap['R'] = '71 82'
    charmap['S'] = '72 82'
    charmap['T'] = '73 82'
    charmap['U'] = '74 82'
    charmap['V'] = '75 82'
    charmap['W'] = '76 82'
    charmap['X'] = '77 82'
    charmap['Y'] = '78 82'
    charmap['Z'] = '79 82'
    charmap['a'] = '81 82'
    charmap['b'] = '82 82'
    charmap['c'] = '83 82'
    charmap['d'] = '84 82'
    charmap['e'] = '85 82'
    charmap['f'] = '86 82'
    charmap['g'] = '87 82'
    charmap['h'] = '88 82'
    charmap['i'] = '89 82'
    charmap['j'] = '8A 82'
    charmap['k'] = '8B 82'
    charmap['l'] = '8C 82'
    charmap['m'] = '8D 82'
    charmap['n'] = '8E 82'
    charmap['o'] = '8F 82'
    charmap['p'] = '90 82'
    charmap['q'] = '91 82'
    charmap['r'] = '92 82'
    charmap['s'] = '93 82'
    charmap['t'] = '94 82'
    charmap['u'] = '95 82'
    charmap['v'] = '96 82'
    charmap['w'] = '97 82'
    charmap['x'] = '98 82'
    charmap['y'] = '99 82'
    charmap['z'] = '9A 82'
    for character in text:
        bytestring = charmap.get(character)
        if bytestring is not None:
            print('00 00 {0} '.format(bytestring), end='')

if __name__ == '__main__':
    main()
