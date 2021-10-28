# ApkIconTamperingPoC

Creates PoC Android apps with its Icons modified to rapidly test application tampering.
<br><br>

## Description

Automatically modifies the "ic_launcher.png" icons with stripped red lines, and creates the tampered app. For the purpose of rapidly testing Android application tampering during Penetration Tests.

<br><br>

## Requirements

Python3
argparse
Pillow
shutil
glob

## Usage

```
usage: ApkIconTamperingPoC.py [-h] -p PACKAGE -o OUTPUT

Android Application Icon Tampering PoC - Automatically modifies the "ic_launcher.png" icons with stripped red lines,
and creates the tampered app.

optional arguments:
  -h, --help            show this help message and exit
  -p PACKAGE, --package PACKAGE
                        Target Application package (.apk file)
  -o OUTPUT, --output OUTPUT
                        Output Location for Tampered Application
```

<br>

### Example:

Creates the PoC app for the given apk file, and saves PoC apk directory - with the name 'PACKAGE-tampered-signed-aligned.apk'.
```text
python3 ApkIconTamperingPoC.py -l "com.example.exampleApp"
```

The tampered package name is quite lengthy, but this intentional as a version is created for each stage (Tampering, Signing, Aligning). This allows better control.

<br>
