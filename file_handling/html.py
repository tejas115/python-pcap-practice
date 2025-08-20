f = open("./oulipo.txt", "r")
# Read the lines of the file
lines = f.readlines()
# Iterate through the lines
for line in lines:
    # fetch the first char of each line
    first_char = line[0]
    # print the line with its first char wrapped
    print("<b>" + first_char + "</b>" + line.strip(first_char))
    