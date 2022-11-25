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
	indx = None
	mid=0
	while first<=last:
		mid = (first+last)//2
		
		''' if num is less than mid ignore 
		right side of the mid'''
		if num<list_items[mid] :
			last = mid-1 
			''' if num is greater than mid ignore 
			right side of the mid
			'''

		elif num>list_items[mid]:   
			first= mid+1   

			'''the num will be present at the mid
			'''
		else:
			return mid
        #if num is not present it will return -1
	return -1


result =binary_search([1,2,3,4,5,6], 6)

print(result)