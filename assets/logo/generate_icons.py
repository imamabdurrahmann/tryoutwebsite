"""Generate app icons for TryOutCPNS"""
from PIL import Image
import os

SOURCE = r"C:\Users\muham\Downloads\Stylized Book and Wings Logo.png"
OUT_DIR = r"C:\Users\muham\tryout_cpns\assets\logo"

def main():
    img = Image.open(SOURCE).convert('RGBA')
    print(f"Loaded: {img.size}")

    # Windows ICO sizes
    for size in [16, 32, 48, 64, 128, 256]:
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(f"{OUT_DIR}/icon_{size}.png", 'PNG')
        print(f"Created icon_{size}.png")

    # Android sizes
    for size in [48, 72, 96, 144, 192]:
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(f"{OUT_DIR}/android_{size}.png", 'PNG')
        print(f"Created android_{size}.png")

    # iOS sizes
    for size in [20, 29, 40, 58, 60, 76, 80, 87, 120, 152, 167, 180, 1024]:
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(f"{OUT_DIR}/ios_{size}.png", 'PNG')
        print(f"Created ios_{size}.png")

    print("\n✅ All icons generated!")

if __name__ == "__main__":
    main()
