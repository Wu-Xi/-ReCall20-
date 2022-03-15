import os
import click


file_path=os.path.dirname(__file__)

file_name=31300


@click.command()
@click.argument('file')
def search_file(file):
    file_name = file+'.log'
    print(file_name)
    text = open(file_name, "r", encoding="utf-8-sig")
    contents = text.read()
    NameSpace=contents[contents.find('Namespace')+len('Namespace'):]
    #print(contents.find('Namespace'))
    NameSpace=str(NameSpace)
    
    NameSpace=NameSpace[:NameSpace.find(')')].strip()
    #print(NameSpace.find(')'))
    #print("--------",NameSpace)

    bitch_size=NameSpace[NameSpace.find('bitch_size')+len('bitch_size')+2+1:]
    bitch_size=bitch_size[:bitch_size.find(',')]

    cl_weight=NameSpace[NameSpace.find('cl_weight')+len('cl_weight')+1:]
    cl_weight=cl_weight[:cl_weight.find(',')]

    coldstartexp=NameSpace[NameSpace.find('coldstartexp')+len('coldstartexp')+1:]
    coldstartexp=coldstartexp[:coldstartexp.find(',')]

    dataset=NameSpace[NameSpace.find('dataset')+len('dataset')+1:]
    dataset=dataset[:dataset.find(',')]

    dropout=NameSpace[NameSpace.find('dropout')+len('dropout')+1:]
    dropout=dropout[:dropout.find(',')]

    l2_weight_decay=NameSpace[NameSpace.find('l2_weight_decay')+len('l2_weight_decay')+1:]
    l2_weight_decay=l2_weight_decay[:l2_weight_decay.find(',')]

    lr=NameSpace[NameSpace.find('lr')+len('lr')+1:]
    lr=lr[:lr.find(',')]

    
    model=NameSpace[NameSpace.find('model')+len('model')+1:]
    model=model[:model.find(',')]

    temperature=NameSpace[NameSpace.find('temperature')+len('temperature')+1:]
    temperature=temperature[:temperature.find(',')]

    NameSpace_new={'dataset':dataset,'lr':lr,'l2_weight_decay':l2_weight_decay,'cl_weight':cl_weight,'dropout':dropout,'temperature':temperature,'bitch_size':bitch_size,'model':model,'coldstartexp':coldstartexp}

    R10=contents[contents.find('Recall@10')+10:contents.find('Recall@10')+18] 

    R20=contents[contents.find('Recall@20')+10:contents.find('Recall@20')+18]

    N10=contents[contents.find('NDCG@10')+8:contents.find('NDCG@10')+16]

    N20=contents[contents.find('NDCG@20')+8:contents.find('NDCG@20')+16]

    for i in NameSpace_new:
        print(i,'  ---  ',NameSpace_new[i])
    print('\n')
    print('Recall@10---Recall@20---NDCG@10---NDCG@20')
    print(R10,R20,N10,N20)

if __name__ == '__main__':
    search_file()
