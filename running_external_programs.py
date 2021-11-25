import subprocess

# older approach
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

# new approach
# completed = subprocess.run(['ls', '-l', '-a'])
# completed = subprocess.run(['ls', '-a'], capture_output=True, text=True)
# completed = subprocess.run(['python3', 'other.py'],
#                            capture_output=True, text=True)
# completed = subprocess.run(
#     ['false'], capture_output=True, text=True)
try:
    completed = subprocess.run(
        ['false'], capture_output=True, text=True, check=True)
    print(type(completed))
    print('args', completed.args)
    print('returncode', completed.returncode)
    print('stdout', completed.stdout)
    print('stderr', completed.stderr)

    if completed.returncode != 0:
        print(completed.stderr)

except subprocess.CalledProcessError as e:
    print(e)
