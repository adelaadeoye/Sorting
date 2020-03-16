# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) ok
        for j in range(cur_index+1,len(arr)):
            if arr[j]< arr[smallest_index]:
                smallest_index=j

        # TO-DO: swap
        if cur_index != smallest_index:
            temp = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = temp
           

    return arr

# Swap Function 
def swapPositions(arr, pos1, pos2):  
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1] 
    return arr
# # TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

# Pseudocode 
# for all elements of list
#       if list[i] > list[i+1]
#          swap(list[i], list[i+1])
#       end if
#    end for
   
#    return list
    for i in range(0,len(arr)-1):
      
        if arr[i]>arr[i+1]:
           swapPositions(arr,i,i+1)
        #    Recursion 
           bubble_sort(arr)
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr