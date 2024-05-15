import pandas as pd
import json
import string
import os
from tqdm import tqdm


data =pd.read_json("/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/tamal_dataset.jsonl", lines=True)

#print(len(data))

def list_files_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    return files

#total = 55271
#train = 44015
#valid = 5396
#test = 5723

#missing = 134
test_data_path = "/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/Java250_processed_pdg_data/all-classes/valid"

files_train = list_files_in_folder(test_data_path)



files_train_set = set(files_train)
print(len(files_train_set))

fileName = []
for fle in files_train:
     java_name = fle.split("_")
     fileName.append(java_name[0])

#print(len(fileName))
files_train_set = set(fileName)

#print(data['label'][0])
new_data = []
for code, label, file_name in tqdm(zip(data['code'], data['label'], data['fileName'])):
    # Split the file_name to extract the Java name

    # Check if the Java name is in files_train_set
    if file_name in fileName:
        # Construct the JSON object as a string
        json_str = json.dumps({"code": code, "label": label, "fileName": file_name})
        new_data.append(json_str)

with open("/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/tamal_valid.jsonl", "w") as f:
    for item in new_data:
        f.write("%s\n" % item)

print(len(new_data))
# str = "s380201673_NA_p02971_graph_dump_209.txt"
# strs = str.split("_")
# print(strs[0])

