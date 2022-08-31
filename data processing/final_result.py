import pandas as pd
import numpy as np

entropy1 = pd.read_csv("/Users/qiuchutong/Desktop/new model result/entropy.csv")
entropy1 = entropy1.values.tolist()
entropy = pd.DataFrame(entropy1,columns=["entropy","coefficient"])

critic = pd.read_csv("/Users/qiuchutong/Desktop/new model result/critic.csv")

weak_list = ["综合推荐热度","总文章","健康号阅读数","总访问"]
strong_list = ["诊后报到患者", "诊后评价","感谢信","心意礼物","健康号粉丝数"]

entire_data_head_list = weak_list + strong_list
entire_washed_data = pd.read_csv("/Users/qiuchutong/Desktop/new model result/min_max.csv")
#entropy
#weak
weak_entropy = entire_washed_data[weak_list]
index_list_weak = []
for position in weak_list:
    index = entropy.index[entropy["entropy"] == position].values.tolist()
    index_list_weak.extend(index)
weak_coefficient = entropy.iloc[index_list_weak]
weak_co = weak_coefficient["coefficient"].values.tolist()
for i in range(0,len(weak_list)):
  weak_entropy[weak_list[i]] = weak_entropy[weak_list[i]].mul(weak_co[i])
weak_entropy["sum"] = weak_entropy.sum(axis=1)
weak_insert_position = entire_washed_data.columns.get_loc("健康号阅读数")+1
entire_washed_data.insert(weak_insert_position,"entropy weak",weak_entropy["sum"])

#strong
strong_entropy = entire_washed_data[strong_list]
index_list_strong = []
for position in strong_list:
    index = entropy.index[entropy["entropy"] == position].values.tolist()
    index_list_strong.extend(index)
strong_coefficient = entropy.iloc[index_list_strong]
strong_co = strong_coefficient["coefficient"].values.tolist()
for i in range(0,len(strong_list)):
  strong_entropy[strong_list[i]] = strong_entropy[strong_list[i]].mul(strong_co[i])
strong_entropy["sum"] = strong_entropy.sum(axis=1)
strong_insert_position = entire_washed_data.columns.get_loc("entropy weak")+1
entire_washed_data.insert(strong_insert_position,"entropy strong",strong_entropy["sum"])

#critic
#weak
weak_critic = entire_washed_data[weak_list]
index_list_weak = []
for position in weak_list:
    index = critic.index[critic["critic"] == position].values.tolist()
    index_list_weak.extend(index)
weak_coefficient = critic.iloc[index_list_weak]
weak_co = weak_coefficient["coefficient"].values.tolist()
for i in range(0,len(weak_list)):
  weak_critic[weak_list[i]] = weak_critic[weak_list[i]].mul(weak_co[i])
weak_critic["sum"] = weak_critic.sum(axis=1)
weak_insert_position = entire_washed_data.columns.get_loc("entropy strong")+1
entire_washed_data.insert(weak_insert_position,"critic weak",weak_critic["sum"])


#strong
strong_critic = entire_washed_data[strong_list]
index_list_strong = []
for position in strong_list:
    index = critic.index[critic["critic"] == position].values.tolist()
    index_list_strong.extend(index)
strong_coefficient = critic.iloc[index_list_strong]
strong_co = strong_coefficient["coefficient"].values.tolist()
for i in range(0,len(strong_list)):
  strong_critic[strong_list[i]] = strong_critic[strong_list[i]].mul(strong_co[i])
strong_critic["sum"] = strong_critic.sum(axis=1)
strong_insert_position = entire_washed_data.columns.get_loc("critic weak")+1
entire_washed_data.insert(strong_insert_position,"critic strong",strong_critic["sum"])


entire_washed_data["entropy weak*strong"] = entire_washed_data["entropy weak"] * entire_washed_data["entropy strong"]
entire_washed_data["critic weak*strong"] = entire_washed_data["critic weak"] * entire_washed_data["critic strong"]
print(entire_washed_data)
print(entire_washed_data)

index_list = [1,2,3,4]
test = entire_washed_data.iloc[:,index_list]
print(test)

entire_washed_data.to_excel("/Users/qiuchutong/Desktop/new model result/final_data.xlsx",index = False)


