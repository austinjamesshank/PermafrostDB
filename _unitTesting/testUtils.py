from core.config import rootCartographer as rc, carpenter

TEST_DB_ROOT = "__poopDB"
PASS = 1
FAIL = 0

def setupTheSystem():
    carpenter.setup(TEST_DB_ROOT)
    rc.setCurrentPIDRoot(TEST_DB_ROOT)
    return ""

def nukeTheFuckingDB():
    '''
    Adios, poopDB.
    '''
    return ""

def createTestDB():
    '''
    Generate some poop for poopDB.
    '''
    return ""