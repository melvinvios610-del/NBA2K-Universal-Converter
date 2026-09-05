[app]

# (str) Title of your application
title = NBA2K Universal Converter

# (str) Package name
package.name = nba2kuniversalconverter

# (str) Package domain
package.domain = org.nba2k

# (str) Source code directory
source.dir = .

# (list) Source file extensions to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,json,zip,iff,dff,n2km,dds

# (str) Application version
version = 1.0

# (list) Python-for-Android requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# Android configuration
android.api = 35
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a

# Use the current python-for-android development branch.
# This is important for the Python 3.14 / charset-normalizer Android wheel fix.
p4a.branch = develop

# Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# Android UI settings
android.orientation = portrait
android.fullscreen = 0

# Android media permissions
android.permissions = READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO

[buildozer]

# Buildozer log level
log_level = 2

# Allow Buildozer to run as root in CI
warn_on_root = 1
