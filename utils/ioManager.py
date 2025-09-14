'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
File management utilities.

Revision History:
    > 2025-09-13 @ajx: Created
'''

import builtins
from typing import IO, Any, Optional
from utils import auditer
from utils.translator import txr

UNKNOWN_FILEPATH = "UNKNOWN FILEPATH"

class Actions:
    OPEN = "OPEN"
    READ = "READ"
    WRITE = "WRITE"
    CLOSE = "CLOSE"
    DELETE = "DELETE"

class IOModes:
    READ = "r"
    WRITE = "w"
    APPEND = "a"
    READ_PLUS = "r+"
    WRITE_PLUS = "w+"
    APPEND_PLUS = "a+"

def openIO(filepath: str, mode: str = IOModes.READ) -> Optional[IO[Any]]:
    try:
        return open(filepath, mode)
    except Exception as e:
        auditer.logActionFailure(Actions.OPEN, filepath, __str__openFailMode(mode), e)
        return None
    
def closeIO(fileIO: IO[Any]) -> bool:
    if not __hasFileIO(fileIO, Actions.CLOSE):
        return False
    try:
        if fileIO:
            fileIO.close()
        return True
    except Exception as e:
        auditer.logActionFailure(Actions.CLOSE, fileIO.name if fileIO else UNKNOWN_FILEPATH, None, e)
        return False
    
def readIO(fileIO: IO[Any], shouldClose: bool = True) -> Optional[list[str]]:
    if not __hasFileIO(fileIO, Actions.READ):
        return None
    try:
        lines = fileIO.readlines()
        if shouldClose:
            closeIO(fileIO)
        return lines
    except Exception as e:
        auditer.logActionFailure(Actions.READ, fileIO.name if fileIO else UNKNOWN_FILEPATH, None, e)
        closeIO(fileIO)
        return None
    
def appendIO(fileIO: IO[Any], lines: list[str], shouldClose: bool = True) -> bool:
    if not __hasFileIO(fileIO, Actions.WRITE):
        return False
    try:
        fileIO.writelines(lines)
        if shouldClose:
            closeIO(fileIO)
        return True
    except Exception as e:
        auditer.logActionFailure(Actions.WRITE, fileIO.name if fileIO else UNKNOWN_FILEPATH, __str__writeFailLineCount(len(lines)), e)
        closeIO(fileIO)
        return False

def rewriteIO(fileIO: IO[Any], lines: list[str], shouldClose: bool = True) -> bool:
    if not __hasFileIO(fileIO, Actions.WRITE):
        return False
    try:
        fileIO.seek(0)
        fileIO.writelines(lines)
        fileIO.truncate()
        if shouldClose:
            closeIO(fileIO)
        return True
    except Exception as e:
        auditer.logActionFailure(Actions.WRITE, fileIO.name if fileIO else UNKNOWN_FILEPATH, __str__writeFailLineCount(len(lines)), e)
        closeIO(fileIO)
        return False
    
def __hasFileIO(fileIO: Optional[IO[Any]], action: str) -> bool:
    if not fileIO:
        auditer.logActionFailure(action, UNKNOWN_FILEPATH, __str__noFileIO(), Exception(__str__noFileIO))
        return False
    return True

### Strings ###
def __str__openFailMode(mode: str) -> str:
    return txr("Mode: {0}", mode)
def __str__writeFailLineCount(lineCount: int) -> str: 
    return txr("Line count: {0}", lineCount)
def __str__noFileIO() -> str:
    return "File IO is None"