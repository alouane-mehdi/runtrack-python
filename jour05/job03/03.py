def triangle(height):
    for i in range(height):
        if i==0:
            print(' '*(height-(i+1))+'/''\\')
        elif i!=0 and i!=height-1:
            print(' '*(height-(i+1))+'/'+'  '*(i),end='')
            print('\\')
        else:
            print('/'+'__'*(height-1)+"\\")


triangle(5)
   