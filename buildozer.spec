[app]
title = G4mbler Predictor
package.name = g4mbler
package.domain = org.kartice.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,db
version = 1.0
requirements = python3,kivy,numpy,scikit-learn,sqlite3,cython
icon.filename = icons/app_icon.png
presplash.filename = icons/splash.png
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 24
android.ndk_path = 
android.sdk_path = 
android.gradle_dependencies = 
android.gradle_plugins = 

android.build_tools_version = 36.0.0

# Include your icons folder
android.add_assets = icons/

# Permissions if needed
android.permissions = INTERNET

# Architecture
android.archs = armeabi-v7a, arm64-v8a

# (optional) Add extra .py files or folders
# source.include_patterns = assets/*,data/*

