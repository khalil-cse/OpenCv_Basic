
from PIL import Image,ImageFilter

image =Image.open(r"image\road.jpg")

image = image.convert("L")

# Calculating Edges using the passed laplacian Kernel
image = image.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
                                               -1, -1, -1, -1), 1,0))

# Saving the Image Under the name Edge_Sample.png
image.save(r"nEdge_Sample.jpg")
image.show()

