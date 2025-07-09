[app]
...
# (bool) Include Cython (for compiling Python extensions)
cython = true
title = SL0TPREDIKSNAPP
package.name = slotprediksnapp
package.domain = org.example
source.dir = .
version = 1.0.0

# Python i biblioteke
requirements = python3,kivy,cython,numpy,scikit-learn

# Ikone i slike
icon.filename = icons/app_icon.png
presplash.filename = icons/splash.png
include_patterns = icons/*.png

# UI podešavanja
orientation = portrait
fullscreen = 1

# Android dozvole
android.permissions = INTERNET

# Android podešavanja
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.entrypoint = org.kivy.android.PythonActivity
android.archs = arm64-v8a,armeabi-v7a

# Ostalo
log_level = 2
copy_mainsource = 1
allow_backup = 1

[buildozer]

# Build folder lokalno
build_dir = ./.buildozer

# Clean build svaki put? (opcionalno)
# clean_build = 1
