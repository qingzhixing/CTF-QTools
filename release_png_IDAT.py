import argparse
import zlib

parser = argparse.ArgumentParser(description="Release Files in PNG IDAT")
parser.add_argument("png_path", help="The png file containing files to be released")
args = parser.parse_args()

png_data = open(args.png_path, "rb").read()

# Find the start of the IDAT chunk
idat_start = png_data.find(b"IDAT")

# Find the end of the IDAT chunk
idat_end = png_data.find(b"IEND", idat_start)
