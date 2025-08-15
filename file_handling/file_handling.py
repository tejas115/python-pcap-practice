f = open('MyData', 'r')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.read())
# f.close()

# f1 = open('abc', 'w')
# f1.write("Hello, World!\n")
# f1.write("this is a test.\n")
# f1.close()

# f1 = open('abc', 'a')
# f1.write("Appending a new line.\n")
# f1.close()  


f1 = open('abc', 'w')

for data in f:
    f1.write(data)


f.close()
f1.close()  

# copy the image file.

f2 = open('images.jpg', 'rb')
f3 = open('images_copy.jpg', 'wb')
for i in f2:
    f3.write(i)

f2.close()
f3.close()

