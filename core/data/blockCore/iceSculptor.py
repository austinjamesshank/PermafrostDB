'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Logic block creation.

Revision History:
    > 2025-09-13 @ajx: Created
''' 

from utils import filepathChampion as fpc, ioManager as io, directoryChampion as dc
from core.data.blockCore import block
from core.config import rootCartographer as rc, recordKeeper as rk

def createNewBlock(blockType: str) -> str:
    dbRoot = rc.getCurrentPIDRoot()
    key = _getNextBlockKey(blockType, dbRoot)
    with io.openIO(block.getBlockPath(blockType, key, dbRoot), io.IOModes.WRITE):
        pass
    return key

def _getNextBlockKey(blockType: str, dbRoot: str) -> str:
    blockTypeDir = block.getBlockDirectory(blockType, dbRoot)
    dc.ensureDirectory(blockTypeDir)
    existingBlocks = dc.getSubcontents(blockTypeDir)
    highestKey = 0
    for filename in existingBlocks:
        if not block.isBlockFile(filename):
            continue
        try:
            key = block.getKeyFromFile(filename)
            key = block.key_strToHex(key)
            if key > highestKey:
                highestKey = key
        except ValueError:
            continue
    return block.key_hexToStr(highestKey + 1)  # returns the next key as a hex string

def blockExists(blockType: str, key: str) -> bool:
    return fpc.filepathExists(block.getFilepath(blockType, key))