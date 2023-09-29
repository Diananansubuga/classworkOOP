# write a function that returns the maximum number in an array

# without a list
def largest(arr,n):
    max = arr[0]
    for i in range (1 , n ):
        if  arr [i]>max:
            max=arr[i]
        return max
    

    
# using an array for loop
num_list=(1,4,2,8,19,24)
def largest(arr,n):
    max= arr[0]
    for num in arr:
        if num>max:
            max=num
    return max

result = largest(num_list, len(num_list))
print("The maximum value in the list is:", result)
num_list = (1, 4, 2, 8, 19, 24)



# using an array while loop
def find_max(arr):
    max_value = arr[0]  
    index = 1
    while index < len(arr):
        if arr[index] > max_value:
            max_value = arr[index] 
        index += 1 
    
    return max_value

result = find_max(num_list)
print("The maximum value in the list is:", result)


