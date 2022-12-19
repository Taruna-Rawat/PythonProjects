import sys
import os
from PIL import Image

#grab arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder,output_folder)
#check path
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
   
#file in loop
for filename in os.listdir(image_folder) :
    img=Image.open(f'{image_folder}{filename}')
    cleaname = os.path.splitext(filename)[0]
    img.save(f'{output_folder}/{cleaname}.png','png')
    print('all done')

