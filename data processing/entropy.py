import pandas as pd
import numpy as np

#1_18弱交互

analysis_1_18_weak = pd.read_csv("/Users/qiuchutong/Desktop/new model result/min_max.csv",usecols=["综合推荐热度", "总文章","健康号阅读数","总访问"])
n1,m1 = analysis_1_18_weak.shape
for col1 in analysis_1_18_weak.columns:
    sum_weak_1_18 = analysis_1_18_weak[col1].sum()
    analysis_1_18_weak[col1] = analysis_1_18_weak[col1].div(sum_weak_1_18)
test1 = analysis_1_18_weak * np.log(analysis_1_18_weak).replace([np.inf,-np.inf],0)
k1 = -1/np.log(n1)
e1 = k1 * (test1.sum(axis=0))
w_1_18 = (1-e1)/np.sum(1-e1)
entire_result = pd.DataFrame(w_1_18)

print(entire_result)
#1_18强交互
analysis_1_18_strong = pd.read_csv("/Users/qiuchutong/Desktop/new model result/min_max.csv",usecols=["诊后报到患者", "诊后评价","感谢信","心意礼物","健康号粉丝数"])
n1,m1 = analysis_1_18_strong.shape
for col1 in analysis_1_18_strong.columns:
    sum_strong_1_18 = analysis_1_18_strong[col1].sum()
    analysis_1_18_strong[col1] = analysis_1_18_strong[col1].div(sum_strong_1_18)
test1 = analysis_1_18_strong * np.log(analysis_1_18_strong).replace([np.inf,-np.inf],0)
k1 = -1/np.log(n1)
e1 = k1 * (test1.sum(axis=0))
s_1_18 = (1-e1)/np.sum(1-e1)

frames = [entire_result,s_1_18]
entire_result = pd.concat(frames)
entire_result.to_csv("/Users/qiuchutong/Desktop/new model result/entropy.csv",index = True)