'''
Second implementation of codekata kata02: karate chop
link of problem statement as follows
http://codekata.com/kata/kata02-karate-chop/
by using binary search
'''
#Binary search function
def binary_search(list_items, num):
	first =0
	last= len(list_items)-1
	mid=0
	while first<=last:
		mid = (first+last)//2

		if num<list_items[mid]:
			last = mid-1
		
			#Other half of the list starting from the 'mid' gets deleted.
			#This reduces the data in the list and makes the search cycles shorter,reduces time complexity.

		elif num>list_items[mid]:  	
			first= mid+1
			
			#Other half of the list upto the 'mid' index gets deleted
			#This reduces the data in the list and makes the search cycles shorter,reduces time complexity. 

		else:	
			return mid
	     #the num will be present at the mid
	
	return -1
	  #if num is not present in list it will return -1

result =binary_search([1,2,3,4,5,6], 5)
#For this binary_search the list should be sorted in ascending order

print(result)
