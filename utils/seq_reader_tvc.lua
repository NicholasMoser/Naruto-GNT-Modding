file = io.open("C:/Users/kites/Desktop/test.log", "a")
io.output(file)
io.write("Begin seq_reader_tvc.lua", "\n")
io.write("File                             Offset   Opcode", "\n")

function parse_seq()
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
end

-- The below four hooks occur in the function seq_parse (0x800e0948)
dolphin.hook_instruction(0x800e0a34, parse_seq)

dolphin.hook_instruction(0x800e0a90, parse_seq)

dolphin.hook_instruction(0x800e0c28, parse_seq)

dolphin.hook_instruction(0x800e0cdc, parse_seq)

-- These appear to be called in other circumstances, like seqs calling other seqs
dolphin.hook_instruction(0x800e0dc8, parse_seq)

dolphin.hook_instruction(0x800e0edc, parse_seq)

dolphin.hook_instruction(0x800e0fa0, parse_seq)

dolphin.hook_instruction(0x800e1050, parse_seq)
