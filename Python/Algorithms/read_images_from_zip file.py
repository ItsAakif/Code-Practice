import zipfile
from PIL import Image
imgzip = zipfile.ZipFile("100-Test.zip")
inflist = imgzip.infolist()
for f in inflist:
ifile = imgzip.open(f)
img = Image.open(ifile)
print(img)
