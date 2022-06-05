import json
from tqdm import tqdm
# with open('./data/train_with_summary.txt', 'r', encoding="utf-8") as file:
#     for line in tqdm(file.readlines()):
#         try:
#             file_line = json.loads(line)
#         except:
#             print("line", line)
#         finally:
#             print("ok")

# import json
# path='./data/nlpcc_data.json'
# f = open(path,'r',encoding='utf-8')
# m = json.load(f) # json.load() 这种方法是解析一个文件中的数据 # json.loads() 需要先将文件，读到一个变量作为字符串, 解析一个字符串中的数
# # with open("test.txt","w",encoding='utf-8') as f:
# #     for index in range(len(m)):
# #         print(m[index])
# #         f.write("{'summarization': '"+m[index]['summarization']+"', 'article': '"+m[index]['article']+"'}\n")
#
# print(type(m[0]))
# print(m[1])
count = 0
with open('./data/mini_set_test.txt', 'r', encoding="utf-8") as file:
    for line in tqdm(file.readlines()):
        count +=1
        file_line = json.loads(line)
        print(str(count) + "ok"+line)
