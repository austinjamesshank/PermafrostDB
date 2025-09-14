'''
Author: Austin Shank (@ajx)
Created: 2025-09-13

Description:
Logic for mapping PIDs to their respective database.

Revision History:
    > 2025-09-13 @ajx: Created
'''

import os
from utils import ioManager as io, auditer, filepathChampion as fpc
import core.config.recordKeeper as rk

PID_ROOT_MAP_FILE = "pid_root_map.cfg"

def getPidRootMapFilepath() -> str:
    return fpc.joinLeadPath(PID_ROOT_MAP_FILE)

def setCurrentPIDRoot(root: str):
    return setPIDRoot(os.getpid(), root)
    
def setPIDRoot(pid: int, root: str):
    return __appendPIDRootMapping(pid, root)

def __appendPIDRootMapping(pid: int, root: str) -> bool:
    try:
        pidRootMapPath = getPidRootMapFilepath()
        pidRootMapIO = io.openIO(pidRootMapPath, io.IOModes.APPEND)
        if not pidRootMapIO:
            return False
        return io.appendIO(pidRootMapIO, [__pidRootMapping(pid, root)])
    except Exception:
        return False
    
def __pidRootMapping(pid: int, root: str) -> str:
    return f"{pid}:{root}"

def getCurrentPIDRoot() -> str | None:
    return getPIDRoot(os.getpid())

def getPIDRoot(pid: int) -> str | None:
    try:
        pidRootMapPath = getPidRootMapFilepath()
        if not fpc.filepathExists(pidRootMapPath):
            return None
        pidRootMapIO = io.openIO(pidRootMapPath, io.IOModes.READ)
        if not pidRootMapIO:
            return None
        lines = io.readIO(pidRootMapIO)
        if not lines:
            return None
        for line in lines:
            line = line.strip()
            if line.startswith(f"{pid}:"):
                return line.split(":", 1)[1]
        return None
    except Exception as e:
        auditer.logActionFailure("GET_PID_ROOT", fpc.joinLeadPath(), str(pid), e)
        return None