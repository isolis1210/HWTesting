def test_printGraph(data):
    out=[]
    for i in data:
        t = []
        for x in range(i):
            print('x', end='')
            t.append('x')
        print()
        out.extend([t])
    return out

data = [1,2,3]
output = test_printGraph(data)
print(output)
assert output == [['x'], ['x', 'x'], ['x', 'x', 'x']]

data2 = [3,4,5]
output = test_printGraph(data2)
print(output)
assert output == [['x','x','x'], ['x','x','x','x'], ['x','x','x','x','x']]
