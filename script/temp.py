import os
import time

def execute(command: str):
    print(command)
    try:
        start_time = time.time()  # Record the start time
        proc = os.popen(command)
        output = proc.read()
        print(output, flush=True)
        
        returncode = proc.close()
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate execution time
        
        print("Command execution time:", execution_time, "seconds")
        if returncode:
            print("Error occurred: " + str(returncode))
            exit(1)
    except Exception as e:
        print("Something wrong: ", e)
        exit(1)

def mergeDevIntoMaster():
    # Example Git commands
    git_commands = [
        "git fetch -p",
        "git merge dev",
    ]

    for command in git_commands:
        output = execute(command)

    print("Done")

if __name__ == "__main__":
    mergeDevIntoMaster()
