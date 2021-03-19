# Sort Algorithm

From the MIT course 6.006 - Algorithm and Data Structure

### Counting Sort
First implementation of counting sort. 

* Step 1: Create a counting array that store the number of times a number is present in a given array;

* Step 2: Sum the numbers in the counting array with the preceding one (**count_arr[i] + count_arr[i - 1]**);

* Step 3: Once the counting array stores the positions of the numbers belonging to the array passed in the function, an output array 
will store the number in a position specified by the counting array. Every time a number gets allocated in the output array, the count must 
  be diminished by 1.
  
#### Notes:
The use of the min to subtract to the index when allocating the objects in the counting array is to account for negative numbers. It basically 
shifts the entire array forward allowing negative numbers from the input array to have positive indexes in the counting array. In addition, 
the use of min makes sure that the smallest number will always be allocated at the 0 index of the counting array.

The function returns an output array which doesn't affect the original input array. As best practice dictates, mutations are 
not recommended. 

#### TODO
Implement Radix Sort and other sort algorithms.