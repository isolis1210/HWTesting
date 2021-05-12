#from numpy import array
#import array as arr

def someSort(arr):
    n = len(arr) # Remove the +1 here because it would cause the range to be too large 
    
    for i in range(n):
        swapped = True

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if swapped == False:
                break

covid_nums = [ 88, 85, 123, 96, 104, 81]
someSort(covid_nums)
print(covid_nums)

