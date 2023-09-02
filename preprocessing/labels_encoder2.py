
import json
import time
import pdb
import pickle as pkl
from tqdm import tqdm
from utils import entity_or_attribute, entity_select, is_attribute, is_entity, Bad_Attribute, label_select

entity_id = 0
label_id = 0
num_labels = 0
sum = 0 
json_file = 'latest-all.json'
# raw_txt = open('raw_txt.txt', 'w', encoding='utf-8') 
# label_txt = open('label_txt.txt', 'w', encoding='utf-8') # split, arrays, torch.tensor
entity_id2des_dict = pkl.load(open('entity_id2des_dict.pkl', 'rb'))
# entity_id2des_dict = {}
label_id2idx_dict = pkl.load(open('label_id2idx_dict.pkl', 'rb'))

json_all = open(json_file, 'r')
# pdb.set_trace()
for line in json_all:
    l1 = len(line)
    s1 = line
    if l1 < 5:
        continue
    while s1[-1] != '}' :
        l1 -= 1
        s1 = line[:l1]
    js = json.loads(s1)
    if 'id' not in js.keys():
        continue
    id = js['id']
    sum += 1
    if sum % 1000 == 0:
        print(f"done {sum} find {entity_id}")
    if id in entity_id2des_dict.keys():
        continue
    if label_select(js) == False:
        continue
    label = js['labels']['en']['value']
    description = js['descriptions']['en']['value']
    entity_txt = label+" be "+description
    entity_id2des_dict[id] = entity_txt
    entity_id += 1
    
label_txt_list = []

for id in label_id2idx_dict.keys():
    if id not in entity_id2des_dict.keys():
        print(f"Warning! {id} is not in entity_id2des_dict! May this label id is not in rule!")
        label_txt_list.append("label be empty.")
    else:
        des = entity_id2des_dict[id]
        label_txt_list.append(des)

# f1 = open('entity_id2des_dict.pkl', 'wb')
# pkl.dump(entity_id2des_dict, f1)
# f1.close()

# f2 = open('label_id2idx_dict.pkl', 'wb')
# pkl.dump(label_id2idx_dict, f2)
# f2.close()

f3 = open('label_txt_list2.pkl', 'wb')
pkl.dump(label_txt_list, f3)
f3.close()

pdb.set_trace()












