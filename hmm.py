import numpy as np
from hmmlearn import hmm
word = ["按照","傲慢","保卫","并列","必须","波浪","捕","灿烂"]
model = []
ANZHAO = []
AOMAN = []
BAOWEI = []
BINGLIE = []
BIXU = []
BOLANG = []
BU = []
CANLAN = []
# Anzhao
for a in range(1, 21):
    a_str = str(a)
    ANZHAO.append(np.loadtxt('./D_train/'+a_str+'.txt'))

# Aoman
for b in range(21, 41):
    b_str = str(b)
    AOMAN.append(np.loadtxt('./D_train/'+b_str+'.txt'))

# Baowei
for c in range(41,61):
    c_str = str(c)
    BAOWEI.append(np.loadtxt('./D_train/'+c_str+'.txt'))

# Binglie
for d in range(61,81):
    d_str = str(d)
    BINGLIE.append(np.loadtxt('./D_train/'+d_str+'.txt'))

# Bixu
for e in range(81,101):
    e_str = str(e)
    BIXU.append(np.loadtxt('./D_train/'+e_str+'.txt'))

# Bolang
for f in range(101,121):
    f_str = str(f)
    BOLANG.append(np.loadtxt('./D_train/'+f_str+'.txt'))

# Bu
for g in range(121,141):
    g_str = str(g)
    BU.append(np.loadtxt('./D_train/'+g_str+'.txt'))

# Canlan
for h in range(141,161):
    h_str = str(h)
    CANLAN.append(np.loadtxt('./D_train/'+h_str+'.txt'))

# matrix of feature ["Aoman","Anzhao","Bolang","Binglie","Baowei","Bu","Bixu","Canlan"]

M_AOMAN = np.concatenate([AOMAN[0],AOMAN[1],AOMAN[2],AOMAN[3],AOMAN[4],AOMAN[5],AOMAN[6],AOMAN[7],AOMAN[8],AOMAN[9],AOMAN[10],AOMAN[11],AOMAN[12],AOMAN[13],AOMAN[14],AOMAN[15],AOMAN[16],AOMAN[17],AOMAN[18],AOMAN[19]])
L_AOMAN = [len(AOMAN[0]),len(AOMAN[1]),len(AOMAN[2]),len(AOMAN[3]),len(AOMAN[4]),len(AOMAN[5]),len(AOMAN[6]),len(AOMAN[7]),len(AOMAN[8]),len(AOMAN[9]),len(AOMAN[10]),len(AOMAN[11]),len(AOMAN[12]),len(AOMAN[13]),len(AOMAN[14]),len(AOMAN[15]),len(AOMAN[16]),len(AOMAN[17]),len(AOMAN[18]),len(AOMAN[19])]

M_ANZHAO = np.concatenate([ANZHAO[0],ANZHAO[1],ANZHAO[2],ANZHAO[3],ANZHAO[4],ANZHAO[5],ANZHAO[6],ANZHAO[7],ANZHAO[8],ANZHAO[9],ANZHAO[10],ANZHAO[11],ANZHAO[12],ANZHAO[13],ANZHAO[14],ANZHAO[15],ANZHAO[16],ANZHAO[17],ANZHAO[18],ANZHAO[19]])
L_ANZHAO = [len(ANZHAO[0]),len(ANZHAO[1]),len(ANZHAO[2]),len(ANZHAO[3]),len(ANZHAO[4]),len(ANZHAO[5]),len(ANZHAO[6]),len(ANZHAO[7]),len(ANZHAO[8]),len(ANZHAO[9]),len(ANZHAO[10]),len(ANZHAO[11]),len(ANZHAO[12]),len(ANZHAO[13]),len(ANZHAO[14]),len(ANZHAO[15]),len(ANZHAO[16]),len(ANZHAO[17]),len(ANZHAO[18]),len(ANZHAO[19])]

M_BOLANG = np.concatenate([BOLANG[0],BOLANG[1],BOLANG[2],BOLANG[3],BOLANG[4],BOLANG[5],BOLANG[6],BOLANG[7],BOLANG[8],BOLANG[9],BOLANG[10],BOLANG[11],BOLANG[12],BOLANG[13],BOLANG[14],BOLANG[15],BOLANG[16],BOLANG[17],BOLANG[18],BOLANG[19]])
L_BOLANG = [len(BOLANG[0]),len(BOLANG[1]),len(BOLANG[2]),len(BOLANG[3]),len(BOLANG[4]),len(BOLANG[5]),len(BOLANG[6]),len(BOLANG[7]),len(BOLANG[8]),len(BOLANG[9]),len(BOLANG[10]),len(BOLANG[11]),len(BOLANG[12]),len(BOLANG[13]),len(BOLANG[14]),len(BOLANG[15]),len(BOLANG[16]),len(BOLANG[17]),len(BOLANG[18]),len(BOLANG[19])]

M_BINGLIE = np.concatenate([BINGLIE[0],BINGLIE[1],BINGLIE[2],BINGLIE[3],BINGLIE[4],BINGLIE[5],BINGLIE[6],BINGLIE[7],BINGLIE[8],BINGLIE[9],BINGLIE[10],BINGLIE[11],BINGLIE[12],BINGLIE[13],BINGLIE[14],BINGLIE[15],BINGLIE[16],BINGLIE[17],BINGLIE[18],BINGLIE[19]])
L_BINGLIE = [len(BINGLIE[0]),len(BINGLIE[1]),len(BINGLIE[2]),len(BINGLIE[3]),len(BINGLIE[4]),len(BINGLIE[5]),len(BINGLIE[6]),len(BINGLIE[7]),len(BINGLIE[8]),len(BINGLIE[9]),len(BINGLIE[10]),len(BINGLIE[11]),len(BINGLIE[12]),len(BINGLIE[13]),len(BINGLIE[14]),len(BINGLIE[15]),len(BINGLIE[16]),len(BINGLIE[17]),len(BINGLIE[18]),len(BINGLIE[19])]

M_BAOWEI = np.concatenate([BAOWEI[0],BAOWEI[1],BAOWEI[2],BAOWEI[3],BAOWEI[4],BAOWEI[5],BAOWEI[6],BAOWEI[7],BAOWEI[8],BAOWEI[9],BAOWEI[10],BAOWEI[11],BAOWEI[12],BAOWEI[13],BAOWEI[14],BAOWEI[15],BAOWEI[16],BAOWEI[17],BAOWEI[18],BAOWEI[19]])
L_BAOWEI = [len(BAOWEI[0]),len(BAOWEI[1]),len(BAOWEI[2]),len(BAOWEI[3]),len(BAOWEI[4]),len(BAOWEI[5]),len(BAOWEI[6]),len(BAOWEI[7]),len(BAOWEI[8]),len(BAOWEI[9]),len(BAOWEI[10]),len(BAOWEI[11]),len(BAOWEI[12]),len(BAOWEI[13]),len(BAOWEI[14]),len(BAOWEI[15]),len(BAOWEI[16]),len(BAOWEI[17]),len(BAOWEI[18]),len(BAOWEI[19])]

M_BU = np.concatenate([BU[0],BU[1],BU[2],BU[3],BU[4],BU[5],BU[6],BU[7],BU[8],BU[9],BU[10],BU[11],BU[12],BU[13],BU[14],BU[15],BU[16],BU[17],BU[18],BU[19]])
L_BU = [len(BU[0]),len(BU[1]),len(BU[2]),len(BU[3]),len(BU[4]),len(BU[5]),len(BU[6]),len(BU[7]),len(BU[8]),len(BU[9]),len(BU[10]),len(BU[11]),len(BU[12]),len(BU[13]),len(BU[14]),len(BU[15]),len(BU[16]),len(BU[17]),len(BU[18]),len(BU[19])]

M_BIXU = np.concatenate([BIXU[0],BIXU[1],BIXU[2],BIXU[3],BIXU[4],BIXU[5],BIXU[6],BIXU[7],BIXU[8],BIXU[9],BIXU[10],BIXU[11],BIXU[12],BIXU[13],BIXU[14],BIXU[15],BIXU[16],BIXU[17],BIXU[18],BIXU[19]])
L_BIXU = [len(BIXU[0]),len(BIXU[1]),len(BIXU[2]),len(BIXU[3]),len(BIXU[4]),len(BIXU[5]),len(BIXU[6]),len(BIXU[7]),len(BIXU[8]),len(BIXU[9]),len(BIXU[10]),len(BIXU[11]),len(BIXU[12]),len(BIXU[13]),len(BIXU[14]),len(BIXU[15]),len(BIXU[16]),len(BIXU[17]),len(BIXU[18]),len(BIXU[19])]

M_CANLAN = np.concatenate([CANLAN[0],CANLAN[1],CANLAN[2],CANLAN[3],CANLAN[4],CANLAN[5],CANLAN[6],CANLAN[7],CANLAN[8],CANLAN[9],CANLAN[10],CANLAN[11],CANLAN[12],CANLAN[13],CANLAN[14],CANLAN[15],CANLAN[16],CANLAN[17],CANLAN[18],CANLAN[19]])
L_CANLAN = [len(CANLAN[0]),len(CANLAN[1]),len(CANLAN[2]),len(CANLAN[3]),len(CANLAN[4]),len(CANLAN[5]),len(CANLAN[6]),len(CANLAN[7]),len(CANLAN[8]),len(CANLAN[9]),len(CANLAN[10]),len(CANLAN[11]),len(CANLAN[12]),len(CANLAN[13]),len(CANLAN[14]),len(CANLAN[15]),len(CANLAN[16]),len(CANLAN[17]),len(CANLAN[18]),len(CANLAN[19])]

# model definition ["Aoman","Anzhao","Bolang","Binglie","Baowei","Bu","Bixu","Canlan"]
Model_AOMAN = hmm.GMMHMM()
Model_ANZHAO = hmm.GMMHMM()
Model_BOLANG = hmm.GMMHMM()
Model_BINGLIE = hmm.GMMHMM()
Model_BAOWEI = hmm.GMMHMM()
Model_BU = hmm.GMMHMM()
Model_BIXU = hmm.GMMHMM()
Model_CANLAN = hmm.GMMHMM()
# training
Model_AOMAN.fit(M_AOMAN, L_AOMAN)
Model_ANZHAO.fit(M_ANZHAO, L_ANZHAO)
Model_BOLANG.fit(M_BOLANG, L_BOLANG)
Model_BINGLIE.fit(M_BINGLIE, L_BINGLIE)
Model_BAOWEI.fit(M_BAOWEI, L_BAOWEI)
Model_BU.fit(M_BU, L_BU)
Model_BIXU.fit(M_BIXU, L_BIXU)
Model_CANLAN.fit(M_CANLAN, L_CANLAN)

COUNT = 0
#1 test Anzhao
seen1 = np.loadtxt('./D_test/1.txt')
logp1 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq1 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp1[0],seq1[0]=Model_ANZHAO.decode(seen1, algorithm='viterbi')
logp1[1],seq1[1]=Model_AOMAN.decode(seen1, algorithm='viterbi')
logp1[2],seq1[2]=Model_BAOWEI.decode(seen1, algorithm='viterbi')
logp1[3],seq1[3]=Model_BINGLIE.decode(seen1, algorithm='viterbi')
logp1[4],seq1[4]=Model_BIXU.decode(seen1, algorithm='viterbi')
logp1[5],seq1[5]=Model_BOLANG.decode(seen1, algorithm='viterbi')
logp1[6],seq1[6]=Model_BU.decode(seen1, algorithm='viterbi')
logp1[7],seq1[7]=Model_CANLAN.decode(seen1, algorithm='viterbi')
print("次数     单词     结果")
print("  1      按照     "+word[logp1.index(max(logp1))])
if logp1.index(max(logp1)) == 0:
    COUNT += 1

# 2 Aoman
seen2 = np.loadtxt('./D_test/2.txt')
logp2 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq2 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp2[0],seq2[0]=Model_ANZHAO.decode(seen2, algorithm='viterbi')
logp2[1],seq2[1]=Model_AOMAN.decode(seen2, algorithm='viterbi')
logp2[2],seq2[2]=Model_BAOWEI.decode(seen2, algorithm='viterbi')
logp2[3],seq2[3]=Model_BINGLIE.decode(seen2, algorithm='viterbi')
logp2[4],seq2[4]=Model_BIXU.decode(seen2, algorithm='viterbi')
logp2[5],seq2[5]=Model_BOLANG.decode(seen2, algorithm='viterbi')
logp2[6],seq2[6]=Model_BU.decode(seen2, algorithm='viterbi')
logp2[7],seq2[7]=Model_CANLAN.decode(seen2, algorithm='viterbi')
print("  2      傲慢     "+word[logp2.index(max(logp2))])
if logp2.index(max(logp2)) == 1:
    COUNT += 1

# 3 Aoman
seen3 = np.loadtxt('./D_test/3.txt')
logp3 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq3 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp3[0],seq3[0]=Model_ANZHAO.decode(seen3, algorithm='viterbi')
logp3[1],seq3[1]=Model_AOMAN.decode(seen3, algorithm='viterbi')
logp3[2],seq3[2]=Model_BAOWEI.decode(seen3, algorithm='viterbi')
logp3[3],seq3[3]=Model_BINGLIE.decode(seen3, algorithm='viterbi')
logp3[4],seq3[4]=Model_BIXU.decode(seen3, algorithm='viterbi')
logp3[5],seq3[5]=Model_BOLANG.decode(seen3, algorithm='viterbi')
logp3[6],seq3[6]=Model_BU.decode(seen3, algorithm='viterbi')
logp3[7],seq3[7]=Model_CANLAN.decode(seen3, algorithm='viterbi')
print("  3      傲慢     "+word[logp3.index(max(logp3))])
if logp3.index(max(logp3)) == 1:
    COUNT += 1

# 4 Baowei
seen4 = np.loadtxt('./D_test/4.txt')
logp4 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq4 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp4[0],seq4[0]=Model_ANZHAO.decode(seen4, algorithm='viterbi')
logp4[1],seq4[1]=Model_AOMAN.decode(seen4, algorithm='viterbi')
logp4[2],seq4[2]=Model_BAOWEI.decode(seen4, algorithm='viterbi')
logp4[3],seq4[3]=Model_BINGLIE.decode(seen4, algorithm='viterbi')
logp4[4],seq4[4]=Model_BIXU.decode(seen4, algorithm='viterbi')
logp4[5],seq4[5]=Model_BOLANG.decode(seen4, algorithm='viterbi')
logp4[6],seq4[6]=Model_BU.decode(seen4, algorithm='viterbi')
logp4[7],seq4[7]=Model_CANLAN.decode(seen4, algorithm='viterbi')
print("  4      保卫     "+word[logp4.index(max(logp4))])
if logp4.index(max(logp4)) == 2:
    COUNT += 1

# 5 Binglie
seen5 = np.loadtxt('./D_test/5.txt')
logp5 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq5 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp5[0],seq5[0]=Model_ANZHAO.decode(seen5, algorithm='viterbi')
logp5[1],seq5[1]=Model_AOMAN.decode(seen5, algorithm='viterbi')
logp5[2],seq5[2]=Model_BAOWEI.decode(seen5, algorithm='viterbi')
logp5[3],seq5[3]=Model_BINGLIE.decode(seen5, algorithm='viterbi')
logp5[4],seq5[4]=Model_BIXU.decode(seen5, algorithm='viterbi')
logp5[5],seq5[5]=Model_BOLANG.decode(seen5, algorithm='viterbi')
logp5[6],seq5[6]=Model_BU.decode(seen5, algorithm='viterbi')
logp5[7],seq5[7]=Model_CANLAN.decode(seen5, algorithm='viterbi')
print("  5      并列     "+word[logp5.index(max(logp5))])
if logp5.index(max(logp5)) == 3:
    COUNT += 1

# 6 Bixu
seen6 = np.loadtxt('./D_test/6.txt')
logp6 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq6 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp6[0],seq6[0]=Model_ANZHAO.decode(seen6, algorithm='viterbi')
logp6[1],seq6[1]=Model_AOMAN.decode(seen6, algorithm='viterbi')
logp6[2],seq6[2]=Model_BAOWEI.decode(seen6, algorithm='viterbi')
logp6[3],seq6[3]=Model_BINGLIE.decode(seen6, algorithm='viterbi')
logp6[4],seq6[4]=Model_BIXU.decode(seen6, algorithm='viterbi')
logp6[5],seq6[5]=Model_BOLANG.decode(seen6, algorithm='viterbi')
logp6[6],seq6[6]=Model_BU.decode(seen6, algorithm='viterbi')
logp6[7],seq6[7]=Model_CANLAN.decode(seen6, algorithm='viterbi')
print("  6      必须     "+word[logp6.index(max(logp6))])
if logp6.index(max(logp6)) == 4:
    COUNT += 1

# 7 Bolang
seen7 = np.loadtxt('./D_test/7.txt')
logp7 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq7 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp7[0],seq7[0]=Model_ANZHAO.decode(seen7, algorithm='viterbi')
logp7[1],seq7[1]=Model_AOMAN.decode(seen7, algorithm='viterbi')
logp7[2],seq7[2]=Model_BAOWEI.decode(seen7, algorithm='viterbi')
logp7[3],seq7[3]=Model_BINGLIE.decode(seen7, algorithm='viterbi')
logp7[4],seq7[4]=Model_BIXU.decode(seen7, algorithm='viterbi')
logp7[5],seq7[5]=Model_BOLANG.decode(seen7, algorithm='viterbi')
logp7[6],seq7[6]=Model_BU.decode(seen7, algorithm='viterbi')
logp7[7],seq7[7]=Model_CANLAN.decode(seen7, algorithm='viterbi')
print("  7      波浪     "+word[logp7.index(max(logp7))])
if logp7.index(max(logp7)) == 5:
    COUNT += 1

# 8 Bolang
seen8 = np.loadtxt('./D_test/8.txt')
logp8 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq8 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp8[0],seq8[0]=Model_ANZHAO.decode(seen8, algorithm='viterbi')
logp8[1],seq8[1]=Model_AOMAN.decode(seen8, algorithm='viterbi')
logp8[2],seq8[2]=Model_BAOWEI.decode(seen8, algorithm='viterbi')
logp8[3],seq8[3]=Model_BINGLIE.decode(seen8, algorithm='viterbi')
logp8[4],seq8[4]=Model_BIXU.decode(seen8, algorithm='viterbi')
logp8[5],seq8[5]=Model_BOLANG.decode(seen8, algorithm='viterbi')
logp8[6],seq8[6]=Model_BU.decode(seen8, algorithm='viterbi')
logp8[7],seq8[7]=Model_CANLAN.decode(seen8, algorithm='viterbi')
print("  8      波浪     "+word[logp8.index(max(logp8))])
if logp8.index(max(logp8)) == 5:
    COUNT += 1

# 9 Bu
seen9 = np.loadtxt('./D_test/9.txt')
logp9 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq9 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp9[0],seq9[0]=Model_ANZHAO.decode(seen9, algorithm='viterbi')
logp9[1],seq9[1]=Model_AOMAN.decode(seen9, algorithm='viterbi')
logp9[2],seq9[2]=Model_BAOWEI.decode(seen9, algorithm='viterbi')
logp9[3],seq9[3]=Model_BINGLIE.decode(seen9, algorithm='viterbi')
logp9[4],seq9[4]=Model_BIXU.decode(seen9, algorithm='viterbi')
logp9[5],seq9[5]=Model_BOLANG.decode(seen9, algorithm='viterbi')
logp9[6],seq9[6]=Model_BU.decode(seen9, algorithm='viterbi')
logp9[7],seq9[7]=Model_CANLAN.decode(seen9, algorithm='viterbi')
print("  9      捕      "+word[logp9.index(max(logp9))])
if logp9.index(max(logp9)) == 6:
    COUNT += 1


# 10 Canlan
seen10 = np.loadtxt('./D_test/10.txt')
logp10 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
seq10 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
logp10[0],seq10[0]=Model_ANZHAO.decode(seen10, algorithm='viterbi')
logp10[1],seq10[1]=Model_AOMAN.decode(seen10, algorithm='viterbi')
logp10[2],seq10[2]=Model_BAOWEI.decode(seen10, algorithm='viterbi')
logp10[3],seq10[3]=Model_BINGLIE.decode(seen10, algorithm='viterbi')
logp10[4],seq10[4]=Model_BIXU.decode(seen10, algorithm='viterbi')
logp10[5],seq10[5]=Model_BOLANG.decode(seen10, algorithm='viterbi')
logp10[6],seq10[6]=Model_BU.decode(seen10, algorithm='viterbi')
logp10[7],seq10[7]=Model_CANLAN.decode(seen10, algorithm='viterbi')
print("  10     灿烂     "+word[logp10.index(max(logp10))])
if logp10.index(max(logp10)) == 7:
    COUNT += 1

print("识别率： " + str(COUNT/10.0))