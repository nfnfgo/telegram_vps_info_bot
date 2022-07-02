import time
import subprocess



#基础函数，用于在shell中执行命令并返回shell的打印结果
def RunInShell(comm):
    subp=subprocess.Popen(comm,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    return_text=subp.communicate()[0]
    if return_text is None:
        return_text='Error: Program has return None'
    return return_text

#从top指令中提取CPU相关信息
def CPUUsage():
    top_text=RunInShell('top -bn 1 -i -c')
    top_text_lines=top_text.splitlines()
    cpu_usage_line=top_text_lines[2]
    cpu_usage_info_list=cpu_usage_line.split(',  ')
    cpu_usage=cpu_usage_info_list[0]
    cpu_usage=cpu_usage.replace('%Cpu(s):','')
    cpu_usage=cpu_usage.replace(' ','')
    cpu_usage=cpu_usage.replace('us','')
    print('cpu_usage',cpu_usage)
    return str(cpu_usage)

#task运行情况
def TaskUsageTotal():
    top_text=RunInShell('top -bn 1 -i -c')
    top_text_lines=top_text.splitlines()
    task_usage_line=top_text_lines[1]
    task_usage_line=task_usage_line.replace(' ','')
    task_usage_info_list=task_usage_line.split(',')
    task_usage_info_total=task_usage_info_list[0] #处理总进程数量
    task_usage_info_total=task_usage_info_total.replace('Tasks:','')
    task_usage_info_total=task_usage_info_total.replace('total','')
    print('task total:',task_usage_info_total)
    return str(task_usage_info_total)

#task运行情况，正在运行
def TaskUsageNow():
    top_text=RunInShell('top -bn 1 -i -c')
    top_text_lines=top_text.splitlines()
    task_usage_line=top_text_lines[1]
    task_usage_line=task_usage_line.replace(' ','')
    task_usage_info_list=task_usage_line.split(',')
    task_usage_info_now=task_usage_info_list[1] #处理正在运行进程数量
    task_usage_info_now=task_usage_info_now.replace(' ','')
    task_usage_info_now=task_usage_info_now.replace('running','')
    print('task now:',task_usage_info_now)
    return str(task_usage_info_now)

#内存使用状况
def CacheUsage():
    #获取基础的行，删除空格，并基于逗号对行进行切分
    top_text=RunInShell('top -bn 1 -i -c')
    top_text_lines=top_text.splitlines()
    mem_usage_line=top_text_lines[3]
    mem_usage_line=mem_usage_line.replace(' ','')
    mem_usage_info_list=mem_usage_line.split(',')
    #处理内存数据，总内存
    mem_usage_info_total=mem_usage_info_list[0]
    mem_usage_info_total=mem_usage_info_total.replace(' ','')
    mem_usage_info_total=mem_usage_info_total.replace(':','')
    mem_usage_info_total=mem_usage_info_total.replace('KiBMem','')
    mem_usage_info_total=mem_usage_info_total.replace('total','')
    #处理已使用内存
    mem_usage_info_used=mem_usage_info_list[2]
    mem_usage_info_used=mem_usage_info_used.replace(' ','')
    mem_usage_info_used=mem_usage_info_used.replace('used','')
    #计算使用百分比
    percent=format((float(mem_usage_info_used)/float(mem_usage_info_total))*100,'.1f')
    percent=str(percent)+'%'
    mem_usage_info_free=float(mem_usage_info_total)-float(mem_usage_info_used)
    #构造返回数列
    return_list=[str(mem_usage_info_total),str(mem_usage_info_free),percent]
    return return_list