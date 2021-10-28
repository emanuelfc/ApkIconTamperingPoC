import argparse

parser = argparse.ArgumentParser(description = 'Android Application Icon Tampering PoC - Automatically modifies the "ic_launcher.png" icons with stripped red lines, and creates the tampered app.')

parser.add_argument('-p', '--package', dest = 'package', required = True, help = 'Target Application package (.apk file)')
parser.add_argument('-o', '--output', dest = 'output', required = True, help = 'Output Location for Tampered Application')

args = parser.parse_args()