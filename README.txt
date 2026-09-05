NBA2K Universal Converter V1 - Final Clean Build

This package is a clean V1 build foundation.

Included:
- main.py
- buildozer.spec
- .github/workflows/build.yml

Important V1 build choices:
- Python 3.14
- Buildozer 1.6.0
- Cython 3.1 to <3.4
- python-for-android develop branch
- Android API 35
- Android NDK 28c
- arm64-v8a only
- no pip cache
- no manual sdkmanager step

The previous 20-minute failure was the charset-normalizer Python 3.14 Android wheel problem while using an old/default p4a configuration. This clean package puts p4a.branch and android.archs in [app] and avoids the separate SDK workflow that caused the later fast failure.

V1 is only the Android foundation/file picker. The cross-version NBA 2K14 -> NBA 2K20 Mobile converter and 3D model viewer are planned for V2 after V1 builds successfully.
