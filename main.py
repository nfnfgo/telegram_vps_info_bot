import subprocess
import time
import telebot


#编写基础函数
def RunInShell(comm):
    subp=subprocess.Popen(comm,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    return_text=subp.communicate()[0]
    if return_text is None:
        return_text='Error: Program has return None'
    return return_text

#开始构造返回信息
info_text=''
info_text+='<strong>HostName:</strong> '+RunInShell('hostname') #vps hostname
info_text+='<strong>CPU Usage:</strong> '+RunInShell('top -bn 1 -i -c')+'\n' #vps hostname



#使用Bot发送生成的信息
bot = telebot.TeleBot("5050467713:AAFQultsmN1YdFnp9MVZiBakXSEXVr1ED6M", parse_mode='HTML')
bot.send_message(975140440,info_text)