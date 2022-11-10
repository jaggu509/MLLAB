import numpy as np
import matplotlib.pyplot as plt


def estimate_coefficent(x,y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(y*x) - n*m_x*m_y
    SS_xx = np.sum(x*x) - n*m_x*m_x

    b_1 = SS_xy/SS_xx
    b_0 = m_y - b_1*m_x
    return(b_0, b_1)

def plot_regression_line(x,y,b):
    plt.scatter(x,y, color="r")
    y_pred = b[0] + b[1]*x 
    
    plt.plot(x,y_pred, color="g")  
    plt.show() 
        
def main():
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([0,1,2,3,4,5,6,7,8,9])
    
    b = estimate_coefficent(x,y)
    plot_regression_line(x,y,b)

if __name__ == "__main__":
    main()
    