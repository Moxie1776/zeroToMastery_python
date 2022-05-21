import os
import sys

from PIL import Image  # , ImageFilter

image_sourceFolder = sys.argv[1] if sys.argv[1] else './images'
image_destinationFolder = sys.argv[2] if sys.argv[2] else './images/png'

if not os.path.exists(image_destinationFolder):
  os.makedirs(image_destinationFolder)

for filename in os.listdir(image_sourceFolder):
  clean_name = os.path.splitext(filename)[0]
  extension_name = os.path.splitext(filename)[1]
  if extension_name in ['.jpeg', '.jpg']:
    img = Image.open(f'{image_sourceFolder}{filename}')
    img.save(f'{image_destinationFolder}/{clean_name}.png', 'png')
    print(f'Converted: {clean_name}{extension_name}')
  if extension_name not in ['.jpeg', '.jpg']:
    print(f'Skipped: {clean_name}', extension_name)
