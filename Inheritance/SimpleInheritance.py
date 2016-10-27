__author__ = 'snow'


class Parent():
    def last_name(self):
        return "Roberts"

class Child(Parent):
    def first_name(self):
        return "Bucky"
    def last_name(self):
        return "Snizelberg"


p=Child()
print(p.first_name()+" "+p.last_name())
