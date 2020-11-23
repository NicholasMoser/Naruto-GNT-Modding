file = io.open("C:/Users/kites/Desktop/test.log", "a")
io.output(file)
io.write("Begin seq_reader.lua", "\n")
io.write("File            Offset   Opcode", "\n")

dolphin.hook_instruction(0x800c9138, function ()
    -- The start of the seq file is at *(int *)(seq_p[5] + 0x5c)
    seq_p = dolphin.ppc.gpr[3]
    temp_p = dolphin.mem_u32[seq_p + 0x14]
    seq_start = dolphin.mem_u32[temp_p + 0x5c]

    -- The current program counter of the seq file is in general purpose register 5
    seq_pc = tonumber(dolphin.ppc.gpr[5])

    -- Calculate the offset in the seq file
    seq_offset = seq_pc - seq_start
    offset_str = string.format("%08x ", seq_offset)

    -- Get the file name, which can be found at seq_p[8][5]
    file_entry = dolphin.mem_u32[seq_p + 0x20]
    file_name = dolphin.str_read(file_entry + 0x14, 0x10)
    file_name_str = string.format("%15s ", string.sub(file_name, 0, 0xf))

    -- Get the current opcode being executed
    opcode = dolphin.mem_u32[seq_pc]
    opcode_str = string.format("%08x ", opcode)

    -- Append the data to the log file
    io.write(file_name_str, offset_str, opcode_str, "\n")
end)
