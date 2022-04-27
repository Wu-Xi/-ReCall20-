import os
print(os.getcwd())
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from multiprocessing.dummy import Process
import psutil as ps
import time
import logging

import click
# 第三方 SMTP 服务
MAIL_HOST="smtp.qq.com"  #设置服务器
MAIL_USER="159*********@qq.com"    #用户名
MAIL_PASS="tqdkbh*********"   #口令 
SENDER = '1591********@qq.com'
RECEIVERS = ['3155**********@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
Process_Check_Time=600
# 每隔10分钟检查你指定的进程是否存活

logging.basicConfig(filename='System_Runtime.log', filemode="w", level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning(os.getpid())




def get_mem():
    x=ps.virtual_memory()
    var_size_M=1024*1024
    total_mem=float(x.total)/(var_size_M)
    available_mem=float(x.available)%(var_size_M)
    percent_mem=float(x.percent)
    free_mem=float(x.free)%(var_size_M)
    return total_mem,available_mem,percent_mem,free_mem

class EmailUtil(object):

    smtpObj = smtplib.SMTP() 
    smtpObj.connect(MAIL_HOST, 25)    # 25 为 SMTP 端口号
    smtpObj.login(MAIL_USER,MAIL_PASS) 
    

    def __init__(self,message,from_name,to_name,subject) -> None:
        self.message = MIMEText(message, 'plain', 'utf-8')
        self.message['From'] = Header(from_name, 'utf-8')
        self.message['To'] =  Header(to_name, 'utf-8')
        self.message['Subject'] = Header(subject, 'utf-8')

        

    def send_email(self) -> None:
        try:
            self.smtpObj.sendmail(SENDER, RECEIVERS, self.message.as_string())
            logging.info("Success: email send ") 
        except Exception as e:
            logging.error(e)
            logging.error("Error: cannot send email") 


def get_flag_dict(file):
    GLOABLE_CONFIG_PID=file
    flag_dict=dict()
    for i in GLOABLE_CONFIG_PID:
        flag_dict[i] = ps.pid_exists(int(i))

    return flag_dict

 
@click.command()
@click.argument('file',nargs=-1)
def get_periment(file):
    error_pid=[]
    EmailUtil(str(file)+"跟踪程序已启动","联通服务器","**","计算实验进程情况").send_email()
    while True:
        x1,x2,x3,x4=get_mem()
        string_cpu="本机的CPU物理核心为："+str(ps.cpu_count(logical=False))+" 个，逻辑核心为："+str(ps.cpu_count())+" 个，使用率为："+ str(ps.cpu_percent())+" %"
        logging.info(string_cpu)
        string_mem="本机的Memory的使用率为： "+str(x3)+"% ,总量为： "+str(x1)+"M， 空闲量为："+str(x4)+"M"
        logging.info(string_mem)

        flag_dict = get_flag_dict(file)
        

        for i in flag_dict:
            flag=flag_dict.get(i)

                    
            if not flag:
                logging.error(str(i)+"PiD has been killed !")
                if i in error_pid:
                    pass
                else:
                    error_message=str(time.asctime())+  str(i)+"  has been killed"
                    EmailUtil(error_message,"联通服务器","**",str(i)).send_email()
                    error_pid.append(i)
                
    

                break
            
            my_pid=ps.Process(int(i))
            xx=my_pid.memory_info().rss/(1024*1024*1024)
            string_pid="进程"+str(i)+"实际占用的内存空间为："+str(xx)+"G"
            logging.info(string_pid)
        if not (True in flag_dict.values()):
            break
        logging.info("\n")
        time.sleep(Process_Check_Time)


if __name__ == "__main__":
    get_periment()
