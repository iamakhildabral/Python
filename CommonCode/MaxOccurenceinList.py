
with open("Input.txt") as file:
    linebuffer = file.read()
    lines = linebuffer.split(" ")


max_occurence = max(lines, key=lines.count)
print("The no occured max is :", max_occurence)
print("The no of time this word occured :", lines.count(max_occurence))
