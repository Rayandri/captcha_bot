from captcha_rayan.image import ImageCaptcha
import random
import os
import shutil
from skimage import io


image = ImageCaptcha()


def generate_folder():
    try:
        shutil.rmtree("dataimage/txt")
        shutil.rmtree("dataimage/png")
        shutil.rmtree("dataimage")
    except: print("ERROR: Impossible d'effacer les dossier \nExecuter le fichier en administateur")
    try:
        os.mkdir("dataimage")
    except: pass
    try:
        os.mkdir("dataimage/png")
        os.mkdir("dataimage/txt")
    except: pass


def generate(nb):
    generate_folder()
    for i in range(nb):
        mot = ""
        for j in range(6):
            mot += random.choice("azertyupqdfghkmwxvbnAZERTYPQDFGHJKMWXBN47852369")

        image.write(mot, f"dataimage/png/{i}.png")
        with open(f"dataimage/txt/{i}.txt", "w") as f:
            f.write(mot)
        if i%100 == 0 : print(i)



def random_image(nb_image):
    nb = random.randint(0,nb_image-1)
    img = f"dataimage/png/{nb}.png"
    with open(f"dataimage/txt/{nb}.txt", "r") as f:
        txt = f.read()
    return img,txt