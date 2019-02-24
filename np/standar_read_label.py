import numpy as np

path=r'C:\Users\mrliangcb\Desktop\note\extra_feature\open\true_labels_training.txt'

def truth_to_arr(path):
    return np.asarray(list(map(float, open(path, 'r').read())))
	
#truth = truth_to_arr(path)#读到的是label的一维np
#print(truth)

print(len(open(path, 'r').read()))#读到了一个20W长度的str

print(list(map(float, open(path, 'r').read())))#转化为list 元素为0.0  1.0 原本的str，每个字符都转成float了