import argparse
import struct
import zlib
import itertools

parser = argparse.ArgumentParser(description="PNG Heigh-Width Blasting Tool")
parser.add_argument("file_path", help="PNG file to blast", type=str)
args = parser.parse_args()

# none file_path
if not args.file_path:
    print("Please provide a file path")
    exit()

print("Received file: " + args.file_path)

# read file
binary_data = open(args.file_path, "rb").read()

PNG_SIGNATURE = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"

# check if file is a PNG
if binary_data[:8] != PNG_SIGNATURE:
    print("File is not a PNG")
    exit()

# CRC check
standard_crc = int(binary_data[29:33].hex(), 16)
calculated_crc = zlib.crc32(binary_data[12:29])

print("Standard CRC32: " + hex(standard_crc))
print("Calculated CRC32: " + hex(calculated_crc))

if standard_crc == calculated_crc:
    print("CRC check passed. Everything is fine.")
    exit()

print("CRC check failed. Heigh-Width Blasting start...")

# Bit depth、ColorType、 Compression method、 Filter method、Interlace method
other_attributes = binary_data[24:29]
IHDR_Signature = binary_data[12:16]

# Enumearte all possible heigh-width values
posible_hw = list(itertools.product(range(1, 0x0FFF), range(1, 0x0FFF)))
for height, width in posible_hw:
    calculated_crc = zlib.crc32(
        IHDR_Signature
        + struct.pack(">i", width)
        + struct.pack(">i", height)
        + other_attributes
    )
    if calculated_crc == standard_crc:
        print("Heigh-Width found!")
        print(f"Height: {height}")
        print(f"Width: {width}")
        print("Height(hex): " + "{:08X}".format(height))
        print("Width(hex): " + "{:08X}".format(width))
        exit()
