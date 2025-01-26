import struct

def read_bmp(file_path):
    """Reads the BMP file and extracts pixel RGB data as if the image is flipped vertically."""
    with open(file_path, 'rb') as f:
        f.seek(10)
        pixel_offset = struct.unpack('<I', f.read(4))[0]
        
        f.seek(18)
        width = struct.unpack('<I', f.read(4))[0]
        height = struct.unpack('<I', f.read(4))[0]
        
        f.seek(28)
        bits_per_pixel = struct.unpack('<H', f.read(2))[0]
        
        if bits_per_pixel != 24:
            raise ValueError("This script supports 24-bit BMP files only.")
        
        f.seek(pixel_offset)
        pixels = []
        padding = (4 - (width * 3) % 4) % 4
        
        for y in range(height):
            row = []
            for x in range(width):
                b = ord(f.read(1))
                g = ord(f.read(1))
                r = ord(f.read(1))
                row.append((r, g, b))
            pixels.append(row)
            f.read(padding)  # Skip padding
        
        # Flip the image vertically
        flipped_pixels = []
        for row in reversed(pixels):
            flipped_pixels.extend(row)
        
        return flipped_pixels

def write_pal(pixels, output_path):
    """Writes the .PAL file in JASC-PAL format with the given pixel data."""
    with open(output_path, 'w') as f:
        f.write("JASC-PAL\n")
        f.write("0100\n")
        f.write(f"{min(256, len(pixels))}\n")
        
        for i, color in enumerate(pixels[:256]):
            r, g, b = color
            f.write(f"{r} {g} {b}\n")

def bmp_to_pal(bmp_file, pal_output):
    """Main function to convert BMP pixel data to a .PAL file."""
    pixels = read_bmp(bmp_file)
    write_pal(pixels, pal_output)

# Example usage:
bmp_file_path = r'pal\testpal1.bmp'
pal_file_path = r'pal\testpal.pal'
bmp_to_pal(bmp_file_path, pal_file_path)

print(f".PAL file generated at {pal_file_path}")
