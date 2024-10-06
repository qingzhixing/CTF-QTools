import argparse

parser = argparse.ArgumentParser(description="File Hex to ASCII Char Count")
parser.add_argument("file_path", help="File path to count ASCII characters", type=str)
args = parser.parse_args()

# none file_path
if not args.file_path:
    print("Please provide a file path")
    exit()

print("Received file: " + args.file_path)

# read file
binary_data = open(args.file_path, "rb").read()

bin2asc = ""
for byte in binary_data:
    bin2asc += chr(byte)

print("ASCII Characters: \n" + bin2asc)

# count ASCII characters
map = {}
for char in bin2asc:
    if char in map:
        map[char] += 1
    else:
        map[char] = 1

for key, value in map.items():
    print(key + ": " + str(value))

# sort by value
sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)

print("Sorted by value: ")
for key, value in sorted_map:
    print(key + ": " + str(value))

print("Sorted string: ")
sorted_string = "".join(sorted_map[i][0] for i in range(len(sorted_map)))
print(sorted_string)
