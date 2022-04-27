# -ReCall20-



6、trace_Pid.py  在系统进程池中查询指定的进程，是否还存活。然后发邮件提示
刚启动的时候会发第一封邮件，告诉你程序监控已启动
程序每个10分钟会检查一下，你指定的进程是否还存活，
若不存活，则会发邮件通知你哪一个进程已经被干掉了。
当你指定的所有进程都已死亡，则该程序停止运行
---
使用方法：
nuhup python trace_Pid.py xxxxx   yyyyyy
(xxxxx,yyyyy)表示你指定的进程号


5、OneFile_search.py针对单个log文件进行实验参数查找以及实验结果查询
---
使用方法：
python3 w_run.py 31308




4、把之前的两个分别寻找IGCN和SSIGCN的代码文件，合并到了一起，一个代码去分别寻找；两个模型的最大值
----------
【输入】：代码有三个输入需要更改
【NEW  输入】：在代码运行时选择相应的模型，IGCN或者SSIGCN模型
新的代码【输出】见下图：
![image](https://user-images.githubusercontent.com/52689912/146871969-2160ab6a-d666-4006-806f-bd0b31f02ce2.png)                                                         
<br>
</br>
3、最久远的的两个文件已 OUT ,现在已经上传最新的版本，maxRecall20_SSIGCN.py 以及 MaxRecall20_IGCN.py
----

maxRecall20_SSIGCN.py     对应了，在加  cl_weight =0   情况下，寻找最大ReCall20文件

MaxRecall20_IGCN.py       对应了，在  cl_weight=0.2 0.5  下，寻找最大ReCall20文件                                                                                       





1、【maxRecall20.py】
----
在王申学长的实验结果中，寻找最大的ReCall20文件，并输出相关的实验数据

通过字符串定位的方式来寻找相关的数据

【输入】：代码有三个输入需要更改

【输出】：程序会遍历所有的log文件，并输出【当前】寻找到的最大ReCall20文件，并输出相关的参数，

输出的最后一个log文件就是所有的log文件里面最大的ReCall20,如下图的2907.log

![image](https://user-images.githubusercontent.com/52689912/143667605-969eb6ae-775b-48f9-be8a-878d57a13cde.png)
  

2、【 MaxRecall20_in_cl_weight.py】

在 cl_weight=0.0 的情况下，寻找最大的Recall20文件    
