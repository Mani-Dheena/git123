#Converts Color Image to Black and White

# Install Pillow library using pip command

#pip install pillow

#Python Pillow Library import
from PIL import Image

input_image = 'c:/black/luffy.jpg'

# Open the input image
img = Image.open(input_image)

#Covert the image to grayscale
bw_image = img.convert('L')

output_image = 'c:/black/output_image_bw.jpg'
# Save the converted image
bw_image.save(output_image)

print(f"Converted image saved as: {output_image}")
