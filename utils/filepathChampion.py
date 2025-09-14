'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Logic for handling file paths.

Revision History:
    > 2025-09-13 @ajx: Created
'''

import os

from core.config.recordKeeper import LEAD_DIR, BLOCK_DIR

ROOT_DIR = "C:\\Users\\austi\\Projects\\Software\\PermafrostDB"

def appRootDir() -> str:
    '''
    Returns the root directory for the application or data storage.
    Returns:
        str: The root directory path.
    '''
    return ROOT_DIR

def filepathExists(filepath: str) -> bool:
    '''
    Checks if a given file path exists.
    Parameters:
        filepath (str): The file path to check.
    Returns:
        bool: True if the file path exists, False otherwise.
    '''
    return os.path.exists(filepath)

def joinLeadPath(*pathSegments: str) -> str:
    '''
    Joins multiple path segments into a single file path.
    Ensures the path is rooted at the application root directory
    and includes the lead directory.
    Parameters:
        *pathSegments (str): The segments of the path to join.
    Returns:
        str: The joined file path.
    '''
    return joinPath(appRootDir(), LEAD_DIR, *pathSegments)

def joinPath(*pathSegments: str) -> str:
    '''
    Joins multiple path segments into a single file path.
    Parameters:
        *pathSegments (str): The segments of the path to join.
    Returns:
        str: The joined file path.
    '''
    return os.path.join(*pathSegments)
