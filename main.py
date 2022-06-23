import subprocess
import time
import telebot

from func import RunInShell
from func import CPUUsage
from func import TaskUsageTotal
from func import TaskUsageNow
from func import CacheUsage



while(True):
    #开始构造返回信息
    info_text=''
    info_text+='<strong>HostName:</strong> '+RunInShell('hostname') #vps hostname
    info_text+='<strong>CPU Usage:</strong> '+CPUUsage()+'\n' #cpu usage
    #处理内存使用
    mem_info=CacheUsage()
    mem_total=mem_info[0]
    mem_free=mem_info[1]
    mem_percent=mem_info[2]
    info_text+='<strong>Memory Usage:</strong> '+CPUUsage()+'\n' #cpu usage
    info_text+='<strong>Task Usage:</strong> '+'总任务数：'+TaskUsageTotal()+'  正在运行：'+TaskUsageNow()+'\n' #task usage



    #使用Bot发送生成的信息
    bot = telebot.TeleBot("5050467713:AAFQultsmN1YdFnp9MVZiBakXSEXVr1ED6M", parse_mode='HTML')
    bot.send_message(975140440,info_text)
    time.sleep(3)