
import numpy as np



def curv_1D_line(ydata,a0,amplitude):
    """take an array return a list, curvature 1D"""
    dfdx=np.gradient(ydata)
    d2fdxdx=np.gradient(dfdx)

    C0 = a0*np.abs(np.max(dfdx))**2


    C = np.array([-amplitude*(y/((C0+x**2)**(3/2))) for x,y in zip(dfdx, d2fdxdx)])


    for i in range(len(C)):
        if C[i]<0:
            C[i]=0

    return (C)


def curv_1D_img(data, a0,amplitude):
    """input array output array"""

    num_line = len(data)
    num_column = len(data[1])

    C = np.zeros((num_line, num_column))
    for k in range(num_line):

        dfdx = np.gradient(data[k])
        d2fdxdx = np.gradient(dfdx)

        C0 = a0 * np.abs(max(dfdx)) ** 2
        C[k] = [-amplitude * (y / ((C0 + x ** 2) ** (3 / 2))) for x, y in zip(dfdx, d2fdxdx)]

        for i in range(len(C[k])):
            if C[k][i] < 0:
                C[k][i] = 0.0



    return(C)
