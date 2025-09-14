'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Logic pertaining to piece data storage operations and management.

Revision History:
    > 2025-09-13 @ajx: Created
'''

def pc2ix(line):
    return line - 1

def pieceStorageFormat(line):
    return f"{pieceStripFormat(line)}\n"

def pieceStripFormat(line):
    return line.strip()