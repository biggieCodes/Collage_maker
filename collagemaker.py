from PIL import Image
import numpy as np
def collage_maker(image1, image2, name):
    i1 = np.array(image1)
    i2 = np.array(image2)
    collage = np.vstack([i1, i2])
    image = Image.fromarray(collage)
    image.save(name)

# To Run The Above Function
collage_maker("_MG_0147.jpg", "_MG_0136.jpg", "_MG_0151.jpg")