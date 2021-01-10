infile=open("C:/Users/USER/Desktop/20190517-20174627-김혜진/11/phones.txt","r")
line=infile.readline().rstrip()
while line !="":
    print(line)
    line=infile.readline().rstrip()
infile.close()
