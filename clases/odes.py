from vector import VectorND

def euler(f, y0, t0, t, n):


    h = (t - t0)/n
    tk = t0
    yk = y0
    ysolve = [yk]*(n+1)
    tsolve = [tk]*(n+1)
    

    for k in range(1, n+1):
        ysolve[k] = ysolve[k-1] + f(ysolve[k-1], tsolve[k-1])*h
        tsolve[k] = tsolve[k-1] + h

    return ysolve, tsolve

def heun(f, y0, t0, t, n):

    h = (t - t0)/n
    tk = t0
    yk = y0
    ysolve = [yk]*(n+1)
    tsolve = [tk]*(n+1)
    

    for k in range(1, n+1):
        k1 = f(ysolve[k-1], tsolve[k-1])*h
        k2 = f(ysolve[k-1] + k1, tsolve[k-1] + h)*h

        ysolve[k] = ysolve[k-1] + 0.5*(k1 + k2)
        tsolve[k] = tsolve[k-1] + h

    return ysolve, tsolve

def rungeKutta(f, y0, t0, t, n):

    h = (t - t0)/n
    tk = t0
    yk = VectorND(y0)
    ysolve = [yk]*(n+1)
    tsolve = [tk]*(n+1)
    

    for k in range(1, n+1):
        omega = 0.5
        k1 = h*f(ysolve[k-1], tsolve[k-1], omega)
        k2 = h*f(ysolve[k-1] +0.5*k1, tsolve[k-1] + 0.5*h, omega)
        k3 = h*f(ysolve[k-1] +0.5*k2, tsolve[k-1] + 0.5*h, omega)
        k4 = h*f(ysolve[k-1] + k3, tsolve[k-1] + h, omega)

        ysolve[k] = ysolve[k-1] + (1/6.0)*(k1 + 2*k2 + 2*k3 + k4)
        
        tsolve[k] = tsolve[k-1] + h
    return ysolve, tsolve

def F(y,t):
    return y


def F2(y,t):
    return -2*t*y**2

#### y = [x, vx] = 
def oscilador(y, t, omega):
    return VectorND([y[1], -omega*y[0]])
"""
La condición inicial y(0) = 0.5
"""
t0 = 0.0
y0 = [1.0, 0.0]
##ye, te = euler(F, y0, t0, 5.0, 100)
##yh, th = heun(F2, y0, t0, 5.0, 20)
yr, tr = rungeKutta(oscilador, y0, t0, 5.0, 20)
print(yr)
print(yr)
#f = f"euler_{t0}_{y0}".replace(".","-") +".dat"
f = f"runge_oscilador_{t0}_{y0}".replace(".","-") +".dat"

#for i in range(len(te)):
#    with open(f, "a") as file:
#        file.write(str(te[i])+" "+str(ye[i])+"\n" )

for i in range(len(tr)):
    with open(f, "a") as file:
        file.write(str(tr[i])+" "+str(yr[i])+"\n" )
###print(f"Tiempos {t} \n y los puntos {y}")
