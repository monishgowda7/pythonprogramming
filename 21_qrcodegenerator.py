import qrcode
# qrcode python
# https://pypi.org/project/qrcode/

url=input("enter a url:")
filename=input("enter a file name:")

if not(filename.endswith(".png")):
    filename=filename+".png"
    
    
img=qrcode.make(url)
img.save(filename)    


