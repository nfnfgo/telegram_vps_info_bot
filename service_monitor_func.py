import subprocess
import time

import config



# Provide a unified func to run sth in shell and got the respones
def RunInShell(comm):
    subp=subprocess.Popen(comm,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    return_text=subp.communicate()[0]
    if return_text is None:
        return_text='Error: Program has return None'
    return return_text

# Check service status
def ServStat():
    # Read config in config.py
    serv_dict=config.service_dict # "serv" means "service"

    # get service status text in by using shell command
    serv_res_text=RunInShell('service --status-all')
    res_text_lines=serv_res_text.split('\n')

    # Initialize return text here for later ref
    res_text='<strong>VPS Service Status: </strong>\n'

    # Use the  shell respone to check the service status
    for serv_item in serv_dict.keys(): # try to check every single item by iterate through the list
        check_list=serv_dict[serv_item]
        line_times=0
        for line in res_text_lines: # iterate every single lines, try to find the corresponding line
            line_times+=1
            check_times=0 # set a flag variable, if it equals element nums in check_list then pass
            for text in check_list:
                if text in line:
                    check_times+=1
            if check_times==len(check_list):
                res_text+=serv_item+': Running\n'
                break
            elif line_times<len(res_text_lines):
                pass
            else:
                res_text+=serv_item+': <strong>Error Occurred!</strong>\n'

        

    return res_text