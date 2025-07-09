[app]

title = SL0TPREDIKSNAPP
package.name = slotprediksnapp
package.domain = org.example
source.dir = .
version = 1.0.0
requirements = kivy, cython, numpy, scikit-learn
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.ndk = 25b
android.sdk = commandline
android.entrypoint = org.kivy.android.PythonActivity
android.archs = arm64-v8a, armeabi-v7a
log_level = 2

[buildozer]

build_dir = ./.buildozer
clean_build = true
