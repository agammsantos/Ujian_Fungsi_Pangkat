def pangkat(x,y):
    j=0
    penambah=x
    while j<y-1:
        hasil=0
        for i in range(0,x):
            hasil+=penambah
        penambah=hasil
        j+=1
    return penambah
        
print(pangkat(2, 2))
print(pangkat(3, 3))
print(pangkat(10, 5))