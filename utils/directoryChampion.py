

import os
from typing import Optional
from utils import filepathChampion as fpc

def ensureDirectory(dirPath: str) -> bool:
    '''
    Ensures that a directory exists; creates it if it does not.
    Parameters:
        dirPath (str): The directory path to ensure.
    '''
    if not fpc.filepathExists(dirPath):
        os.makedirs(dirPath)
    return True

def getSubcontents(dirPath: str) -> Optional[list[str]]:
    '''
    Lists all contents in a given directory.
    Parameters:
        dirPath (str): The directory path to list files from.
    Returns:
        list[str]: A list of file names / directories in the directory.
    '''
    if not isDirectory(dirPath):
        return None
    
    return os.listdir(dirPath)

def isDirectory(dirPath: str) -> bool:
    '''
    Checks if a given path is a directory.
    Parameters:
        dirPath (str): The path to check.
    Returns:
        bool: True if the path is a directory, False otherwise.
    '''
    return fpc.filepathExists(dirPath) and os.path.isdir(dirPath)