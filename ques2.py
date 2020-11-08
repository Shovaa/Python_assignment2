##removing duplicate element from list 
list1 =[1,1,3,5,7,9,9]

removedset = set(list1)
removedlist =list(removedset)
print("The duplicate free list :",removedlist)



list2=[2, 1, 6 ,9, 2, 1, 3, 5]

removedset1=set(list2)
removedlist1=list(removedset1)
print("The duplicate free list:", removedlist1)


#finding common elements from list
common_items=removedset.intersection(removedset1)
common_item=list(common_items)
print("The common elements from given two set:", common_item)
