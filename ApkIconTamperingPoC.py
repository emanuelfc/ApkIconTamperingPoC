#!/usr/bin/env python3

import glob
from lib.ToolNotFoundException import ToolNotFoundException
import os
import subprocess
from lib.imageTampering import alterImage
from lib.args import args
import shutil

TARGET_IMAGE_NAME = "ic_launcher*.png"
TARGET_IMAGE_BASE_DIRECTORY = "res/**/"

def runCommand(command):
	result = subprocess.run(command)
	result.check_returncode()

def createTamperPOC(packageLocation: str, outputLocation: str) -> None:
	packageName, _ = os.path.splitext(os.path.split(packageLocation)[1])

	# Decompile Package

	print("Decompiling package...")
	runCommand([APKTOOL, 'd', '-r', '-s', packageLocation, '-o', outputLocation])

	# Get all target images

	imagesLocation = os.path.join(outputLocation, TARGET_IMAGE_BASE_DIRECTORY)
	targetImages = glob.glob(os.path.join(imagesLocation, TARGET_IMAGE_NAME), recursive=True)

	# Alter target images

	print("Changing images...")
	for targetImage in targetImages:
		print(targetImage)
		alterImage(targetImage)

	# Compile tampered Package

	compilationPath = os.path.join(outputLocation, "dist")

	tamperedPackageName = packageName + "-tampered"

	print("Compiling tampered app...")
	runCommand([APKTOOL, 'b', outputLocation, '-o', os.path.join(compilationPath, tamperedPackageName + ".apk")])

	# Sign tampered package

	signedPackageName = tamperedPackageName + "-signed"

	print("Signing tampered package...")
	runCommand([D2J_APK_SIGN, os.path.join(compilationPath, tamperedPackageName + ".apk"), "-o", os.path.join(compilationPath, signedPackageName + ".apk")])

	# Align tampered package

	alignedPackageName = signedPackageName + "-aligned"

	print("Aligning signed tampered package...")
	runCommand([ZIPALIGN, '-p', '4', os.path.join(compilationPath, signedPackageName + ".apk"), os.path.join(compilationPath, alignedPackageName + ".apk")])

def getTool(executableName: str, envVar: str) -> str:

	tool = shutil.which(executableName, mode = os.F_OK | os.X_OK)

	if tool:
		return tool
	
	try:
		tool = os.environ[envVar]
	except KeyError:
		raise ToolNotFoundException(executableName)

APKTOOL = getTool('apktool', 'APKTOOL')
D2J_APK_SIGN = getTool('d2j-apk-sign', 'D2J_APK_SIGN')
ZIPALIGN = getTool('zipalign', 'ZIPALIGN')

if __name__ == "__main__":
	createTamperPOC(args.package, args.output)