import os
import subprocess

'''
Quick run:
python -m _unitTesting.testRunner
'''

UNIT_TESTING_DIR = "_unitTesting"

def __runAllTests():
    currentDir = os.path.dirname(__file__)
    testDir = os.path.join(currentDir, "tests")
    for file in os.listdir(testDir):
        if not file.endswith(".py"):
            continue
        print(f'Running {file}...')
        module = f"{UNIT_TESTING_DIR}.tests.{file[:-3]}"
        result = subprocess.run(['python', '-m', module], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print('ERROR:', result.stderr)

if __name__ == "__main__":
    __runAllTests()