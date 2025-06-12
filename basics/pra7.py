#loop
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  #list comprehension
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Perform a case-insensitive sort of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse the order of the list items
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy of list
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


print("TUPLE EXERCISES")
#Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple)

#this will raise an error because the tuple no longer exists

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)