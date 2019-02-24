#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 09:19:11 2019

@author: pan
"""

import numpy as np
import pandas as pd
from pylab import *  
    
if __name__ == "__main__":
###生成数据集   
#    x = np.arange(0,1000)
    x_all=np.random.normal(10,2,1000)
    y_all = map(lambda x_all : x_all*3+1, x_all)
    y_all = np.array(list(y_all))
    #增加噪声
    x_all=x_all+np.random.normal(0.1,0.01,1000)
    y_all=y_all+np.random.normal(0.1,0.01,1000)
    
    x=x_all[:800]
    y=y_all[:800]
    
    x_test=x_all[800:]
    y_test=y_all[800:]
###############################################################################    
    w = 0
    b = 0

    
    CT = 1
    count = 6000
    CT_w = 0
    CT_b = 0
    
    xtage = list(range(count)) 
    ytage = list(range(count)) 
    
    for j in range(count):
        sw = 0
        sb = 0
        for i in range(len(x)):
            sb = sb - 2*(y[i] - (w*x[i] + b))* 1
            sw = sw - 2*(y[i] - (w*x[i] + b))* x[i]
            pass
        
###############################################################################        
        #update parameters
        CT_w = CT_w + sw**2
        CT_b = CT_b + sb**2
        
        w = w - CT/(np.sqrt(CT_w)) * sw
        b = b - CT/(np.sqrt(CT_b))* sb

        
        xtage[j] = w
        ytage[j] = b
    pass
###############################################################################
   #plot the result    
    plt.figure(figsize=(8, 8))

    plt.subplot(2, 2, 1)
    loc = int(count*0.1)
    xx = xtage[:loc]
    yy = ytage[:loc]
    
    plt.title('cout:'+str(loc))
    plot(xx, yy, '.')
    plot(3, 1, 'v')
    
    plt.subplot(2, 2, 2)
    loc = int(count*0.2)
    xx = xtage[:loc]
    yy = ytage[:loc]
    
    plt.title('cout:'+str(loc))
    plot(xx, yy, '.')
    plot(3, 1, 'v')
    
    plt.subplot(2, 2, 3)
    loc = int(count*0.4)
    xx = xtage[:loc]
    yy = ytage[:loc]
    
    plt.title('cout:'+str(loc))
    plot(xx, yy, '.')
    plot(3, 1, 'v')
    
    plt.subplot(2, 2, 4)
    plt.title('cout:'+str(count))
    plot(xtage, ytage, '.')
    plot(3, 1, 'v')
    
#测试集
    plt.figure()
    #根据训练出来的值，进行计算
    y_hat=np.array(list(map(lambda x : xx[-1]*x+yy[-1],x_test)))

    mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error
    print ("Mean Squared Error is:",mse)
    print ("Root Mean Squared Error is:",rmse)
    print ("y=ax+b: a=",xx[-1],",b=",yy[-1])

    t = np.arange(len(x_test))
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()
    
    
    






























        
    