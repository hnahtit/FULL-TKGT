import sys
#declare variables
arr = []

#read data from file
f = open('data.txt','r')
for val in f.read().split():
    arr.append(int(val))
f.close()

#test
"""
def maxSubArraySum(a,size): 
       
    max_so_far = -999999 - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 
"""
a = [1,-3,2,1,-1]
#Main function

def maxCrossingSum(arr, l, m, h) : 
      
    # Include elements on left of mid. 
    sumMax = 0
    left_sum = -sys.maxsize-1
      
    for i in range(m, l-1, -1) : 
        sumMax = sumMax + arr[i] 
          
        if (sumMax > left_sum) : 
            left_sum = sumMax 
      
      
    # Include elements on right of mid 
    sumMax = 0
    right_sum = -sys.maxsize-1
    for i in range(m + 1, h + 1) : 
        sumMax = sumMax + arr[i] 
        if(sumMax > right_sum):
            right_sum = sumMax
      
  
    # Return sum of elements on left and right of mid 
    return left_sum + right_sum
  
  
# Returns sum of maxium sum subarray in aa[l..h] 
def maxSubArraySum(arr, l, h) : 
      
    # Base Case: Only one element 
    if (l == h) : 
        return arr[l] 
  
    # Find middle point 
    m = (l + h) // 2
  
    # Return maximum of following three possible cases 
    # a) Maximum subarray sum in left half 
    # b) Maximum subarray sum in right half 
    # c) Maximum subarray sum such that the  
    #     subarray crosses the midpoint  
    return max(maxSubArraySum(arr, l, m), 
               maxSubArraySum(arr, m+1, h), 
               maxCrossingSum(arr, l, m, h))

print("Original array:")
print(a)
subSum= maxSubArraySum(a,0,len(a)-1)
print("Max sub vector:")
print(subSum)