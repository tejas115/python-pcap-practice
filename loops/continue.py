""" loop problems showcasing continue""" 
## print values except the one's divisible by 3 or by 5 ###
for i in range(1, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i, end=", ")
print()
# End-of-file (EOF)
