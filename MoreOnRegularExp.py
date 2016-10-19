__author__ = 'snow'
# re.findall(pattern, string[, flags])
t="A fat cat doesn't eat oat but a rat eats bats."
# Splitting a String With or Without with Regular Expressions
# There is a string method split, which can be used to split a string into a list of substrings.
line = "James;Miller;teacher;Perl"
print(line.split(";"))
line2 = "James Miller teacher Perl"
l=line2.split(" ")
st=" "
string=str(l[0])+st+str(l[1])+st+str(l[2])+st+str(l[3])
print(string)
print()

