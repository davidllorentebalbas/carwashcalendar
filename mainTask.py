from PIL import Image 
from calendarGenerator import calendargen

calendargen([(2024, 7, 2), (2024, 7, 12),(2024, 7, 18),(2024, 7, 17)])



# Opening the primary image (used in background) 
img1 = Image.open(r"carWashAmazingWallpaper.png") 
  
# Opening the secondary image (overlay image) 
img2 = Image.open(r"calendar_carwash.png") 

# Cropping
width, height = img2.size
new_width = 590
new_height = 590

left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2

img_cropped = img2.crop((left, top, right, bottom))
img_cropped=img_cropped.resize((546,545))
img_cropped.save("calendarcropped.png")

# Pasting img2 image on top of img1  

img1.paste(img_cropped, (1245,490), mask = img_cropped) 
  
# Displaying the image 
img1.save("carWashPersonalised.png")