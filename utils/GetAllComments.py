#Get all comments for this binary from the starting address to 0x80280000
#@author Nicholas Moser
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 

def getAddress(offset):
    return currentProgram.getAddressFactory().getDefaultAddressSpace().getAddress(offset)

addr = currentProgram.getMemory().getMinAddress().offset
itr = 0
while addr < 0x80280000:
    try:
        comment = getPlateCommentAsRendered(getAddress(addr))
        print('Plate: {:08x}'.format(addr))
        print(comment + '\n')
    except:
        pass
    try:
        comment = getPreCommentAsRendered(getAddress(addr))
        print('Pre: {:08x}'.format(addr))
        print(comment + '\n')
    except:
        pass
    try:
        comment = getPlateCommentAsRendered(getAddress(addr))
        print('Plate: {:08x}'.format(addr))
        print(comment + '\n')
    except:
        pass
    addr += 4
print('Done')
