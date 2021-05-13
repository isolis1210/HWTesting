def myfunc(x):
    y = 0
    if x == 10:
        return False
    elif y >= 1:
        raise True
    else:
        print('It does not work')
    if x < 0:
        y = -x
    return 0

# $ coverage run partb.py
# $ coverage report
    ''' Stmts 10
        Miss 9
        Cover 10%
    '''
# 1/10 maximum statement coverage
