#lists
list=["apple","orange","grapes"]
print(list)
print(len(list))

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the list content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)