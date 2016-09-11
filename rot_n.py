results = []
string = 'nxvuvgb.gfhobv'
for num in range(26):
    new_string = []
    for character in string:
        if 'z' < chr(ord(character) + num):
          new_charcter = chr(ord(character) - (26-num))
        else:
          new_charcter = chr(ord(character) + num)
        new_string.append(new_charcter)

    results.append(''.join(new_string))

for result in results:
    print result.decode('rot13')
