#To check if an item exits in list
lst = ['apple','mango','grapes','banana','gauva']
if 'apple' in lst:
    print("Apple is present in list")
#insert at index
    lst.insert(2,'watermelon')
    print(lst)        #no of items will increase
    
#Append
lst.append("poatato")
print(lst)

#Extend list
list1 = ["apple","mango","banana"]
list2 = ["tomato","potato","carrot"]
list1.extend(list2)
print(list1)

tuple1 = ("kiwi","orange")
list2.extend(tuple1)
print(lst2)

list3 = list1 + list2   #concatenation with +
print(list3)

#to remove from list
list1.remove("tomato")
print(list1)

list1.pop(3)   #with index
#if index is not provided it will pop last item

del list1[3]
print(list1)

#to delete entire list items
list1.clear()
print(list1)

# to find length
print(len(list1))

#Sorting
list2.sort()
print(list2)

list2.sort(reverse = True)
print(list2)

#Copying lists
mylist = list(list2)
print(mylist)

mylist = list2.copy()
print(mylist)

#count elements in list with value
list2.count("kiwi")
