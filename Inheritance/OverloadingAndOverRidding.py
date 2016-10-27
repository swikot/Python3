__author__ = 'snow'




class Person:

    def __init__(self, first, last,age):
        self.firstname = first
        self.lastname = last
        self.age=age

    def __str__(self):
        return self.firstname + " " + self.lastname+" "+str(self.age)


class Employee(Person):

    def __init__(self, first, last,age, staffnum):
        super().__init__(first, last,age)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__()+", "+self.staffnumber


x = Person("Marge", "Simpson",10)
y = Employee("Homer", "Simpson",11, "1007")

print(x)
print(y)







