from os import listdir

files = listdir(".")
new_name = "yolov4.pytorch.txt"
new_file = open(new_name,"w")

for fname in files:
        if fname.find(".py") > 0 or fname.find("_test") > 0 or fname.find("label") > 0 or fname.find(".txt") < 0 :
                continue
        print(fname)
        file = open(fname)
        new_row = fname.split(".")[0] + "_test.jpg "
        for row in file:
                part_row = ""
                row = row.strip("\n")
                elems = row.split(" ")
                for k in elems[0:4]:
                        part_row += k + ","
                part_row += elems[-1] + " "
                new_row += part_row
        new_file.write(new_row + "\n")
        file.close()

new_file.close()
