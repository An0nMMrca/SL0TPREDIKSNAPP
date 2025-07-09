[app]

# (str) Title of your application
title = SL0TPREDIKSNAPP

# (str) Package name
package.name = slotprediksnapp

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3, kivy, cython, numpy, scikit-learn, sqlite3

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (bool) Whether to include android.permissions (location, camera, etc)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (str) Android API level
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK Build Tools version
android.build_tools_version = 36.0.0

# (str) Android NDK version
android.ndk = 25b

# (bool) Use Android SDK Commandline tools instead of legacy SDK
android.sdk = commandline

# (str) Android entry point, default is 'org.kivy.android.PythonActivity'
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android archs to build for (armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = arm64-v8a, armeabi-v7a

# (str) Application icon
# icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash screen
# presplash.filename = %(source.dir)s/data/presplash.png

# (list) List of excluded files (or directories) when packaging
# exclude_dirs = tests

# (bool) Copy all the files from the project dir to the package
copy_mainsource = 1

# (bool) Show logcat output during build
log_level = 2

[buildozer]

# (str) Path to buildozer dir (default is ~/.buildozer)
build_dir = ./.buildozer

# (bool) Clean build before building
clean_build = true
