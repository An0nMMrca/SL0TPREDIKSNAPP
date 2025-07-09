[app]

title = SL0TPREDIKSNAPP
package.name = slotprediksnapp
package.domain = org.example
source.dir = .
version = 1.0.0
requirements = kivy,cython,numpy,scikit-learn
presplash.filename = icons/splash.png
icon.filename = icons/app_icon.png
include_patterns = icons/*.png
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.ndk = 25.2.9519653
android.entrypoint = org.kivy.android.PythonActivity
android.archs = arm64-v8a,armeabi-v7a
log_level = 2
build_dir = ./.buildozer
copy_mainsource = 1

[buildozer]

build_dir = ./.buildozer
