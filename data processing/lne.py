import pandas as pd
import numpy as np

analysis_pre_all = pd.read_csv("/Users/qiuchutong/Desktop/new model result/washed set.csv")
analysis_pre_all["总患者lne"] = np.log(analysis_pre_all["总患者"])
column_to_reorder = analysis_pre_all.pop("总患者lne")
insert_position = analysis_pre_all.columns.get_loc("总患者")+1
analysis_pre_all.insert(insert_position,"总患者lne",column_to_reorder)
analysis_pre_all["总患者"] = np.log(analysis_pre_all["总患者"])

analysis_pre_all.to_csv("/Users/qiuchutong/Desktop/new model result/min_max.csv",index = False)