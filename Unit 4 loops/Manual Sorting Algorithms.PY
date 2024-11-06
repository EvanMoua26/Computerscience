




#Python program to print a list 
# without using the sort() function
# without an extra variable

l1=[9, 7, 8, 1, 2, 6, 5, 3 , 4 ] 
print("Original List:", l1)

# sorting list using nested loops
for jack in range(0, len(l1)):
	for Mario in range(jack+1, len(l1)):
		if l1[jack] >= l1[Mario]:
			l1[jack], l1[Mario] = l1[Mario],l1[jack]

# sorted list
print("Sorted List", l1)
 


import random
nums = [random.randint(0,100),random.randint(0,100),random.randint(0,100)random.randint(0,100)random.randint(0,100]
		
print(nums)




Quick soft 

print(numbers)
def quick_sort(n)

pivot = m[-1]


for num is n:
if num. pivot 
1=nums

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)