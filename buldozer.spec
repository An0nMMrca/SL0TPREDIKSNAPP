[app]

# General
title = SL0TPREDIKSNAPP
package.name = slotprediksnapp
package.domain = org.example
source.dir = .
version = 1.0.0
orientation = portrait
fullscreen = 1

# Entry point
source.include_exts = py,png,jpg,kv,atlas,ttf
android.entrypoint = org.kivy.android.PythonActivity
copy_mainsource = 1

# Requirements (Python packages and Android dependencies)
requirements = python3,kivy,cython,numpy,scikit-learn

# Presplash and icon
icon.filename = icons/app_icon.png
presplash.filename = icons/splash.png

# Include assets (card images etc.)
include_patterns = icons/*.png

# Permissions
android.permissions = INTERNET

# Android SDK/API setup
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.archs = arm64-v8a,armeabi-v7a

# Log level
log_level = 2

# Build directory
[buildozer]
build_dir = .buildozer
warn_on_root = 1

