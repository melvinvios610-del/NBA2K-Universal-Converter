
[app]
title = NBA2K Universal Converter
package.name = nba2kuniversalconverter
package.domain = org.nba2ktools
source.dir = .
source.include_exts = py,png,jpg,kv,json,bin
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 35
android.minapi = 23
android.archs = arm64-v8a,armeabi-v7a
