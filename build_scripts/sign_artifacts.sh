#!/bin/bash
set -e

KEY_ID="52BCCD17AD95D0A64ADBB73F2AC31B2120605AA5"  # Robert Shubert GPG RSA Key ID
BUILD_DIR="../signed_builds"

mkdir -p "$BUILD_DIR"

echo "🔐 Signing all artifacts in $BUILD_DIR"
for file in "$BUILD_DIR"/*; do
  [ -f "$file" ] || continue
  echo "✍️ Signing $file..."
  gpg --default-key "$KEY_ID" --output "$file.sig" --detach-sign "$file"
done

echo "✅ All artifacts signed with key $KEY_ID"
