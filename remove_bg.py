from rembg import remove
from PIL import Image

input_path = 'assets/logo_nova.png'
output_path = 'assets/logo_transparent.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
