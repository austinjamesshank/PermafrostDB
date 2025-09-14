'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Core DB set operations.

Revision History:
    > 2025-09-13 @ajx: Created
'''

from typing import IO, Any
from core.data.blockCore import iceWizard as wizard, pieceGoblin as goblin, block
from utils import auditer, ioManager as io
from utils.translator import txr

def set(blockType: str, key: str, pc: int, data: str) -> bool:
    '''
        Sets a piece of data in a block.

        Parameters:
            blockType (str): The type of block being modified.
            key (str): The key of the specific block to which we are setting data.
            pc (int): The piece of our block we are setting.
            data (str): The data set into the piece.
        Returns:
            bool: True if the operation was successful, otherwise False.
    '''
    blockIO = wizard.openBlockIO(blockType, key, io.IOModes.READ_PLUS)
    if blockIO is None:
        print(f"Failed to open blockIO for {blockType} {key}") # TODO remove me
        return False
    return __writeData(blockIO, data, pc, blockType, key)

def __writeData(blockIO: IO[Any], data: str, pc: int, blockType: str, key: str) -> bool:
    try:
        blockPieces = wizard.readBlockIOPieces(blockIO, False)
        i = goblin.pc2ix(pc)
        if not block.containsPiece(pc, len(blockPieces)):
            wizard.fillBlockPieces(blockPieces, i)
        blockPieces[i] = goblin.pieceStorageFormat(data)
        wizard.writeBlockIOPieces(blockIO, blockPieces, True)
        return True
    except Exception as e:
        wizard.closeBlockIO(blockIO)
        auditer.logActionFailure(io.Actions.WRITE, blockIO.name, __str__pieceWriteFail(pc), e)
        return False
    
### Strings ###
def __str__pieceWriteFail(piece: int) -> str: 
    return txr("Piece: {0}", piece)
