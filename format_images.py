
#%%
import glob
import pathlib
from PIL import Image


#%%
pathlib.Path('formatted_images').mkdir(parents=True, exist_ok=True) 


#%%
image_file_path = pathlib.Path('images')
image_file_list = list(image_file_path.glob("*.jpg"))


#%%
for image_file in image_file_list:
    image = Image.open(image_file)
    greyscale_image = image.convert(mode="L").resize(size=(1024, 683))
    greyscale_image.save(pathlib.Path(f"formatted_images/{image_file.name}"))


