
# Manual way of getting the seq execution path before I wrote a Lua script.
base = 0x802c6780

with open('seq_path', 'r') as f:
    lines = f.readlines()

for line in lines:
    if line.startswith('#'):
        print(line.strip())
    else:
        num = int(line, 16)
        offset = num - base
        print(hex(offset))
