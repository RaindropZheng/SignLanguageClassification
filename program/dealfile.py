import numpy as np

def MaxMinNormalization(x, Max, Min):
    x = (x - Min) / (Max - Min)
    return '{:.6f}'.format(x)
for i in range(5):
    j_i = 156 + i
    i_str = str(i+1)
    j_str = str(j_i)
    f = open("C:\\Users\Administrator\Desktop\Gproject\datasets\D_train/"+j_str+".txt", 'w')
    f1 = open("C:\\Users\Administrator\Desktop\Gproject\datasets\RawData\Train\L_Canlan_ZSJ_" + i_str + '.txt', 'r')
    f2 = open("C:\\Users\Administrator\Desktop\Gproject\datasets\RawData\K_Canlan_ZSJ_"+i_str+'.txt','r')
    a = np.loadtxt("C:\\Users\Administrator\Desktop\Gproject\datasets\RawData\Train\L_Canlan_ZSJ_" + i_str + '.txt')
    a_Max = np.max(a)
    a_Min = np.min(a)
    b = np.loadtxt("C:\\Users\Administrator\Desktop\Gproject\datasets\RawData\K_Canlan_ZSJ_"+i_str+'.txt')
    b_Max = np.max(b)
    b_Min = np.min(b)
    line1 = f1.readline()
    j = 0
    while line1:
        for m in range(36):
            new_a = a[j][m]
            arr =str( MaxMinNormalization(new_a, a_Max, a_Min))
            f.write(arr+' ')
        f.write('\n')
        line1 = f1.readline()
        j += 1

    line2 = f2.readline()
    k = 0
    while line2:
        for n in range(12):
            new_a = a[k][n]
            arr =str( MaxMinNormalization(new_a, a_Max, a_Min))
            f.write(arr+' ')
        for q in range(24):
            f.write("0.500000 ")
        f.write('\n')
        line2 = f2.readline()
        k += 1
    f.close()
    f1.close()
    f2.close()