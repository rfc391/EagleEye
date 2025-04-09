#!/usr/bin/env python3
import subprocess
import os

requirements_file = "../requirements.lock.txt"
download_dir = "../offline_packages"

os.makedirs(download_dir, exist_ok=True)

subprocess.run([
    "pip", "download",
    "-r", requirements_file,
    "-d", download_dir
])
print(f"✅ All packages downloaded to: {download_dir}")
