[app]

# (str) Title of your application
title = SL0TPREDIKSNAPP

# (str) Package name
package.name = slotprediksnapp

# (str) Package domain (unique, reverse domain-style)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = kivy,cython,numpy,scikit-learn

# (str) Presplash of the application
presplash.filename = icons/splash.png

# (str) Icon of the application
icon.filename = icons/app_icon.png

# (list) Include patterns for source files
include_patterns = icons/*.png

# (list) Supported orientations
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (int) Target API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android build tools version
android.build_tools_version = 33.0.0

# (str) Android NDK version
android.ndk = 25.2.9519653

# (str) Entry point for your application
android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported architectures
android.archs = arm64-v8a,armeabi-v7a

# (int) Log level (0 = error, 1 = warning, 2 = info, 3 = debug, 4 = trace)
log_level = 2

# (str) Directory for buildozer build files
build_dir = ./.buildozer

# (bool) Copy the main source file to the target (1) or not (0)
copy_mainsource = 1

# (str) Additional source extensions to include (not needed if include_patterns is set)
# source.include_exts = py,png,jpg,kv,atlas

# (str) Additional patterns to exclude (if needed)
# exclude_patterns = tests/*,docs/*

[buildozer]

# (str) Build directory (default: .buildozer)
build_dir = ./.buildozer

# (bool) Clean build (not needed, handled by GitHub Actions)
# clean_build = true
