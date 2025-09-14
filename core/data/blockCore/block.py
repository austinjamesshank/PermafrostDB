'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Basic block definitions.

Revision History:
    > 2025-09-13 @ajx: Created
'''

import os
from core.config import rootCartographer as rc, recordKeeper as rk
from utils import filepathChampion as fpc

BLOCK_SUFFIX = ".frz"

def containsPiece(pc, blockLength):
    return 1 <= pc <= blockLength
        
def getBlockPath(blockType: str, key: str, dbRoot: str = None) -> str:
    return fpc.joinPath(getBlockDirectory(blockType, dbRoot), f"{key}{BLOCK_SUFFIX}")

def getBlockDirectory(blockType: str, dbRoot: str = None) -> str:
    if dbRoot is None:
        dbRoot = rc.getCurrentPIDRoot()
    return fpc.joinLeadPath(dbRoot, rk.BLOCK_DIR, blockType)

def isBlockFile(filename: str) -> bool:
    return filename.endswith(BLOCK_SUFFIX)

def getKeyFromFile(filename: str) -> str:
    return filename[:-len(BLOCK_SUFFIX)]

def key_strToHex(key: str) -> int:
    return int(key, 16)

def key_hexToStr(key: int) -> str:
    return format(key, "x")