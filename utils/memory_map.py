'''
Tool for working with memory maps
'''

import sys

def main():
    ''' Main function, responsible for parsing args and running the appropriate tool. '''
    if len(sys.argv) < 3:
        print('Usage:')
        print('-c   Clean up functions.')
        print('-d   Find duplicate functions.')
        print('-l   Map length check.')
        print('-ll  Map length fix.')
        print('-o   Find functions without objects.')
        print('-s   Find locations where the object has been switched/changed.')
        print('-v   Check the memory map for validity.')
        print('-z   Find functions that still are unidentified.')
        print('Example:')
        print('python memory_map.py -l RNEEDA.map')
        sys.exit(0)
    arg = sys.argv[1]
    if arg == '-c':
        clean_up_functions()
    elif arg == '-d':
        find_duplicates()
    elif arg == '-l':
        map_length_check()
    elif arg == '-ll':
        map_length_fix()
    elif arg == '-o':
        find_missing_objects()
    elif arg == '-s':
        find_switched_objects()
    elif arg == '-v':
        is_map_valid()
    elif arg == '-z':
        find_unidentified_functions()
    else:
        print('Unknown argument: ' + arg)
        sys.exit(1)
    sys.exit(0)

def clean_up_functions():
    ''' Cleans up functions that are incorrect and replace them with basic function names. '''
    if len(sys.argv) != 5:
        print('Please add a start and end line (decimal, inclusive) to clean up.')
        sys.exit(1)
    cleaned = 0
    start = int(sys.argv[3])
    end = int(sys.argv[4])
    map_file = sys.argv[2]
    new_lines = []
    with open('general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    for count, line in enumerate(lines):
        if start <= count <= end and len(line) > 29:
            function = line[29:-1]
            if function in BANNED_FUNCTIONS:
                address = line[:8]
                first_part = line[:29]
                line = f'{first_part}zz_{address}_\n'
                cleaned += 1
        new_lines.append(line)
    with open('general/symbol_maps/' + map_file, 'w') as open_file:
        open_file.writelines(new_lines)
    print(f'{cleaned} cleaned.')

def find_duplicates():
    ''' Finds duplicate functions. '''
    map_file = sys.argv[2]
    with open('general/symbol_maps/' + map_file, 'r') as open_file:
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
    with open('general/symbol_maps/' + map_file, 'r') as open_file:
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

def map_length_fix():
    '''
    Fixes the length of function in the symbol map with incorrect lengths.
    The reason that some lengths are incorrect is because they may contain a branch that shouldn't
    count for the function length, but did count when Dolphin automatically generated the symbol
    map. It accomplished this by counting the difference in bytes between the start and end
    of the function.
    '''
    map_file = sys.argv[2]
    with open('general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    newlines = []
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
                    newlines[-1] = newlines[-1][:9] + '{:08x}'.format(diff) + newlines[-1][17:]
                    print('Fixed function: {} ({:02X})'.format(previous[4].strip(), previous_addr))
            previous = parts
        newlines.append(line)
    with open('general/symbol_maps/' + map_file, 'w', newline='\n') as open_file:
        for newline in newlines:
            open_file.write(newline)

def find_missing_objects():
    ''' Find functions without objects. '''
    map_file = sys.argv[2]
    with open('general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    for line in lines:
        if line.startswith('8') and len(line) > 29:
            function = line[29:-1]
            parts = function.split(' ')
            if len(parts) < 2:
                print(f'Function {function} does not have an object.')

def find_switched_objects():
    if len(sys.argv) != 5:
        print('Please add a start and end line (decimal, inclusive) to find switched objects.')
        sys.exit(1)
    start = int(sys.argv[3])
    end = int(sys.argv[4])
    map_file = sys.argv[2]
    switches = []
    last = None
    with open('general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    for count, line in enumerate(lines):
        if start <= count <= end and len(line) > 29:
            function = line[29:-1]
            split = function.find(' ')
            # Assume that all functions have objects
            if split != -1:
                obj = function[split + 1:]
                if last != obj:
                    # We've changed objects, check if we've already changed away before
                    if obj in switches:
                        # Found a switch, alert the user
                        print(f'Switch found at line {count}: {function}')
                    else:
                        switches.append(obj)
                last = obj

def is_map_valid():
    ''' Checks that the given memory map file is a valid memory map. '''
    # Check that the address in the 1st and 3rd spot of each line match
    map_file = sys.argv[2]
    with open('general/symbol_maps/' + map_file, 'r') as open_file:
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
    with open('general/symbol_maps/' + map_file, 'r') as open_file:
        lines = open_file.readlines()
    for line in lines:
        if len(line) > 31 and line[29:32] == 'zz_':
            print('Found ' + line[29:-1])

BANNED_FUNCTIONS = ['GXInitTexObjUserData 	gx.a GXTexture.o',
'J2DTevBlock1::setFontNo(unsigned short) 	J2DGraph.a J2DMatBlock.o',
'J2DTextBoxEx::setAnimation(J2DAnmTevRegKey *) 	J2DGraph.a J2DTextBoxEx.o',
'WorldDarkening::Fade(float, float)', 'nlVector3::Set(float, float, float)',
'JAUSeqDataBlock::JAUSeqDataBlock(void) 	JAudio2.a JAUSeqDataBlockMgr.o',
'nlListContainer<P8SaveData>::__ct(void)', 'IPCGetBufferLo 	ipc.a ipcMain.o',
'J3DShapeMtxMulti::getUseMtxNum(void) const 	J3DGraphBase.a J3DShapeMtx.o',
'JGadget::TNodeLinkList::iterator::operator++(void) 	JAudio2.a JASTrack.o',
'GDSetCurrOffset 	J3DGraphBase.a J3DMatBlock.o', 'glxSwapWaitDrawDone(void)',
'homebutton::MotorCallback(OSAlarm *, OSContext *) 	homebuttonLib.a HBMBase.o',
'dJointSetCharacterNoMotionDirection(dxJoint *, float *)', 'OSGetCurrentContext',
'OSGetStackPointer 	os.a OSContext.o', 'THPSimpleGetCurrentFrame', 'nlInit(void)',
'GameInfoManager::SetUserSelectedCupSidekick(eSidekickID)', 'cTeam::GetPlayer(int)',
'homebutton::Controller::isPlayReady(void) const 	homebuttonLib.a HBMController.o',
'JASDsp::getDSPMixerLevel(void) 	JAudio2.a JASDSPInterface.o', 'PSQUATDotProduct',
'nw4hbm::lyt::Window::GetRuntimeTypeInfo(void) const 	homebuttonLib.a lyt_window.o',
'J3DColorBlockLightOff::setColorChanNum(unsigned char) 	J3DGraphBase.a J3DMatBlock.o',
'J3DColorBlockLightOff::getColorChanNum(void) const 	J3DGraphBase.a J3DMatBlock.o',
'GetCommonDesireData(eFielderDesireState)', 'FEAudio::ResetRandomVoiceToggleSFX(void)',
'BIRDOSoundPropAccessor::ResetSoundPropTable(void)', 'dGeomDisable', '__set_debug_bba',
'DrawableTmModel::SetAnimationSpeed(float)', 'EmissionController::IsLingering( (void))',
'AnimatedModelExplodable::SetUnexplodedModelVisibility(bool)', 'dataARAMDefaultGetInfo',
'cPlayer::PostPhysicsUpdate(void)', 'FETweener::setDoneCallFunc(void (*)(void *), void *)',
'GetOneTimerLeadGroundContactAnims(void)', 'DrawableCharacter::GetAnimController( (void))',
'dVector4Set(float *, float, float, float, float)', 'cPoseNode::SetChild(int, cPoseNode *)',
'__dla(void *) 	JKernel.a JKRHeap.o', 'GXInitLightColor', 'IPCSetBufferLo 	ipc.a ipcMain.o',
'Increment<Q29CrowdMood10CROWD_MOOD>(CrowdMood::CROWD_MOOD &)', 'PSVECSubtract 	mtx.a vec.o',
'nw4hbm::ut::TextWriterBase<w>::SetCharSpace(float) 	homebuttonLib.a ut_TextWriterBase.o',
'setTevColor__Q23lyt16MaterialAccessorCFUlRCQ33hel6common5Color 	src.a MaterialAccessor.o',
'DBClose 	NdevExi2A.a DebuggerDriver.o', 'AnimatedModelExplodable::GetWorldMatrix( (void))',
'___blank(char *,...)', 'J3DLockedMaterial::initialize(void) 	J3DGraphBase.a J3DMaterial.o',
'cPlayer::ClearSwapControllerTimer(void)', 'JAISeMgr::initParams(void) 	JAudio2.a JAISeMgr.o',
'JUTResFont::getFontType(void) const 	JUtility.a JUTCacheFont.o', 'GLXMemoryInfo::__ct(void)',
'nw4hbm::ut::TextWriterBase<w>::GetCharSpace(void) const 	homebuttonLib.a ut_TextWriterBase.o',
'J3DGXColorS10::operator=(_GXColorS10 const &) 	J3DGraphBase.a J3DMatBlock.o', 'SetTRKConnected',
'GXPosition3f32 	J2DGraph.a J2DPictureEx.o', 'cAIPad::__ct(void)', 'PSVECAdd 	mtx.a vec.o',
'OSInitFastCast 	d_meter2_draw.o ', 'cFielder::IsStriker( (void))', 'ButtonComponent::__ct(void)',
'J3DTexGenBlock4::getNBTScale(void) 	J3DGraphBase.a J3DMatBlock.o', 'TRKTargetSetInputPendingPtr',
'JGadget::operator==(JGadget::TNodeLinkList::iterator, JGadget::TNodeLinkList::iterator) 	JAudio2.a JASTrack.o',
'JSUList<Q212JUTException12JUTExMapFile>::JSUList<Q212JUTException12JUTExMapFile>(bool) 	JUtility.a JUTException.o',
'gdev_cc_shutdown 	TRK_Hollywood_Revolution.a C:\\products\\RVL\\runtime_libs\\gamedev\\cust_connection\\cc\\exi2\\GCN\\EXI2_GDEV_GCN\\mai',
'CBGetBytesAvailableForRead 	TRK_Hollywood_Revolution.a C:\\products\\RVL\\runtime_libs\\gamedev\\cust_connection\\utils\\common\\Circle']

if __name__ == "__main__":
    main()
