'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Core DB get operations.

Revision History:
    > 2025-09-13 @ajx: Created
'''

from typing import IO, Any
from core.data.blockCore import iceWizard as wizard, pieceGoblin as goblin, block
from utils import auditer, ioManager as io
from utils.translator import txr

def get(blockType: str, key: str, pc: int) -> str:
    '''
        Gets a piece of data from a block.

        Parameters:
            blockType (str): The type of block from which we are getting data.
            key (str): The key of the specific block from which we are getting data.
            pc (int): The piece of our block we are getting.
        Returns:
            bool: True if the operation was successful, otherwise False.
    '''
    blockIO = wizard.openBlockIO(blockType, key, io.IOModes.READ)
    if blockIO is None:
        return ""
    return __readData(blockIO, pc, blockType, key)

def __readData(blockIO: IO[Any], pc: int, blockType: str, key: str) -> str:
    try:
        blockPieces = wizard.readBlockIOPieces(blockIO, False)
        i = goblin.pc2ix(pc)
        result = ""
        if block.containsPiece(pc, len(blockPieces)):
            result = goblin.pieceStripFormat(blockPieces[i])
        wizard.closeBlockIO(blockIO)
        return result
    except Exception as e:
        wizard.closeBlockIO(blockIO)
        auditer.logActionFailure(io.Actions.READ, blockType, key, __str__pieceReadFail(pc), e)
        return ""
    
### Strings ###
def __str__pieceReadFail(pc: int) -> str: 
    return txr("Piece: {0}", pc)