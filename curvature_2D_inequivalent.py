import numpy as np



def curv_2D(data,amplitude):
    """I0 could be a variable"""
    num_line = len(data)
    num_column = len(data[1])

    etha = num_line
    etha = 0.01
    chi = num_column
    chi=5e-3
    I0 =1
    #I0 = 10**0.5
    Cx=I0**2*chi**2
    Cy=I0**2*etha**2

    [Dy, Dx] = np.gradient(data)
    [DyDx, DxDx] = np.gradient(Dx)
    [DyDy, DxDy] = np.gradient(Dy)


    C_c=np.zeros((num_line,num_column))
    for k in range(len(Dx)):
        #C_c[k] = [-1*((1+Cx*i**2)*Cy*m-(2*Cx*Cy*i*j*l)+(1+Cy*j**2)*Cx**k)/((1+Cx*i**2+Cy*j**2)**(3/2)) for i,j,k,l,m in zip(Dx[k], Dy[k], D2x[k], DxDy[k], D2y[k])]
        #C_c[k] = [-1*(((1 + Cx * i ** 2) * Cy * m) - (2 * Cx * Cy * i * j * l) + ((1 + Cy * j ** 2) * Cx * k)) / (
        #            (1 + Cx * i ** 2 + Cy * j ** 2) ** (3 / 2))  for i,j,k,l,m in zip(Dx[k], Dy[k], DxDx[k], DxDy[k], DyDy[k])]

        C_c[k] = [-amplitude * ((( i ** 2) * m) - (2 * i * j * l) + (( j ** 2) * k)) / (
                (Cx * i ** 2 + Cy * j ** 2) ** (3 / 2)) for i, j, k, l, m in
                  zip(Dx[k], Dy[k], DxDx[k], DxDy[k], DyDy[k])]

        for i in range(len(C_c[k])):
            if C_c[k][i]<0:
                C_c[k][i]=0.0

    return(C_c)