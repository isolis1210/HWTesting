def printGraph(data):
    out=[]
    for i in data:
        t = []
        for x in range(i):
            print('x', end='')
            t.append('x') # x should be within quotes, empty quotes would print empty
        print()
        out.extend([t]) # if the output t is a range of i as x, each range should be within brackets
    return out

data = [1,2,3]
output = printGraph(data)
print(output) 

