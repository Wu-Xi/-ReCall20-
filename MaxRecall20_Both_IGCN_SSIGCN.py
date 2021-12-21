import sys


##############文件起始编号
start_num=7100


#####################log文件数量
num_total_log=9

filePath='D:\KEG实验室\吴熙\ContrastiveLearning-main\\1210\\'#############这里填写你自己的log文件夹地址

#       --------------------------------------------------------------------  以上部分是程序头部，以下部分，请勿随意改动，

def find_from_IGCN():
    '''
    在加  cl_weight =0   情况下，寻找最大ReCall20文件

    对应了登记表的， IGCN     


    '''
    R10_max='0'
    R20_max='0'
    N10_max='0'
    N20_max='0'
    NameSpace={'cl_weight':'','coldstartexp':'','dataset':'','l2_weight_decay':'','lr':'','model':''}
    fileName_max=''
    def find_NameSpace(nameSpace_string):
        string=nameSpace_string
        #print(string)
        NameSpace1={'cl_weight':'','coldstartexp':'','dataset':'','l2_weight_decay':'','lr':'','model':''}
        for i in NameSpace1:
            temp=string[string.find(i)+len(i)+1:]
            temp=temp[:temp.find(',')]
            NameSpace1[i]=temp
        #print(NameSpace1)

        return NameSpace1
    for i in range(0,num_total_log):

        fileName=str(start_num+i)+'.log'

        fileName=filePath+fileName

        text = open(fileName, "r", encoding="utf-8-sig")

        contents = text.read()

        cl_weight=contents[contents.find('Namespace')+len('Namespace')+1:]
        cl_weight=cl_weight[cl_weight.find('cl_weight')+len('cl_weight')+1:]

        #print(cl_weight)
        cl_weight=cl_weight[:cl_weight.find(', ')]
        #print(cl_weight)
        
        cl_weight=cl_weight.strip()
        #print('------------------------------------',cl_weight,'--------------',len(cl_weight))
        
        
        if cl_weight=='0.0':

            R10=contents[contents.find('Recall@10')+10:contents.find('Recall@10')+18] 

            R20=contents[contents.find('Recall@20')+10:contents.find('Recall@20')+18]

            N10=contents[contents.find('NDCG@10')+8:contents.find('NDCG@10')+16]

            N20=contents[contents.find('NDCG@20')+8:contents.find('NDCG@20')+16]

            

            if R20>R20_max:
                R10_max=R10
                R20_max=R20
                N10_max=N10
                N20_max=N20
                NameSpacexx=contents[contents.find('Namespace')+len('Namespace'):]
                NameSpacexx=NameSpacexx[:NameSpacexx.find(')')]
                NameSpacexx=find_NameSpace(NameSpacexx)
                NameSpace=NameSpacexx
                fileName_max=fileName
                #print(NameSpace)
        else:                   #           自带纠错功能，，，秒啊
            print('傻逼，这是IGCN吗？  cl_weight=',cl_weight)
            #print(type(cl_weight))
            sys.exit(0)
    print('\n   在登记表  IGCN  中，登记   ,此时    cl_weight= 0 ----  ',end="")
    print(fileName_max,'\n')
    #print(NameSpace,'===========================')
    print('数据集：',NameSpace['dataset'],'--','模型：',NameSpace['model'],'--','冷启动：',NameSpace['coldstartexp'],'--','cl_weight：',NameSpace['cl_weight'],'--','lr：',NameSpace['lr'],'--','l2_weight_decay：',NameSpace['l2_weight_decay'],'--\n')
    print('Recall@10--Recall@20--NDCG@10--NDCG@20')
    print(R10_max,R20_max,N10_max,N20_max)

def find_from_SSIGCN():
    '''

    cl_weight=0.2 0.5  下，寻找最大ReCall20文件

    对应了登记表中，ssigcn 只登记      cl=0.2   0.5 

    '''
    R10_max='0'
    R20_max='0'
    N10_max='0'
    N20_max='0'
    NameSpace={'cl_weight':'','coldstartexp':'','dataset':'','l2_weight_decay':'','lr':'','model':''}
    fileName_max=''
    def find_NameSpace(nameSpace_string):
        string=nameSpace_string
        #print(string)
        NameSpace={'cl_weight':'','coldstartexp':'','dataset':'','l2_weight_decay':'','lr':'','model':''}
        for i in NameSpace:
            temp=string[string.find(i)+len(i)+1:]
            temp=temp[:temp.find(',')]
            NameSpace[i]=temp
        #print(NameSpace)
        return NameSpace
    for i in range(0,num_total_log):

        fileName=str(start_num+i)+'.log'

        fileName=filePath+fileName

        text = open(fileName, "r", encoding="utf-8-sig")

        contents = text.read()

        cl_weight=contents[contents.find('Namespace')+len('Namespace')+1:]
        cl_weight=cl_weight[cl_weight.find('cl_weight')+len('cl_weight')+1:]
        cl_weight=cl_weight[:cl_weight.find(',')] 

        cl_weight=cl_weight.strip()

        if cl_weight=='0.0':############   不要 CL_WEIGHT 为 0 的文件

            continue

        else:

            R10=contents[contents.find('Recall@10')+10:contents.find('Recall@10')+18] 

            R20=contents[contents.find('Recall@20')+10:contents.find('Recall@20')+18]

            N10=contents[contents.find('NDCG@10')+8:contents.find('NDCG@10')+16]

            N20=contents[contents.find('NDCG@20')+8:contents.find('NDCG@20')+16]

            if R20>R20_max:
                R10_max=R10
                R20_max=R20
                N10_max=N10
                N20_max=N20
                NameSpacexx=contents[contents.find('Namespace')+len('Namespace'):]
                NameSpacexx=NameSpacexx[:NameSpacexx.find(')')]
                NameSpacexx=find_NameSpace(NameSpacexx)
                NameSpace=NameSpacexx
                fileName_max=fileName


    print('\n   在登记表  SSIGCN  中，登记   ,此时    (不统计 cl_weight= 0) ----  ',end="")
    print(fileName_max,'\n')
    print('数据集：',NameSpace['dataset'],'--','模型：',NameSpace['model'],'--','冷启动：',NameSpace['coldstartexp'],'--','cl_weight：',NameSpace['cl_weight'],'--','lr：',NameSpace['lr'],'--','l2_weight_decay：',NameSpace['l2_weight_decay'],'--\n')
    print('Recall@10--Recall@20--NDCG@10--NDCG@20')
    print(R10_max,R20_max,N10_max,N20_max)

print('\n\n\n\nIGCN 模型（在加  cl_weight =0  情况下，寻找最大ReCall20文件），SSIGCN 模型（不统计 cl_weight =0 ）')
print('--------------------------------------------------------------------------')
model_num=input(' 【请输入模型代码】 IGCN 模型输入 0 , SSIGCN 模型输入 1：----- ')
model_num=int(model_num)
if model_num==0 or model_num==1:
    if model_num==0:
        find_from_IGCN()
    else:
        find_from_SSIGCN()

else:
    print('输入不合法，憨批！！！')
print('\n\n\n\n')
