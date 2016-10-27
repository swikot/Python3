__author__ = 'snow'

class Father():
    def father_says(self):
        print("good boy")

class Mother():
    def mother_says(self):
        print("bad boy")


class Boy(Father,Mother):

    pass

c=Boy()
c.father_says()
c.mother_says()
