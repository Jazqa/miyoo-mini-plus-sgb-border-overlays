from img_get import get_imgs
from img_manip import manip_imgs
from cfg_gen import gen_cfg

img_gallery_url = ""
img_gallery_folder = "./gallery/"
retroarch_folder = "./RetroArch/.retroarch/overlay/GB-GBC/Super Game Boy Borders/"

def main():
    get_imgs(img_gallery_url, img_gallery_folder)
    manip_imgs(img_gallery_folder, retroarch_folder)
    gen_cfg(retroarch_folder)
   
main()