import sys
import os

def execute(command: str, read_result: bool):
    proc = os.popen(command)
    if read_result:
        output = proc.read()
        print(output, flush=True)

def mergeDevIntoMaster():
    execute("git fetch -p", read_result=True)
    execute("git checkout -b main origin/main", read_result=True)
    execute("git checkout -b main origin/main", read_result=True)
    execute("git pull origin dev --no-rebase --no-edit", read_result=True)
    print("Done")

if __name__ == "__main__":
    mergeDevIntoMaster()
