list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)
print(type(list_1))

list_2 =set([2,6,0,66,22,8,4])
print(list_1,list_2)
#交集
print(list_1.intersection(list_2))
#并集
print(list_1.union(list_2))
#差集
print(list_1.difference(list_2))
print(list_2.difference(list_1))
#子集
list_3=set([1,3,7])
print(list_1.issubset(list_3))
print(list_3.issuperset(list_1))

#对称差集
print(list_1.symmetric_difference(list_2))


print(list_3.isdisjoint(list_1))
print(list_1^list_2)
list_1.update([111,"s"])
print(list_1)
print(list_1.pop())
print(list_1.remove("s"))

print(list_1.discard(111))#Remove an element from a set if it is a member. If the element is not a member, do nothing.
print(list_1.symmetric_difference_update([7,151]))
print(list_1)
print(list_2.isdisjoint(list_1))#没有相同元素返回True
s = ([1,2,3])
print(s)
print(type(s))