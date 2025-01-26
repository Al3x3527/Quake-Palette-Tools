def read_jasc_pal(pal_file):
    """Reads a JASC-PAL file and extracts the RGB values."""
    with open(pal_file, 'r') as f:
        lines = f.readlines()

    # Ensure this is a valid JASC-PAL file
    if lines[0].strip() != "JASC-PAL" or lines[1].strip() != "0100":
        raise ValueError("Not a valid JASC-PAL file")

    # Extract the number of colors and RGB values
    num_colors = int(lines[2].strip())
    colors = []

    for line in lines[3:3 + num_colors]:
        r, g, b = map(int, line.strip().split())
        colors.append((r, g, b))

    return colors

def write_hex_palette(colors, hex_file):
    """Writes the colors to a Python file as a hexadecimal palette."""
    with open(hex_file, 'w') as f:
        f.write("newpal = (\n")
        for r, g, b in colors:
            f.write(f"    (0x{r:02X}, 0x{g:02X}, 0x{b:02X}),\n")
        f.write(")\n")

def pal_to_hex(pal_file, hex_file):
    """Converts a JASC-PAL file to a Python file with a hexadecimal palette."""
    colors = read_jasc_pal(pal_file)
    write_hex_palette(colors, hex_file)

# Example usage:
pal_file_path = r'pal\input_pal.pal'
hex_file_path = r'pal\output_pal.py'

# Convert the JASC-PAL file to a Python .py file with a hexadecimal palette
pal_to_hex(pal_file_path, hex_file_path)

print(f"Hexadecimal palette saved to {hex_file_path}")
