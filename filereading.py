__author__ = 'snow'
fobj=open("test.txt","r")
for line in fobj:
    print(line.rstrip())
fobj.close()