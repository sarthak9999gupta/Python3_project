#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Function to perform binary search on a sorted array
def binarysearch(arr, x, low, high):
    mid = 0  # Initialize mid
    while low <= high:
        mid = low + (high - low) // 2  # Calculate mid within the loop

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1  # If x is greater, ignore the left half
        else:
            high = mid - 1  # If x is smaller, ignore the right half

    return -1

# Take input from the user
i = int(input("Enter the number of elements: "))
arr = []

# Loop to get elements for the array
while i != 0:
    b = int(input("Enter a number: "))
    arr.append(b)
    i = i - 1

# Sort the array
arr.sort()

# Take the number to find
x = int(input("Enter the number to find: "))

# Perform the binary search
a = binarysearch(arr, x, 0, len(arr) - 1)

# Output the result
if a != -1:
    print("Number is at index " + str(a))
else:
    print("Number not found in array.")
