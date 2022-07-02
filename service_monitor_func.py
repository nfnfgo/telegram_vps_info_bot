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

    # Use the  shell respone to check the service status
    for serv_item in serv_dict.keys():
        check_list=serv_dict[serv_item]
        print(check_list)

    return serv_res_text