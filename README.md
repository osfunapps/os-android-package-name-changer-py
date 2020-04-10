Introduction
------------

Run this module to change your android app's package name externally.

## Installation
Install via pip:

    pip install os-android-package-name-changer

## Usage       
From python:
    
    import os_android_package_name_changer.NameChanger as nc;
    nc.change_package_name('path/to/android/project', 'com.new.packagename')
  
From the command line:

    python3 -c 'import os_android_package_name_changer.NameChanger as nc;nc.change_package_name("path/to/android/project", "com.new.packagename")'

## Licence
MIT