import pandas as pd
from sklearn.preprocessing import MinMaxScaler

analysis_pre_all = pd.read_csv("/Users/qiuchutong/Desktop/new model result/washed set.csv")
#not_change = pd.DataFrame(analysis_pre_all[["id","姓名","职称","科室","获奖情况","出诊医院与科室"]].copy())
min_max_scaler = MinMaxScaler()
analysis_pre_all[["综合推荐热度","总访问","总文章","总患者","诊后报到患者","诊后评价","感谢信","心意礼物","健康号粉丝数","健康号阅读数"]] = min_max_scaler.fit_transform(analysis_pre_all[["综合推荐热度","总访问","总文章","总患者","诊后报到患者","诊后评价","感谢信","心意礼物","健康号粉丝数","健康号阅读数"]])
print(analysis_pre_all)

analysis_pre_all.to_csv("/Users/qiuchutong/Desktop/new model result/min_max.csv",index = False)