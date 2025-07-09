[app]

title = SL0TPREDIKSNAPP
package.name = slotprediksnapp
package.domain = org.example
source.dir = .
version = 1.0.0
requirements = python3,kivy,cython,numpy,scikit-learn,sqlite3
orientation = portrait
fullscreen = 1
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.ndk = 25.2.9519653
android.sdk = commandline
android.entrypoint = org.kivy.android.PythonActivity
android.archs = arm64-v8a, armeabi-v7a
copy_mainsource = 1
log_level = 2

[buildozer]

build_dir = ./.buildozer
clean_build = true
