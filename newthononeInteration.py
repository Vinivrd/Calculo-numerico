import numpy as np



def formula(x,y):
    f= (x-1)**2 + y**2 -4
    g = x**2 +(y-1)**2 -4
    return [f,g]
def form(x, y):

    f= formula(x,y)[0]
    g = formula(x,y)[1]

    print("FXY = ",f)
    print("GXY = ",g)

    fx =  2*x -2
    fy=  2*y

    gx= 2*x
    gy = 2*y - 2
    print("\nFX = ",fx)
    print("FY = ",fy)
    print("GX = ",gx)
    print("FY = ",gy)

    fgy =  (f*gy)
    fyg = fy*g

    fxg = fx * g 
    fgx = f * gx

    jfg = fx*gy - fy*gx

   

    res1 = x - (( fgy -  fyg) / jfg)
    res2 =  y - ((fxg - fgx)/jfg)
    print(res1)
    print(res2)
    print('formula  final = ',formula(res1,res2))

    

form(1.83,1.83)
