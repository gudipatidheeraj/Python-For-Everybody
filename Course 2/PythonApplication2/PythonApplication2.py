# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
o = fh.read()
print(o.upper().rstrip())
