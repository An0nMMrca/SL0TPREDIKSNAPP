[app]

# Osnovno
title = G4mbler
package.name = g4mbler
package.domain = org.example
source.dir = .

# Verzija
version = 0.1

# Ekstenzije koje se uključuju
source.include_exts = py,png,jpg,kv,atlas

# Zahtevi
requirements = python3,kivy,numpy,cython

# Orijentacija i fullscreen
orientation = portrait
fullscreen = 1

# Ikonica
icon.filename = icons/icon.png

# Android podešavanja
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.ndk = 25b
android.permissions = INTERNET

# Bootstrap
p4a.bootstrap = sdl2

# Arhitekture
android.archs = armeabi-v7a, arm64-v8a

# Log nivo
log_level = 2

# Kopiraj main.py i ceo source
copy_mainsource = 1

# Buildozer build folder
[buildozer]
build_dir = ./.buildozer
