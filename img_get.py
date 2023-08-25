import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from PIL import Image

def get_img_urls(url):
    img_urls = []
    imgs = bs(requests.get(url).content, "html.parser").find_all("img")
    
    for img in imgs:
        img_src = img.attrs.get("src")
        if img_src.startswith("sgb/"):
            img_url = urljoin(url, img_src)
            img_urls.append(img_url)
            
    return img_urls

def get_img(url, folder):
    name = url.split("/")[-1]
    path = folder + name
    
    if os.path.isfile(path):
        return
        
    data = requests.get(url).content
    
    print("Writing " + path + "...")
    
    f = open(folder + name, "wb")
    f.write(data)
    f.close()
    
    

def get_imgs(url, folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
    
    img_urls = get_img_urls(url)
    
    for img_url in img_urls:
        get_img(img_url, folder)