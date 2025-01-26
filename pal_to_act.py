def read_jasc_pal(pal_file):
    """Reads a JASC-PAL file and extracts the RGB values."""
    with open(pal_file, 'r') as f:
        lines = f.readlines()

    # Ensure this is a valid JASC-PAL file
    if lines[0].strip() != "JASC-PAL" or lines[1].strip() != "0100":
        raise ValueError("Not a valid JASC-PAL file")

    # The number of colors in the palette
    num_colors = int(lines[2].strip())
    colors = []

    # Extract the RGB values
    for line in lines[3:3 + num_colors]:
        r, g, b = map(int, line.strip().split())
        colors.append((r, g, b))

    return colors

def write_act_file(colors, act_file):
    """Writes the colors into an .ACT file format."""
    with open(act_file, 'wb') as f:
        # Write the RGB values (up to 256 colors)
        for i, (r, g, b) in enumerate(colors):
            f.write(bytes([r, g, b]))
        
        # If there are fewer than 256 colors, pad the remaining with 0
        for _ in range(256 - len(colors)):
            f.write(bytes([0, 0, 0]))

        # No additional metadata (optional), so just write the file up to 768 bytes

def pal_to_act(pal_file, act_file):
    """Converts a JASC-PAL file to a .ACT palette."""
    colors = read_jasc_pal(pal_file)
    write_act_file(colors, act_file)

# Example usage:
pal_file_path = r'pal\testpal.pal'
act_file_path = r'pal\testpal.act'

# Convert the JASC-PAL file to an .ACT file
pal_to_act(pal_file_path, act_file_path)

print(f".ACT file generated at {act_file_path}")
