# Python code to combine 4 figures in 2 x 2 form keeping the resolution of whole figures as 300 dpi
from PIL import Image
import matplotlib.pyplot as plt

# Load the 4 images
img1 = Image.open("Rg-chain1-270T.png")
img2 = Image.open("Rg-chain2-270T.png")
img3 = Image.open("Rg-chain3-270T.png")
img4 = Image.open("Rg-chain4-270T.png")

# Ensure all images are same size (optional: resize if not)
width, height = img1.size

# Create a blank canvas (2x2)
combined = Image.new("RGB", (2 * width, 2 * height), "white")

# Paste images
combined.paste(img1, (0, 0))
combined.paste(img2, (width, 0))
combined.paste(img3, (0, height))
combined.paste(img4, (width, height))

# Save with 300 dpi
combined.save("Rg_chains_270T.png", dpi=(300, 300))

