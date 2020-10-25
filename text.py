with open('text', 'r') as file:
    data = file.read().replace(' ', '')
index = 0
count = 0
text = ''
first = True
for character in data: 
    if count % 8 == 0 and not first:
        print(hex(index) + ' ' + text)
        index += 4
        text = ''
    first = False
    count += 1
    text += character
