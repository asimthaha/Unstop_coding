def input_array_format(num):
    arr = list(map(int, num.strip().split()))
    return arr

def sort_descending(N, arr):
    reversed_arr=arr[::-1]
    for i in reversed_arr:
      print(i, end=' ')

N = int(input())
num = input()
arr = input_array_format(num)
sort_descending(N, arr)
