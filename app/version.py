import subprocess

PROJECT_NAME = "fastapi-helloworld"

def get_git_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
    except Exception:
        return "unknown"

