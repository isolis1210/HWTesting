def test_someSort(arr):
    n = len(arr) # Remove the +1 here because it would cause the range to be too large

    for i in range(n):
        swapped = True

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

            if swapped == False:
                break
                
#unit test 1                
covid_nums = [88, 85, 123, 96, 104, 81]
out = test_someSort(covid_nums)
print(covid_nums)
try:
    assert out == [81, 85, 88, 96, 104, 123]
except AssertionError as msg:
    print(msg)

#unit test 2
random_nums = [ 17, 98, 54, 32, 14, 64, 109]
out = test_someSort(random_nums)
print(random_nums)
try:
    assert out == [14, 17, 32, 54, 64, 98, 109]
except AssertionError as msg:
    print(msg)
