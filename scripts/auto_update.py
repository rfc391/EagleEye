#!/usr/bin/env python3
import requests
import subprocess
import os

REPO = "rfc391/EagleEye"
BRANCH = "main"
TARGET_DIR = "/opt/eagleeye"

def update_repo():
    print("[UPDATE] Checking for updates from GitHub...")
    if not os.path.exists(TARGET_DIR):
        subprocess.run(["git", "clone", f"https://github.com/{REPO}.git", TARGET_DIR])
    else:
        subprocess.run(["git", "-C", TARGET_DIR, "pull", "origin", BRANCH])
    print("[UPDATE] Repo update complete.")

def install_requirements():
    req_path = os.path.join(TARGET_DIR, "requirements.txt")
    if os.path.exists(req_path):
        subprocess.run(["pip3", "install", "-r", req_path])
        print("[UPDATE] Dependencies updated.")

if __name__ == "__main__":
    update_repo()
    install_requirements()