#!/bin/bash
set -e
curl -fsSL https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.24.5-stable.tar.xz | tar xz
export PATH="$PWD/flutter/bin:$PATH"
flutter config --no-analytics
flutter pub get
flutter build web --web-renderer html