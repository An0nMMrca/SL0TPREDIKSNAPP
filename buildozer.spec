[app]
title = G4mbler Predictor
package.name = g4mbler
package.domain = org.kartice.ai
source.dir = .
source.include_exts = py,png,jpg,kv,ttf,db
version = 1.0
requirements = python3,kivy,numpy,scikit-learn,sqlite3,cython
icon.filename = icons/app_icon.png
fullscreen = 1

# Assets folder za slike i ikonice
android.add_assets = icons/

# Kompresija logova
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
# Android API i NDK
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk_path = ~/.buildozer/android/platform/android-sdk
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET

# build-tools verzija
android.build_tools_version = 34.0.0

# Omogući sklapanje C biblioteka
android.copy_libs = 1

# Ako koristiš sqlite3, ovo pomaže kod builda
android.sqlite3 = True

# Onemogući proguard (ili uključi kasnije za release)
android.enable_proguard = 0
