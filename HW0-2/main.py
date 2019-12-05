#Img
import Image
im = Image.open("sumi.jpg")
print(im.format, im.size, im.mode)

pixel = im.load()
for x in range(im.size[0]):
    for y in range(im.size[1]):
        r,g,b = pixel[x,y]
        pixel[x,y] = (int(r/2),int(g/2),int(b/2))
im.save("Q2.jpg")
im.show()

"""
參考
1.https://yungyuc.github.io/oldtech/python/python_imaging.html(影像處理)
2.https://john850512.wordpress.com/2018/02/28/python%E9%80%8F%E9%81%8Epil%E6%94%B9%E8%AE%8A%E5%9C%96%E7%89%87%E7%9A%84pixel/(改變圖片pixel)
"""