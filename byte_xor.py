import argparse


def xor_bytes(data, key):
    return bytes([data[i] ^ key for i in range(len(data))])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="XOR bytes with a key")
    parser.add_argument("data_file", type=str, help="data to be XORed")
    parser.add_argument("key", type=str, help="key to XOR with")
    args = parser.parse_args()

    data = open(args.data_file, "rb").read()

    key = int(args.key, 16)
    result = xor_bytes(data, key)

    with open(args.data_file + ".xor", "wb") as f:
        f.write(result)
