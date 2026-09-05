[app]
title = NBA2K Universal Converter
package.name = nba2kuniversalconverter
package.domain = org.nba2k

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,json,zip,iff,dff,n2km,dds

version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a

android.entrypoint = org.kivy.android.PythonActivity
android.orientation = portrait
android.fullscreen = 0
android.permissions = READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO

# Python 3.14 support / current p4a fixes
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
