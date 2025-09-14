'''
Author: Austin Shank (@ajx)
Created: 2025-09-14

Description:
Core DB building logic.

Revision History:
    > 2025-09-14 @ajx: Created
'''

import core.config.recordKeeper as rk
from utils import filepathChampion as fpc, ioManager as io
import os

def setup(newRoot: str) -> None:
    '''
    Ensure the directory structure exists.
    '''
    for dirPath in __dirs(newRoot):
        if not fpc.filepathExists(dirPath):
            os.makedirs(dirPath)

    rootsFilepath = fpc.joinLeadPath(rk.ROOTS_FILE)
    with io.openIO(rootsFilepath, io.IOModes.APPEND) as rootsIO:
        io.appendIO(rootsIO, [newRoot])         

def __dirs(newRoot: str) -> list[str]:
    newRootDir = fpc.joinLeadPath(newRoot)
    return [
        os.path.join(newRootDir, rk.BLOCK_DIR),
        os.path.join(newRootDir, rk.CONFIG_DIR),
        os.path.join(newRootDir, rk.LOG_DIR),
        os.path.join(newRootDir, rk.INDEX_DIR),
        os.path.join(newRootDir, rk.TEMP_DIR)
    ]
