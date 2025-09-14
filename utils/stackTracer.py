'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Stack tracing utilities.

Revision History:
    > 2025-09-13 @ajx: Created
'''

import inspect

def getMe() -> str:
    '''
        Get the name of the current function.
        Returns:
            str: The name of the current function.
    '''
    return inspect.stack()[1].function

def getMyCaller() -> str:
    '''
        Get the name of the calling function.
        Returns:
            str: The name of the calling function.
    '''
    return inspect.stack()[2].function

def getParent(n: int) -> str:
    '''
        Get the name of the nth parent function.
        Parameters:
            n (int): The number of levels up the call stack to go.
        Returns:
            str: The name of the nth parent function.
    '''
    return inspect.stack()[n + 1].function