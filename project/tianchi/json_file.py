from data_pre import dicom_metainfo, dicom2array
import os
import json
import glob
import SimpleITK as sitk
import pandas as pd

trainPath = r'd:\Thunderbolt download\tianchi_spine\train\train'
jsonPath = r'd:\Thunderbolt download\tianchi_spine\lumbar_train51_annotation.json'
# studyUid,seriesUid,instanceUid,annotation
annotation_info = pd.DataFrame(columns=('studyUid','seriesUid','instanceUid','annotation'))
json_df = pd.read_json(jsonPath)
for idx in json_df.index:
    studyUid = json_df.loc[idx,"studyUid"]
    seriesUid = json_df.loc[idx,"data"][0]['seriesUid']
    instanceUid =  json_df.loc[idx,"data"][0]['instanceUid']
    annotation =  json_df.loc[idx,"data"][0]['annotation']
    row = pd.Series({'studyUid':studyUid,'seriesUid':seriesUid,'instanceUid':instanceUid,'annotation':annotation})
    annotation_info = annotation_info.append(row,ignore_index=True)
dcm_paths = glob.glob(os.path.join(trainPath,"**","**.dcm"))
# 'studyUid','seriesUid','instanceUid'
tag_list = ['0020|000d','0020|000e','0008|0018']
dcm_info = pd.DataFrame(columns=('dcmPath','studyUid','seriesUid','instanceUid'))
for dcm_path in dcm_paths:
    try:
        studyUid,seriesUid,instanceUid = dicom_metainfo(dcm_path,tag_list)
        row = pd.Series({'dcmPath':dcm_path,'studyUid':studyUid,'seriesUid':seriesUid,'instanceUid':instanceUid })
        dcm_info = dcm_info.append(row,ignore_index=True)
    except:
        continue
result = pd.merge(annotation_info,dcm_info,on=['studyUid','seriesUid','instanceUid'])
result = result.set_index('dcmPath')['annotation']
print(result)