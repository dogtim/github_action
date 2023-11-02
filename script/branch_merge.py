import subprocess

def execute_git_command(command):
    print(command)
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,  # Raise a CalledProcessError for non-zero exit codes.
        )
        output = result.stdout
        if "fatal:" in output.lower() or "Automatic merge failed" in output.lower():
            print("Error encountered: " + output)
            exit(1)
        print(output)
    except subprocess.CalledProcessError as e:
        # Handle Git command error here
        print(str(e))
        exit(1)

def mergeDevIntoMaster():
    # Example Git commands
    git_commands = [
        "git fetch -p",
        "git checkout -b main origin/main",
        "git pull origin dev --no-rebase --no-edit",
    ]

    for command in git_commands:
        output = execute_git_command(command)
        print(output)

    print("Done")

if __name__ == "__main__":
    mergeDevIntoMaster()
