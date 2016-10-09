from morsecode import morse



# But what's the difference between lists and dictionaries?' \
# ' A list is an ordered sequence of objects, ' \
# 'whereas dictionaries are unordered sets. ' \
# 'But the main difference is that items in dictionaries are accessed via keys ' \
# 'and not via their position.

#  Dictionaries are implemented as hash tables

# This why they are known as Hashes in Pearl



# This is how a simple Dictionary looks like
cities={"New York City":8175133,
        "Los Angeles": 3792621,
        "Washington":632323,
        "Chicago": 2695598,
        "Toronto":2615060,
        "Montreal":11854442,
        "Ottawa":883391,
        "Boston":62600}

# this is the way to retrive the data from a Dictionary
print(cities["New York City"]," ",cities["Chicago"]," ",cities["Boston"])
# print(cities["sunderland"])  KeyError will happen here
# We can access into  dictionary via a Key not via  an index()
# This why it is un ordered



#print a total dictionary
print(cities)



# It is very easy to add another entry to an existing dictionary:

cities["Halifax"]=30000
print(cities)

# This is how it is possible to create a Dictionary from  an empty dictionary


city={}
city["Halifax"]=30000
city["Darban"]=40000
print(city)


# The values can be the same in dictionary

food={"ham":"yes","pizza":"yes","egg":"no"}
print()
print(food)
food["egg"]="yes"
print(food)
print()
print()
# examples
#  next example is a simple English-German dictionary
en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
print("ENG-GERMAN=",en_de)
print(en_de["red"])

# let's say German-French

de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}

print("GERMAN-FRENCH=",de_fr)

# Lets conert English to french
# By using value of a Dictionary as the key of another Dictionary

en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}

print("English To French:")
print("The French of Red is : ",de_fr[en_de["red"]])
print("The French of Yellow is : ",de_fr[en_de["yellow"]])
print("The French of green is : ",de_fr[en_de["green"]])
print("The French of blue is : ",de_fr[en_de["blue"]])



# We can use arbitrary types as values in a dictionary
# but there is a restriction for the keys. Only immutable data types can be used as keys
#no lists or dictionaries can be used:

dic1={1:"swikot",2:"akash",3:"sajon"}
print(dic1[3])

# you can use imutable objects like "Tuples"
# otherwise arbitrary key can be used

dic2={(1,2,3):"swikot",1:"akash","two":"sajan"}
print(dic2[(1,2,3)]," ",dic2[1]," ",dic2["two"])



# lets improve the previous case senerio
# We create a dictionary of dictionaries:

en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}

dictionaries={"en_de":en_de,"de_fr":de_fr}
print(dictionaries["de_fr"]["blau"])
print()


print(dictionaries["en_de"]["blue"])

# english to french

# Operation of dictionaries
# len(d)
# returns the number of stored entries, i.e. the number of (key,value) pairs.
# del d[k]
# deletes the key k together with his value
# k in d ******
# True, if a key k exists in the dictionary d
# k not in d ******
# True, if a key k doesn't exist in the dictionary d


# next into Morse Code files

x=len(morse)
print(x)

print("a" in morse)
print("A" in morse)
print("a" not in morse)


# pop and pop item
# pop()

# If D is a dictionary, then D.pop(k)

a={"aus":3000,"ned":5000,"swe":7000,"ksa":10000}

a.pop("ksa")
print(a)

# popitem() is a method of dict, which doesn't take any parameter and removes and returns an arbitrary (key,value) pair as a 2-tuple

capitals = {"Springfield":"Illinois",
            "Augusta":"Maine",
            "Boston": "Massachusetts",
            "Lansing":"Michigan",
            "Albany":"New York",
            "Olympia":"Washington",
            "Toronto":"Ontario"}

print(capitals)
(city,state)=capitals.popitem()
print("poitem deleted city and states are= ",(city,state))
print()
print(capitals)


# Accessing non Existing Keys

locations = {"Toronto" : "Ontario", "Vancouver":"British Columbia"}

if "Toronto" in locations:print(locations["Toronto"])

if "ottowa" in locations:print(locations["ottowa"])


# alternative

print("Using get = ",locations.get("Toronto"))
print("Using get an unknow key the value is =",locations.get("dhaka"))
print("Using get an unknow key the value is =",locations.get("dhaka","narayongong"))
print("revised dict=",locations)   #it will not add (key,value)




#copy
#Important Methods

print()
words={'house': 'Haus', 'cat': 'Katze'}
w=words.copy() #only applicable for shallow Dictionary

w['cat']='mouse'
print("words=",words)
print()
print("w=",w)


# case- nested dictionary
trainings = { "course1":{"title":"Python Training Course for Beginners",
                         "location":"Frankfurt",
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }

print(trainings["course2"]["title"])


tainings2=trainings.copy()
tainings2["course2"]["title"]="Perl Training course for beginners"


print(trainings["course2"]["title"] is tainings2["course2"]["title"])

w.clear()
tainings2.clear()
trainings.clear()
print(w," ",trainings," ",tainings2)




# Update: Merging Dictionaries

# list=[1,2,3,4,5]
# for i in range(0,len(list)-1):
#     print(list[i])
knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
knowledge.update(knowledge2)
print(knowledge)


# iterate to a dictionary
d = {"a":123, "b":34, "c":304, "d":99}
# No method is needed to iterate over the keys of a dictionary:


for key in d:
    print(key," : ",d[key])

# keys()
for key in d.keys():
    print(key,":",d[key])

#values() very efficient thn finding d[keys] way
for values in d.values():
    print(values)





#Connection between Lists and Dictionaries



# If we have a dictionary

D = {"list":"Liste", "dictionary":"Wörterbuch", "function":"Funktion"}

# we could turn this into a list with two-tuples:

L = [("list","Liste"), ("dictionary","Wörterbuch"), ("function","Funktion")]



print()
print()
print()

### lists from dictionary
# items() keys() values()
wait = {"house":"Haus", "cat":"", "red":"rot"}

items_view=wait.items()
print(wait)
print("items view: ",items_view)
items=list(items_view)
print("List items: ",items)


keys_view=wait.keys()
print("keys view: ",keys_view)
keys=list(keys_view)
print("keys: ",keys)



values_view=wait.values()
print("Values view : ",values_view)
values_final=list(values_view)
print("values final",values_final)




# Turn Lists into Dictionaries


# must needs two consecutive lists
# list zip dict
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

print()

country_speciality=list(zip(countries,dishes))
print(country_speciality)

country_dish_dict=dict(country_speciality)
print(country_dish_dict)


# It's easy to answer: The superfluous elements, which cannot be paired, will be ignored:
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"," Switzerland"]
country_specialities = list(zip(countries, dishes))
country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)
# {'Germany': 'sauerkraut', 'Italy': 'pizza', 'USA': 'hamburger', 'Spain': 'paella'}




# every thing in one step
country_specialities_dict = dict(list(zip(["pizza", "sauerkraut", "paella", "hamburger"], ["Italy", "Germany", "Spain", "USA"," Switzerland"])))
print(country_specialities_dict)





# Danger Lurking
# zip() used to return a list, now it's returning an iterator in python 3
# You have to keep in mind that iterators exhaust themselves, if they are used.
l1 = ["a","b","c"]
l2 = [1,2,3]

c=zip(l1,l2)

for i in c:
    print(i)


l3 = ["a","b","c"]
l4 = [1,2,3]



d=zip(l3,l4)

z1=list(d)
z2=list(d)

print(z1)

print(z2)



# solving this problem by removing intermadiate list in list to dic conversation

l5 = ["a","b","c"]
l6 = [1,2,3]

z=zip(l5,l6)
dictonaries_last=dict(z)

print(dictonaries_last)
# del

print()
del dictonaries_last["c"]
print(dictonaries_last)












































