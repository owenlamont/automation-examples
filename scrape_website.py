
#%%
from bs4 import BeautifulSoup
from os.path import basename
import requests
import os
import shutil
import pathlib


#%%
pathlib.Path('images').mkdir(parents=True, exist_ok=True) 


#%%
page_link = 'https://unsplash.com/search/photos/desktop-background'
page_response = requests.get(page_link, timeout=20)
page_content = BeautifulSoup(page_response.content, "html.parser")


#%%
image_link_list = page_content.find_all("a", attrs={"title": "Download photo", "class": "_37zTg _1l4Hh _1CBrG _1zIyn xLon9 _1Tfeo NDx0k _2Xklx"})


#%%
for index, image_link in enumerate(image_link_list):
    response = requests.get(image_link.attrs["href"], stream=True, timeout=10.0)
    if response.status_code == 200:
        with open(pathlib.Path(f"images/desktop{index}.jpg"), "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)


