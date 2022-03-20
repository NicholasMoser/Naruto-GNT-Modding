-- During seq file parsing will send UDP packets with the filename, seq file offset, opcode, and program counter
-- The UDP packet will be sent over port 12198

socket = require("socket")
udp = socket.udp()
udp:settimeout(0)
udp:setoption('reuseaddr',true)
udp:setsockname('*', 1900)
udp:setpeername('localhost', 12198) -- Echo IP and Port number

function parse_seq()
    -- The start of the seq file is at *(int *)(seq_p[5] + 0x5c)
    seq_p = dolphin.ppc.gpr[3]
    temp_p = dolphin.mem_u32[seq_p + 0x14]
    seq_start = dolphin.mem_u32[temp_p + 0x5c]

    -- The current program counter of the seq file is in general purpose register 5
    seq_pc = tonumber(dolphin.ppc.gpr[5])

    -- Calculate the offset in the seq file
    seq_offset = seq_pc - seq_start
    offset_str = string.format("%08x,", seq_offset)

    -- Get the file name, which can be found at seq_p[8][5]
    file_entry = dolphin.mem_u32[seq_p + 0x20]
    file_name = dolphin.str_read(file_entry + 0x14, 0x10)
    file_name_str = string.format("%-15s,", string.sub(file_name, 0, string.len(file_name) - 1))

    -- Get the current opcode being executed
    opcode = dolphin.mem_u32[seq_pc]
    opcode_str = string.format("%08x,", opcode)

    -- Get the program counter
    pc = dolphin.ppc.pc
    pc_str = string.format("%08x", pc)
    full_str = file_name_str .. offset_str .. opcode_str .. pc_str
    udp:send(full_str)
end

-- The below four hooks occur in the function seq_parse (0x800c8f38)
dolphin.hook_instruction(0x800c903c, parse_seq)

dolphin.hook_instruction(0x800c9094, parse_seq)

dolphin.hook_instruction(0x800c9138, parse_seq)

dolphin.hook_instruction(0x800c91a0, parse_seq)

-- These appear to be called in other circumstances, like seqs calling other seqs
dolphin.hook_instruction(0x800c8e30, parse_seq)

dolphin.hook_instruction(0x800c8ef8, parse_seq)

dolphin.hook_instruction(0x80106f10, parse_seq)
