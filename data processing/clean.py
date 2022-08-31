import pandas as pd
import numpy as np
wait_clean = pd.read_csv("/Users/qiuchutong/Desktop/new model result/0125.csv",encoding='gbk')

wait_clean.drop(["教育职称"],axis=1,inplace=True)
wait_clean.drop(["医院"],axis=1,inplace=True)
wait_clean.drop(["健康号文章数"],axis=1,inplace=True)
wait_clean.drop(["线下诊后评价总数"],axis=1,inplace=True)
wait_clean.drop(["线上服务患者数"],axis=1,inplace=True)
#wait_clean.drop(["门诊类型"],axis=1,inplace=True)

print("新数据集")
print(wait_clean)

#获奖情况
wait_clean["获奖情况"].replace("None","0")
for i in range(0,len(wait_clean)):
    if wait_clean["获奖情况"][i] != "None":
        wait_clean["获奖情况"][i] = "1"
    else:
        wait_clean["获奖情况"][i] = "0"

for j in range(0,len(wait_clean)):
    if "国际" in wait_clean["门诊类型"][j]:
        wait_clean["门诊类型"][j] = "8"
    elif "特需" in wait_clean["门诊类型"][j]:
        wait_clean["门诊类型"][j] = "7"
    elif "名医" in wait_clean["门诊类型"][j]:
        wait_clean["门诊类型"][j] = "6"
    elif "VIP" in wait_clean["门诊类型"][j]:
        wait_clean["门诊类型"][j] = "5"
    elif "专家" in wait_clean["门诊类型"][j]:
        wait_clean["门诊类型"][j] = "4"
    elif "专病" in wait_clean["门诊类型"][j] or "专科" in wait_clean["门诊类型"][j]:
        wait_clean["门诊类型"][j] = "3"
    elif "普通门诊" in wait_clean["门诊类型"][j]:
        wait_clean["门诊类型"][j] = "1"
    elif "None" in wait_clean["门诊类型"][j] or "停诊" in wait_clean["门诊类型"][j]:
        wait_clean["门诊类型"][j] = "0"
    else:#所有未属于以上类别的其他门诊和少数表述不清晰的门诊，全部属于其他门诊
        wait_clean["门诊类型"][j] = "2"

#如果需要更改过滤的总访问，在这里修改数字即可，注意这里是满足条件的删除
wait_clean.drop(wait_clean[wait_clean.总访问 < 1000].index,inplace=True)
#wait_clean.drop(wait_clean[wait_clean.总访问 > 10000000].index,inplace=True)

wait_clean.drop(wait_clean[(wait_clean.总患者 < 50) & (wait_clean.综合推荐热度 > 4.5)].index,inplace=True)

wait_clean = wait_clean.replace({"暂未收到评价":"0"})

wait_clean.dropna(axis=0,how="any",inplace=True)

wait_clean["总患者le"] = np.log(wait_clean["总患者"])
wait_clean.to_csv("/Users/qiuchutong/Desktop/new model result/washed set.csv",index = False)



