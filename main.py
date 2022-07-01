import subprocess
import time
import telebot

from sys_info_func import RunInShell
from sys_info_func import CPUUsage
from sys_info_func import TaskUsageTotal
from sys_info_func import TaskUsageNow
from sys_info_func import CacheUsage
from config import sepa
from service_monitor_func import ServStat



while(True):
    #开始构造返回信息
    info_text=''
    info_text+='<strong>HostName:</strong> '+RunInShell('hostname') #vps hostname
    info_text+='<strong>CPU:</strong> '+CPUUsage()+'%\n' #cpu usage
    #处理内存使用
    mem_info=CacheUsage()
    mem_total=mem_info[0]
    mem_free=mem_info[1]
    mem_percent=mem_info[2]
    info_text+='<strong>Memory:</strong> '+'总内存：'+mem_total+'MB  未使用：'+mem_free+'MB  占用比：'+mem_percent+'\n' #memory usage
    info_text+='<strong>Task:</strong> '+'总任务数：'+TaskUsageTotal()+'  正在运行：'+TaskUsageNow()+'\n' #task usage

    #Service Montinor Function
    info_text+=sepa+'\n'
    info_text+=ServStat()+'\n'


    #使用Bot发送生成的信息
    bot = telebot.TeleBot("5050467713:AAFQultsmN1YdFnp9MVZiBakXSEXVr1ED6M", parse_mode='HTML')
    bot.send_message(975140440,info_text)
    time.sleep(3)