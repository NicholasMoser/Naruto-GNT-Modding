file = io.open("C:/Users/kites/Desktop/test.log", "a")
io.output(file)
io.write("Begin seq_reader.lua", "\n")

dolphin.hook_instruction(0x800c9138, function ()
    -- The start of the seq file is at *(int *)(seq_p[5] + 0x5c)
    seq_p = dolphin.ppc.gpr[3]
    temp_p = dolphin.mem_u32[seq_p + 0x14]
    seq_start = dolphin.mem_u32[temp_p + 0x5c]

    -- The current program counter of the seq file is in general purpose register 5
    seq_pc = tonumber(dolphin.ppc.gpr[5])

    -- Calculate the offset in the seq file
    seq_offset = seq_pc - seq_start
    offset = string.format("Offset: %08x ", seq_offset)

    -- Append the data to the log file
    io.write(offset, "\n")
end)
