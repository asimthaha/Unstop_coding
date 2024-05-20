def input_format(n, arr):
    t = n.split()
    arr_length = int(t[0])
    target_val = int(t[1])
    arr = list(map(int, arr.split()))
    return arr_length, target_val, arr

# Function to find pairs of flowers
def types_of_flowers(arr_length, target_val, arr):
    for i in range(arr_length):
        for j in range(i + 1, arr_length):
            if arr[i] + arr[j] == target_val:
                print(i, j)

# Read input
n = input()
arr = input()

# Format input
first, second_val, arr = input_format(n, arr)

# Find and print pairs
types_of_flowers(first, second_val, arr)
