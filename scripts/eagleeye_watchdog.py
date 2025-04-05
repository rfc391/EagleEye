#!/usr/bin/env python3
import subprocess
import time
import os
import signal

PROCESS_NAME = "cli.py"
PROCESS_PATH = "/opt/eagleeye/src/cli.py"

def is_process_running():
    try:
        output = subprocess.check_output(["pgrep", "-f", PROCESS_NAME])
        return bool(output.strip())
    except subprocess.CalledProcessError:
        return False

def start_process():
    print("[WATCHDOG] Starting EagleEye...")
    return subprocess.Popen(["python3", PROCESS_PATH])

def main():
    print("[WATCHDOG] EagleEye watchdog is now active.")
    process = None

    while True:
        if not is_process_running():
            if process:
                try:
                    os.kill(process.pid, signal.SIGTERM)
                except Exception:
                    pass
            process = start_process()
        time.sleep(10)

if __name__ == "__main__":
    main()