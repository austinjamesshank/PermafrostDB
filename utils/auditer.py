'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Core error logging operations.

Revision History:
    > 2025-09-13 @ajx: Created
'''

NO_MESSAGE = "NO MSG"
ERROR_PREFACE = "ERROR"

def logActionFailure(action: str, filepath: str, message: str, e: Exception) -> None:
    '''
        Logs an action failure.
        Parameters:
            action (str): The action that failed.
            filepath (str): The file path related to the action.
            message (str): The error message to log.
            e (Exception): The exception that was raised.
    '''
    print(f"{ERROR_PREFACE}: {action} FAILURE / {filepath} / {message if not __noMessage(message) else NO_MESSAGE} / {e}")

def __noMessage(message: str) -> bool:
    return message is None or message.strip() == ""