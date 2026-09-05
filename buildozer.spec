[app]

# (str) Title of your application
title = NBA2K Universal Converter

# (str) Package name
package.name = nba2kuniversalconverter

# (str) Package domain
package.domain = org.nba2k

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,json,zip,iff,dff,n2km,dds

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


[buildozer]

# (str) Log level
log_level = 2

# (str) Warn if running as root
warn_on_root = 1


[app:android]

# (str) Android API
android.api = 35

# (str) Android minimum API
android.minapi = 24

# (str) Android NDK
android.ndk = 28c

# (str) Android architecture
android.arch = arm64-v8a

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app orientation
android.orientation = portrait

# (bool) Android fullscreen
android.fullscreen = 0

# (str) Android permissions
android.permissions = READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO

# (str) python-for-android branch
p4a.branch = develop


[tool:p4a]

# Keep Python-for-Android focused on the required packages