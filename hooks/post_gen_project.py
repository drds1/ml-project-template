import subprocess

subprocess.run(["poetry", "install"])
subprocess.run(["poetry", "run", "pre-commit", "install"])