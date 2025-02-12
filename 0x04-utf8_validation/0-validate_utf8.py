#!/usr/bin/python3
'''UTF-8 Validation'''


def validUTF8(data):
    '''Checks if a given array of integers represents
    valid UTF-8 encoded data.'''
    continuation_bytes = 0
    for byte in data:
        if continuation_bytes == 0:
            if (byte & 0b10000000) == 0b00000000:
                continue
            elif (byte & 0b11100000) == 0b11000000:
                continuation_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                continuation_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                continuation_bytes = 3
            else:
                return False
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            continuation_bytes -= 1
    return continuation_bytes == 0
