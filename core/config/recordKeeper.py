'''
Author: Austin Shank (@ajx)
Created: 2025-09-14

Description:
Core DB configuration information.

Revision History:
    > 2025-09-14 @ajx: Created
'''

LEAD_DIR = ".pmf"
''' Stores the "lead" directory for this implementation. This is defined as the highest directory of
    the PermafrostDB structure. Database roots are stored within.'''

BLOCK_DIR = ".b"
CONFIG_DIR = ".c"
LOG_DIR = ".l"
INDEX_DIR = ".i"
TEMP_DIR = ".t"
ROOTS_FILE = "db_roots.cfg"