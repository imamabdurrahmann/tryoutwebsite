#!/bin/bash
cd /c/Users/muham/tryout_cpns

echo "Building Flutter web..."
flutter build web

echo "Deploying to Vercel..."
cd build/web
vercel --prod -y

echo "Adding alias..."
DEPLOY_URL=$(vercel ls 2>/dev/null | grep -oP 'https://[^ ]+' | head -1 | sed 's/https:\/\///')
vercel alias add $DEPLOY_URL jagoancpns.vercel.app

echo "Done! https://jagoancpns.vercel.app"