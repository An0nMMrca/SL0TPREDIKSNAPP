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

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0
android.ndk = 25.2.9519653
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET
android.add_assets = icons/
