__author__ = 'snow'

s="xxxxabcabcabccd"
sub="abc"
count=0
for i in range(len(s)):

    if s[i:i+len(sub)]==sub:
        count+=1
    else:
        continue

print(count)

