
from core.config import rootCartographer as rc
from core.data import seeker, scribe
from core.data.blockCore import iceSculptor
from _unitTesting import testUtils

def __test001():
    testUtils.setupTheSystem()
    
    dbRoot = rc.getCurrentPIDRoot()
    assert (dbRoot == testUtils.TEST_DB_ROOT)
    
    testUtils.nukeTheFuckingDB()

    # If there is no database, getting a value should return ""
    value = seeker.get("BLOCK", "KEY", 1)
    assert (value == "")

    key1 = iceSculptor.createNewBlock("BLOCK")
    key2 = iceSculptor.createNewBlock("BLOCK")
    assert (key1 != "")
    assert (key2 != "")
    assert (key1 != key2)

    scribe.set("BLOCK", key1, 1, "VALUE1")
    scribe.set("BLOCK", key1, 2, "VALUE2")
    scribe.set("BLOCK", key2, 1, "VALUE3")
    scribe.set("BLOCK", key2, 2, "VALUE4")

    value = seeker.get("BLOCK", key1, 1)
    assert (value == "VALUE1")
    value = seeker.get("BLOCK", key1, 2)
    assert (value == "VALUE2")
    value = seeker.get("BLOCK", key2, 1)
    assert (value == "VALUE3")
    value = seeker.get("BLOCK", key2, 2)
    assert (value == "VALUE4")

    return testUtils.PASS

if __name__ == "__main__":
    __test001()