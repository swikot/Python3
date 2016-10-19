__author__ = 'snow'


# google_search=search("cats","i have cats and mouse")
# if google_search:
#     print("cats found")
# else:
#     print("cats not found")
#
#
#
# google_search=search(r"[A-Z][a-z]"," F")
# if google_search:
#     print("letter found")
# else:
#     print("letter not found")


#
# >>> import re
# >>> s1 = "Mayer is a very common Name"
# >>> s2 = "He is called Meyer but he isn't German."
# >>> print(re.search(r"M[ae][iy]er", s1))
# <_sre.SRE_Match object at 0x7fc59c5f26b0>
# >>> print(re.search(r"M[ae][iy]er", s2))
# <_sre.SRE_Match object at 0x7fc59c5f26b0>
# >>> print(re.match(r"M[ae][iy]er", s1))
# <_sre.SRE_Match object at 0x7fc59c5f26b0>
# >>> print(re.match(r"M[ae][iy]er", s2))
# None
# >>>



# r"M[ae][iy]e?r"  "e" may or may not occur
# r"Feb(ruary)? 2011"

# Quantifiers

# the question mark ?
# the asterisk or star character *, which is derived from the Kleene star
# and the plus sign +, derived from the Kleene cross
# r"[0-9]*" any digits 0 or more times

#ex: Write a regular expression which matches strings which starts with
# a sequence of digits - at least one digit - followed by a blank and after this arbitrary characters.
# r"^[0-9][0-9]* "
#r"[0-9]*" any digits at least 1 or more times


#ex: These lines usually contain a four digits long post code followed by a blank and a city name
# r"^[0-9][0-9][0-9][0-9] [A-Za-z]+"
# Fortunately, there is an alternative available:
# r"^[0-9]{4} [A-Za-z]*"
# r"^[0-9]{4} [A-Za-z]*"
# r"^[0-9]{4,5} [A-Z][a-z]{2,}"


# Now we want to improve our regular expression.
# Let's assume that there is no city name in Switzerland, ' \
#    'which consists of less than 3 letters, at least 3 letters. ' \
#    'We can denote this by [A-Za-z]{3,}. Now we have to recognize lines with German post code (5 digits) ' \
# 'lines as well, i.e. the post code can now consist of either four or five digits:


# r"^[0-9]{4,5} [A-Z][a-z]{2,}"


# A Closer Look at the Match Objects

import re
# mo = re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
# print(mo.group())
# print(mo.span())
# print(mo.start())
# print(mo.end())
# print()
# print(mo.span()[0])
# print(mo.span()[1])


mo = re.search("([0-9]+).*: (.*)", "Customer number: 232454, Date: February 12, 2011")

mo.group()
mo.group(1)
mo.group(2)
mo.group(1,2)






