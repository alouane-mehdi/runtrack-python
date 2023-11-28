def draw_rectangle(width,height):
    for i in range(height):
        
        if i==0 or i==height-1:
            print('|'+'-'*(width-2), end='')
            print('|')
        else:
            print("|"+' '*(width-2), end="") 
            print('|')


draw_rectangle(10,3)

