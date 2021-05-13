def test_printGraph(data):
    out=[]
    for i in data:
        t = []
        for x in range(i):
            print('x', end='')
            t.append('x') # x should be within quotes, empty quotes would print empty
        print()
        out.extend([t]) # if the output t is a range of i as x, each range should be within brackets
    return out

#unit test 1
data = [1,2,3]
output = test_printGraph(data)
print(output)
assert output == [['x'], ['x', 'x'], ['x', 'x', 'x']]

#unit test 2
data2 = [3,4,5]
output = test_printGraph(data2)
print(output)
assert output == [['x','x','x'], ['x','x','x','x'], ['x','x','x','x','x']]
