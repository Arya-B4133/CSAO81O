
for i in range(12,20):
    count=0
    for j in range(1,10):
        if(i%j==0):
            continue:
        else:
            count+=1
    if count>=1:
        print(i)
            
