### CSC6013 Class 07 - Programming Project 07
### Copyright Alexander Medeiros 12-09-2023

"""
This program is designed to select the k-th smallest item in a list using recursion.

The methods defined in this program are :

	random_list(length) - Used to generate an array of random numbers, arguments are an integer that specifies the array length

	pivot(array, left, right) - Used to define the pivot value, similar to the recursive_sort method. Arguments are an array, index positions for the start (left) and end (right) of the array

	recursive_sort(array, left, right) - Recursively sort an array of elements into ascending order using the pivot method, arguments are an array or integers, start (left) and end (right) bounds

	QuickSelect(array, k) - Method used to find the k-th smallest element of an array. Arguments are an array and k value for smallest element to be selected.

Method descriptions:

	random_list(length)
		- The random  module is imported. An array variable 'A' is initialized and the length is passed to the random.sample() method. 
		Random numbers between 0-10000 are generated and populate the array based on the specified length. The array is returned. 

	pivot(array, left, right)
		- An array of values is passed to the method, and a variable called 'pivot' is initialized using the right-most value in the array 
		a pointer variable 'i' is initialized as the left most element - 1
		a for loop runs through each element in the array, for each j element in the array, compare it to the pivot value
		when the jth element of the array is less than or equal to the pivot, increment the point index and swap the jth and ith values,
		this loop continues until all elements smaller than the pivot are to the left, then it swaps the pivot element with the pointer value+1, and returns the pointer value+1

	recursive_sort(array, left, right)
		- An array of values is passed to the method, along with the array star and end bounds. If condition compares the left and right bounds are provided in the correct format where 
		left < right (start < end). An index value for the pivot is obtained using the 'pivot' method to be provided to the recursion which defines the value to sort elements to the left 
		and right of using an ascending order. The recursion iteration continues until the list is completely sorted.


	QuickSelect(array, k)
		- An array of values and a value for k is provided to the method as arguments.
		A while loop runs such that k is contained within the extent of the array. 'recursive_sort' method is called to sort the list in ascending order, then the value located at 
		index k-1 of the array is returned. If a k value is provided that is outside of the bounds of the array, a prompt is displayed for the user.

"""
import random

# Method to define an array of values with a specified number of elements
def random_list(length):
    A = random.sample(range(0,10000),length)
    return A

# Method to define a pivot value, where elements are sorted to the left and right of the pivot based on a comparison of size
def pivot(array, left, right): # Input array, left and right positions

	pivot = array[right] # Select the list end element as the pivot

	i = left - 1 # Define a starting pointer 
	
	for j in range(left, right): # For each item in the array
		if array[j] <= pivot: # Compare element j with the pivot value, if less than or equal to, execute swap

			i += 1 # Increment the pointer

			(array[i], array[j]) = (array[j], array[i]) # Swap i and j elements

	(array[i+1], array[right]) = (array[right], array[i+1]) # Finally swap the pivot element with the pointer
	
	return i+1 # Return the position of the pointer

# Method to recursively sort the array in ascending order
def recursive_sort(array, left, right):
    if left < right:
 
        # Index of array where values smaller than index are on the left values greater than the index are on the right
        index = pivot(array, left, right)
 
        # Recursion sort for left side of the pivot
        recursive_sort(array, left, index - 1)
 
        # Recursion sort for right side of the pivot
        recursive_sort(array, index + 1, right)

# Method to select the kth smallest element of the array
def QuickSelect(array, k):
    
	# Check the k index is contained within the array
	while (0 < k <= len(array)):

		# Call the array sorting algorithm
		recursive_sort(array, 0, len(array) - 1)
		
		# Return the value in the array associated with the kth smallest value
		return array[k - 1]
	
	# Handle case where k is not contained within the array
	if k <= 0 or k > len(array):
		print("k does not exist in array")


# Main method to ask for k value input, generate array, and select the kth smallest value
if __name__=="__main__":
	k = int(input(f'input a value for k: ')) # User input for 'k' value
	A = random_list(1000) # Generate the random number array
	value = QuickSelect(A, k) # Select the value 'k' from array 'A'
	
	print(value) # Display selected value for the user