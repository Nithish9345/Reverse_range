""" Given an array A of N integers and
    also given two integers B and C.
    Reverse the elements of the array A within
    the given inclusive range [B, C]. """

"""Approach - swap elements
              split the range/2 
              swap first half and second half
              if the array length is odd
              it will left the middle element"""

def reverse_range(array, start, end):
    while(start < end):
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1



array = list(map(int, input().split()))
start = int(input())
end = int(input())
reverse_range(array, start, end)

print(array)