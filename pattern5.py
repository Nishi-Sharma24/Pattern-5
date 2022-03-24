#pattern6
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
for x in range(1,6):
    for y in range(1,x+1):
        print('*',end=' ')
    print('\n')   
for p in range(5,0,-1):        
    for z in range(0,p-1):
        print('*',end=' ')
    print('\n')
input() 
