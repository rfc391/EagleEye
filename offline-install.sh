#!/bin/bash
set -e

echo "🔐 EagleEye Secure Offline Installer"
echo "-------------------------------------"

# Verify GPG signature of this installer if present
if [ -f offline-install.sh.sig ]; then
    echo "🔍 Verifying GPG signature..."
    gpg --verify offline-install.sh.sig offline-install.sh || {
        echo "❌ GPG signature verification failed."
        exit 1
    }
    echo "✅ Signature OK"
fi

# Create virtual environment
echo "📦 Setting up virtualenv..."
python3 -m venv eagleeye-env
source eagleeye-env/bin/activate

# Install dependencies from offline mirror
echo "⬇️ Installing packages from offline mirror..."
pip install --no-index --find-links=offline_packages -r requirements.lock.txt

# Optional: Start the app
echo "✅ Installation complete."
echo "To run: source eagleeye-env/bin/activate && python3 src/main.py"
