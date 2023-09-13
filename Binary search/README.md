

### Header

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

- The `#!/usr/bin/env python3` line specifies that the script should be run using Python 3.
- The `# -*- coding: utf-8 -*-` line specifies that the script uses UTF-8 encoding.

### Function: `binarysearch`

```python
def binarysearch(arr, x, low, high):
```

This function takes a sorted array (`arr`), an element to search for (`x`), and the `low` and `high` indices as parameters and performs binary search.

- `mid = 0`: Initializes `mid` to 0.
- `low <= high`: Keeps the loop running as long as the `low` index is less than or equal to the `high` index.
- `mid = low + (high - low) // 2`: Calculates the middle index.
- The function returns the index of the element if it is found, otherwise, it returns -1.

### User Input

The script prompts the user to enter the number of elements in the array and the elements themselves.

```python
i = int(input("Enter the number of elements: "))
arr = []

while i != 0:
    b = int(input("Enter a number: "))
    arr.append(b)
    i = i - 1
```

- `i`: Stores the number of elements to be added to the array.
- `arr`: Stores the elements of the array.
- The loop continues until all numbers are entered.

### Sort the array

```python
arr.sort()
```

The array is sorted in ascending order.

### Search Element

```python
x = int(input("Enter the number to find: "))
```

The user is prompted to enter the number to search for.

### Perform Search

```python
a = binarysearch(arr, x, 0, len(arr) - 1)
```

The `binarysearch` function is called to search for the element `x` in the array.

### Output

```python
if a != -1:
    print("Number is at index " + str(a))
else:
    print("Number not found in array.")
```

The program outputs the index at which the number is found. If not found, it outputs that the number is not present in the array.
