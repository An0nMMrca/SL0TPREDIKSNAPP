[app]
title = G4mbler
package.name = g4mbler
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,numpy,cython
orientation = portrait
fullscreen = 1

# (Opcioni) Ikonice i splash
icon.filename = %(source.dir)s/icons/icon.png

# Android specifično
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 25b
source.dir = .
# Use SDL2 bootstrap
p4a.bootstrap = sdl2


# Allow multiple architectures
android.archs = armeabi-v7a, arm64-v8a

# Ostalo po potrebi
