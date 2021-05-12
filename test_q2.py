# Unsure of what to assert for this test

def test_printGraph():
    out=[]
    for i in data:
        t = []
        for x in range(i):
            print('x', end='')
            t.append('x')
        print()
        out.extend([t])
    return out

#data = [1,2,3]
assert out == [['x'], ['x', 'x'], ['x', 'x', 'x']]

