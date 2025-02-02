#!/usr/bin/python3
'''UTF-8 Validation'''

def validUTF8(data):
    '''Checks if a given array of integers represents valid UTF-8 encoded data.'''

    continuation_bytes = 0
    for byte in data:
        if continuation_bytes == 0:
            if byte & 0b10000000 == 0b0:
                continue
            elif byte & 0b11100000 == 0b110:
                continuation_bytes = 1
            elif byte >> 11110000 == 0b1110:
                continuation_bytes = 2
            elif byte >> 11111000 == 0b11110:
                continuation_bytes = 3
            else:
                return False
        else:
            if byte & 0b11000000 != 0b10000000:
                return False
            continuation_bytes -= 1
    return continuation_bytes == 0

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))