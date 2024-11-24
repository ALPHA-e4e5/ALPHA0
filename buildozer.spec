[app]
# (str) Title of your application
title = AirMouse

# (str) Package name
package.name = airmouse

# (str) Package domain (must be unique to avoid conflicts with other apps)
package.domain = org.example.airmouse

# (str) Source files to include in the APK
source.include_exts = py,png,jpg,kv

# (list) Application requirements
# Include dependencies such as kivy, plyer, and pyserial for USB communication
requirements = python3, kivy, plyer, pyserial

# (str) Supported orientation (portrait, landscape, sensor, or all)
orientation = portrait

# (bool) Enable fullscreen mode (no status bar)
fullscreen = 1

# (list) Permissions required by the app
# Add USB permissions for communication
android.permissions = INTERNET, ACCESS_NETWORK_STATE, USB_PERMISSION

# (int) Target Android API version
android.api = 30

# (int) Minimum Android API version
android.minapi = 21

# (str) The build tool to use (python3, p4a)
p4a.branch = stable

# (str) Presplash image
presplash.filename = assets/presplash.png

# (str) Icon for the application
icon.filename = assets/icon.png

# (list) Presplash animation (leave blank if not required)
presplash_color = #FFFFFF

# (bool) Add numeric version to APK filename to differentiate builds
version = 1.0.0

[buildozer]
# (str) Path to the project's source code directory
#source.dir = .

# (bool) Copy only source files into the APK, skipping unused dependencies
copy_to_bin = False

# (str) Specify debug or release build (debug by default)
debug = 1

[android]
# (list) Additional Java classes and JARs to include (for advanced features)
android.add_jars = 

# (str) Specify architecture for APK builds (armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = arm64-v8a, armeabi-v7a

# (str) Set NDK version (update if required by your system)
android.ndk = 21b

# (list) Additional environment variables for Android build
android.environment = ANDROID_NDK_HOME=$HOME/.buildozer/android/platform/android-ndk-r21b

# (bool) Build both .apk and .aab files
android.aab = False
