
import numpy as np


def curv_2D(data,a0,amplitude):
    [Dy, Dx] = np.gradient(data)
    [DyDx, D2x] = np.gradient(Dx)
    [D2y, DxDy] = np.gradient(Dy)

    C0 = a0*np.abs(np.max(Dx))**2

    C=[[] for i in range(len(Dx))]
    for k in range(len(Dx)):
        C[k] = [-amplitude*((C0+i**2)*m-(2*i*j*l)+(C0+j**2)*k)/((C0+i**2+j**2)**(3/2)) for i,j,k,l,m in zip(Dx[k], Dy[k], D2x[k], DxDy[k], D2y[k])]

        for i in range(len(C[k])):
            if C[k][i]<0:
                C[k][i]=0.0

    C= np.array(C)
    return(C)