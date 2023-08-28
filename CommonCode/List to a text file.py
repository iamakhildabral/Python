# Write an entire list data into a Text File

file_object = open("TEXT_TO_FILE.TXT","w")

list = {"This is Line 1\n",
        "This gonna be Line 2\n",
        "This ends with Line3\n"}

file_object.write(list)
file_object.close()

