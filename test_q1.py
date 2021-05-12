#from numpy import array
#import pytest
#import array as arr

# Unsure of what to assert in this test

def test_someSort(arr):
    n = len(arr)+1

    for i in range(n):
        swapped = True

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

            if swapped == False:
                break

