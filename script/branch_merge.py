import subprocess

def execute_git_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,  # Raise a CalledProcessError for non-zero exit codes.
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Handle Git command error here
        error_message = e.stderr
        return error_message

def mergeDevIntoMaster():
    # Example Git commands
    git_commands = [
        "git fetch -p",
        "git checkout -b main origin/main",
        "git pull origin dev --no-rebase --no-edit",
    ]

    for command in git_commands:
        try:
            output = execute_git_command(command)
            print(output)
            if "fatal:" in output.lower() or "merge conflict" in output.lower():
                print("Error encountered.")
                exit(1)
        except subprocess.CalledProcessError as e:
            # Handle Git command error here
            print(f"Error executing command: {command}")
            print(f"Error message: {e.stderr}")
            exit(1)

    print("Done")

if __name__ == "__main__":
    mergeDevIntoMaster()
