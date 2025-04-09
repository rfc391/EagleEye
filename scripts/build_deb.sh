#!/bin/bash

set -e

APP_NAME="eagleeye"
VERSION="1.0.0"
ARCH="amd64"
BUILD_DIR="dist/${APP_NAME}_${VERSION}_${ARCH}"

echo "[DEB] Creating DEB package structure..."
mkdir -p ${BUILD_DIR}/DEBIAN
mkdir -p ${BUILD_DIR}/opt/${APP_NAME}

cp -r src config scripts requirements.txt ${BUILD_DIR}/opt/${APP_NAME}/
cp -r debian/control debian/postinst ${BUILD_DIR}/DEBIAN/

chmod 755 ${BUILD_DIR}/DEBIAN/postinst

echo "[DEB] Building package..."
dpkg-deb --build ${BUILD_DIR}

echo "[DEB] Package built at ${BUILD_DIR}.deb"