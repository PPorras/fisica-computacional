def write_file(name, binary=False):
    """Create a file and write several lines (text or binary)."""
    mode = 'wb' if binary else 'w'
    with open(name, mode) as f:
        for i in range(2**10):
            line = "This is a test line\n"
            f.write(line.encode() if binary else line)


def read_file(name, num_lines=5, num_chars=10, binary=False):
    """Read part of the file and show its content (text or binary)."""
    mode = 'rb' if binary else 'r'
    for i in range(num_lines):
        with open(name, mode) as f:
            data = f.readline(num_chars)
            if binary:
                data = data.decode(errors='ignore')
            print(f"Line {i+1}: {data.strip()}")


def append_file(name, binary=False):
    """Append a line at the end of the file (text or binary)."""
    mode = 'ab' if binary else 'a'
    with open(name, mode) as f:
        line = "This line goes at the end\n"
        f.write(line.encode() if binary else line)


if __name__ == "__main__":
    file_name = "file.txt"

    print("=== TEXT MODE ===")
    write_file(file_name)
    read_file(file_name)
    append_file(file_name)

    print("\n=== BINARY MODE ===")
    file_name_bin = "file.bin"
    write_file(file_name_bin, binary=True)
    read_file(file_name_bin, binary=True)
    append_file(file_name_bin, binary=True)

    print("\nProcess completed successfully.")

