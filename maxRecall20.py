
start_num=2900##############文件起始编号
num_total_log=12#####################log文件数量

filePath='D:\KEG实验室\吴熙\HGCN-source\\'
R20_max='0'
for i in range(0,num_total_log):
    fileName=str(start_num+i)+'.log'
    fileName=filePath+fileName
    text = open(fileName, "r", encoding="utf-8-sig")
    contents = text.read()
    R10=contents[contents.find('Recall@10')+10:contents.find('Recall@10')+18] 
    R20=contents[contents.find('Recall@20')+10:contents.find('Recall@20')+18]
    #print(R20,i)
    N10=contents[contents.find('NDCG@10')+8:contents.find('NDCG@10')+16]
    N20=contents[contents.find('NDCG@20')+8:contents.find('NDCG@20')+16]
    if R20>R20_max:
        R20_max=R20
        print(fileName)
        print(R10,R20,N10,N20)
        print('\n')
    #break
