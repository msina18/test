def v (str):
    n = {'a', 'e','i','o','u'}
    c = 0
    r = []
    for i in str :
        if i.lower() in n:
            r.append(i)
            c+= 1 
    return c, r
        
print(v(input('enter a name :'))) 
print('************') 
print('=============')
















