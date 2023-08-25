import os
from PIL import Image
from PIL import ImageDraw

def manip_imgs(src_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for file in os.listdir(src_folder):
        src_file = src_folder + file
        
        if os.path.isfile(src_file) and file.endswith(".png"):
            img = Image.open(src_file)
            
            width = 768
            height = 672
            
            crop_h = 64
            crop_v = 96
            
            new_img = img.resize((width, height), Image.NEAREST)
            
            width = 640
            height = 480
            
            start_x = crop_h
            start_y = crop_v
            end_x = crop_h + width
            end_y = crop_v + height
            
            new_img = new_img.crop((start_x, start_y, end_x, end_y))
            
            screen = (80, 24, 80 + 480 - 1, 24 + 432 - 1)
            mask = Image.new("L", new_img.size, color=255)
            draw = ImageDraw.Draw(mask)
            draw.rectangle(screen, fill=0)
            new_img.putalpha(mask)

            file = target_folder + file
            
            print("Saving " + file + "...")
            
            new_img.save(file)