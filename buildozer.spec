[app]

title = SL0TPREDIKSNAPP
package.name = slotprediksnapp
package.domain = org.example
source.dir = .

version = 1.0.0

requirements = python3, kivy, cython, numpy, scikit-learn, sqlite3

orientation = portrait
fullscreen = 1

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.sdk = commandline

android.entrypoint = org.kivy.android.PythonActivity
android.archs = arm64-v8a, armeabi-v7a

# DATA (ikone i slike)
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/splash.png

# Kopiraj sve podatke
copy_mainsource = 1

# Isključi nepotrebne direktorijume
exclude_dirs = tests

# Uključi folder data u APK
include_exts = png,jpg,kv,atlas,ttf
source.include_exts = py,png,jpg,kv,atlas,ttf
android.add_src = data/

log_level = 2

[buildozer]
build_dir = ./.buildozer
clean_build = false
