import pandas as pd
import numpy as np

#1_18弱交互
analysis_1_18_weak = pd.read_csv("/Users/qiuchutong/Desktop/new model result/min_max.csv",usecols=["综合推荐热度", "总文章","健康号阅读数","总访问"])
n,m = analysis_1_18_weak.shape
weak_1_18 = np.array(analysis_1_18_weak)
R = np.array(pd.DataFrame(weak_1_18).corr())
delta = np.zeros(m)
c = np.zeros(m)
for j in range(0,m):
    delta[j] = weak_1_18[:,j].std()
    c[j] = R.shape[0] - R[:,j].sum()
delta = pd.Series(delta, dtype=object).fillna(0).tolist()
C = delta * c
w = C/sum(C)
head_list = ["综合推荐热度", "总文章","健康号阅读数","总访问"]
data = {"critic":head_list,"coefficient":w}
df_weak_1_18 = pd.DataFrame(data)

#1_18强交互
analysis_1_18_strong = pd.read_csv("/Users/qiuchutong/Desktop/new model result/min_max.csv",usecols=["诊后报到患者", "诊后评价","感谢信","心意礼物","健康号粉丝数"])
n,m = analysis_1_18_strong.shape
strong_1_18 = np.array(analysis_1_18_strong)
R = np.array(pd.DataFrame(strong_1_18).corr())
delta = np.zeros(m)
c = np.zeros(m)
for j in range(0,m):
    delta[j] = strong_1_18[:,j].std()
    c[j] = R.shape[0] - R[:,j].sum()
delta = pd.Series(delta, dtype=object).fillna(0).tolist()
C = delta * c
w = C/sum(C)
head_list = ["诊后报到患者", "诊后评价","感谢信","心意礼物","健康号粉丝数"]
data = {"critic":head_list,"coefficient":w}
df_strong_1_18 = pd.DataFrame(data)

df = pd.concat([df_weak_1_18,df_strong_1_18])
print(df)
df.to_csv("/Users/qiuchutong/Desktop/new model result/critic.csv",index = False)



