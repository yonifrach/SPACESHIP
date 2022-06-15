VEL=5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
WIDTH, HEIGHT = 900, 500
BORDERX= WIDTH/2 -5
def y_movement(dire, locX , locY, borderX , borderY):
    pass

  
#TEST:
x=150
y=60
print(x,y,'L')
y_movment('L',x,y,BORDERX,HEIGHT)
x=0
y=60
print(x,y,'L')
y_movment('L',x,y,BORDERX,HEIGHT)

x=385
y=160
print(x,y,'R')
movment('R',x,y,BORDERX,HEIGHT)
x=200
y=160
print(x,y,'R')
movment('R',x,y,BORDERX,HEIGHT)

x=20
y=0
print(x,y,'U')
y_movment('U',x,y,BORDERX,HEIGHT)
x=20
y=100
print(x,y,'U')
y_movment('U',x,y,BORDERX,HEIGHT)

x=400
y=460
print(x,y,'D')
movment('R',x,y,BORDERX,HEIGHT)
x=400
y=160
print(x,y,'D')
movment('R',x,y,BORDERX,HEIGHT)
