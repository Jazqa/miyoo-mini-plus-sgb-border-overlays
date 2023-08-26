import os

def gen_cfg(target_folder):
    for file in os.listdir(target_folder):
        if os.path.isfile(target_folder + file) and file.endswith(".png"):
            cfg_file = target_folder + os.path.splitext(file)[0] + ".cfg"
            
            print("Writing " + cfg_file + "...")
            
            f = open(cfg_file, "w+")
            f.write("overlays = 1\noverlay0_full_screen = true\noverlay0_descs = 0\noverlay0_overlay = " + file)
            f.close()