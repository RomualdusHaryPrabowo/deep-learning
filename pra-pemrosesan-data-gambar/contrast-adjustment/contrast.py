import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

# Membaca citra
image_path = "kucing.jpg"
image = Image.open(image_path)

# Menampilkan citra asli
plt.figure(figsize=(8, 4))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis('off')

#Transformasi untuk penyesuaian kontras (hingga +50%)
contrast_adjustment = transforms.Compose([
 transforms.ColorJitter(contrast=(1, 1.5)) # Penyesuaian kontras hingga sebesar +50%
])
high_contrast_image = contrast_adjustment(image)

# Menampilkan citra setelah penyesuaian kontras
plt.subplot(1, 3, 2)
plt.title("High Contrast Image")
plt.imshow(high_contrast_image)
plt.axis('off')

# Transformasi untuk penyesuaian kontras (hingga -50%)
low_contrast_adjustment = transforms.Compose([
 transforms.ColorJitter(contrast=(0.5, 1)) # Penyesuaian kontras hingga sebesar -50%
])
low_contrast_image = low_contrast_adjustment(image)

# Menampilkan citra setelah penyesuaian kontras
plt.subplot(1, 3, 3)
plt.title("Low Contrast Image")
plt.imshow(low_contrast_image)
plt.axis('off')

plt.tight_layout()
plt.show()