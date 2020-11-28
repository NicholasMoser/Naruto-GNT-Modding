file = io.open("C:/Users/kites/Desktop/test.log", "a")
io.output(file)
io.write("Begin seq_reader_tvc.lua", "\n")
io.write("File                             Offset   Opcode", "\n")

dolphin.hook_instruction(0x800e0a34, function ()
    -- The start of the seq file is at *(int *)(seq_p[3] + 0x5c)
    seq_p = dolphin.ppc.gpr[3]
    temp_p = dolphin.mem_u32[seq_p + 0xc]
    seq_start = dolphin.mem_u32[temp_p + 0x5c]

    -- The current program counter of the seq file is in general purpose register 5
    seq_pc = tonumber(dolphin.ppc.gpr[5])

    -- Calculate the offset in the seq file
    seq_offset = seq_pc - seq_start
    offset_str = string.format("%08x ", seq_offset)

    -- Get the file name, which can be found at seq_p[3][1d][4]
    temp_p2 = dolphin.mem_u32[seq_p + 0xc]
    file_entry = dolphin.mem_u32[temp_p2 + 0x58]
    file_name = dolphin.str_read(file_entry + 0x1c, 0x20)
    file_name_str = string.format("%-32s ", string.sub(file_name, 0, string.len(file_name) - 1))

    -- Get the current opcode being executed
    opcode = dolphin.mem_u32[seq_pc]
    opcode_str = string.format("%08x ", opcode)

    -- Append the data to the log file
    io.write(file_name_str, offset_str, opcode_str, "\n")
end)

dolphin.hook_instruction(0x800e0a90, function ()
    -- The start of the seq file is at *(int *)(seq_p[3] + 0x5c)
    seq_p = dolphin.ppc.gpr[3]
    temp_p = dolphin.mem_u32[seq_p + 0xc]
    seq_start = dolphin.mem_u32[temp_p + 0x5c]

    -- The current program counter of the seq file is in general purpose register 5
    seq_pc = tonumber(dolphin.ppc.gpr[5])

    -- Calculate the offset in the seq file
    seq_offset = seq_pc - seq_start
    offset_str = string.format("%08x ", seq_offset)

    -- Get the file name, which can be found at seq_p[3][1d][4]
    temp_p2 = dolphin.mem_u32[seq_p + 0xc]
    file_entry = dolphin.mem_u32[temp_p2 + 0x58]
    file_name = dolphin.str_read(file_entry + 0x1c, 0x20)
    file_name_str = string.format("%-32s ", string.sub(file_name, 0, string.len(file_name) - 1))

    -- Get the current opcode being executed
    opcode = dolphin.mem_u32[seq_pc]
    opcode_str = string.format("%08x ", opcode)

    -- Append the data to the log file
    io.write(file_name_str, offset_str, opcode_str, "\n")
end)

dolphin.hook_instruction(0x800e0c28, function ()
    -- The start of the seq file is at *(int *)(seq_p[3] + 0x5c)
    seq_p = dolphin.ppc.gpr[3]
    temp_p = dolphin.mem_u32[seq_p + 0xc]
    seq_start = dolphin.mem_u32[temp_p + 0x5c]

    -- The current program counter of the seq file is in general purpose register 5
    seq_pc = tonumber(dolphin.ppc.gpr[5])

    -- Calculate the offset in the seq file
    seq_offset = seq_pc - seq_start
    offset_str = string.format("%08x ", seq_offset)

    -- Get the file name, which can be found at seq_p[3][1d][4]
    temp_p2 = dolphin.mem_u32[seq_p + 0xc]
    file_entry = dolphin.mem_u32[temp_p2 + 0x58]
    file_name = dolphin.str_read(file_entry + 0x1c, 0x20)
    file_name_str = string.format("%-32s ", string.sub(file_name, 0, string.len(file_name) - 1))

    -- Get the current opcode being executed
    opcode = dolphin.mem_u32[seq_pc]
    opcode_str = string.format("%08x ", opcode)

    -- Append the data to the log file
    io.write(file_name_str, offset_str, opcode_str, "\n")
end)

dolphin.hook_instruction(0x800e0cdc, function ()
    -- The start of the seq file is at *(int *)(seq_p[3] + 0x5c)
    seq_p = dolphin.ppc.gpr[3]
    temp_p = dolphin.mem_u32[seq_p + 0xc]
    seq_start = dolphin.mem_u32[temp_p + 0x5c]

    -- The current program counter of the seq file is in general purpose register 5
    seq_pc = tonumber(dolphin.ppc.gpr[5])

    -- Calculate the offset in the seq file
    seq_offset = seq_pc - seq_start
    offset_str = string.format("%08x ", seq_offset)

    -- Get the file name, which can be found at seq_p[3][1d][4]
    temp_p2 = dolphin.mem_u32[seq_p + 0xc]
    file_entry = dolphin.mem_u32[temp_p2 + 0x58]
    file_name = dolphin.str_read(file_entry + 0x1c, 0x20)
    file_name_str = string.format("%-32s ", string.sub(file_name, 0, string.len(file_name) - 1))

    -- Get the current opcode being executed
    opcode = dolphin.mem_u32[seq_pc]
    opcode_str = string.format("%08x ", opcode)

    -- Append the data to the log file
    io.write(file_name_str, offset_str, opcode_str, "\n")
end)
