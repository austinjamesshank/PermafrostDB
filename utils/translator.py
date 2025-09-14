'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Translation logic for user-facing strings.

Revision History:
    > 2025-09-13 @ajx: Created
'''

import utils.stackTracer as tracer

txr = lambda s, *args: __placeArguments(__translate(s, tracer.getMyCaller()), *args)
'''
    Translate a string and replace placeholders with provided arguments.
    Parameters:
        s (str): The string to translate, with placeholders like {0}, {1}, etc.
        *args: Arguments to replace the placeholders in the string.
    Returns:
        str: The translated string with placeholders replaced by arguments.
'''

def __translate(s: str, key: str) -> str:
    return __txrLookup(s, key)

def __placeArguments(s: str, *args) -> str:
    for i, val in enumerate(args):
        s = s.replace(f'{{{i}}}', str(val))
    return s

def __txrLookup(s: str, key: str) -> str:
    if key == "example_key":
        return "example_translation"
    return s