'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Logic for direct block operations.

Revision History:
    > 2025-09-13 @ajx: Created
''' 

from typing import IO, Any, Optional

from core.data.blockCore import block, pieceGoblin as goblin
from utils import auditer, ioManager as io
from utils.translator import txr

### Core Block IO Operations ###

def openBlockIO(blockType: str, key: str, mode: str) -> Optional[IO[Any]]:
    return io.openIO(block.getBlockPath(blockType, key), mode)

def closeBlockIO(blockIO: IO[Any]) -> bool:
    return io.closeIO(blockIO)

def readBlockIOPieces(blockIO: IO[Any], shouldClose: bool = True) -> Optional[list[str]]:
    return io.readIO(blockIO, shouldClose)

def writeBlockIOPieces(blockIO: IO[Any], pieces: list[str], shouldClose: bool = True) -> bool:
    return io.rewriteIO(blockIO, pieces, shouldClose)

def fillBlockPieces(blockPieces: list[str], targetIndex: int, fillValue: str = "") -> list[str]:
    while len(blockPieces) <= targetIndex:
        blockPieces.append(goblin.pieceStorageFormat(fillValue))
    return blockPieces
