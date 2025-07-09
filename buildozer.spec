[app]
title = CardPredictor
package.name = cardpredictor
package.domain = org.karta.predikcija
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*

version = 1.0
requirements = python3,kivy,numpy,scikit-learn
orientation = portrait

fullscreen = 1
icon.filename = assets/icon.png
presplash.filename = assets/splash.png

# Android permissions
android.permissions = INTERNET

# Entry point
entrypoint = main.py

# Android specific
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True

# This enables OpenGL ES 2.0 which is needed for Kivy
android.opengl_es2 = True

# Hide the title bar
android.hide_title = 1

# Enable logcat
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
