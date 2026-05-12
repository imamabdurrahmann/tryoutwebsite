#!/bin/bash
set -e

# Download and extract Flutter
echo "Downloading Flutter..."
curl -fsSL https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.24.5-stable.tar.xz | tar xz

# Add Flutter to PATH
export PATH="$PWD/flutter/bin:$PATH"

# Disable analytics
flutter config --no-analytics

# Precache Flutter
flutter precache

# Get dependencies
flutter pub get

# Build for web
flutter build web --web-renderer html

echo "Build completed!"